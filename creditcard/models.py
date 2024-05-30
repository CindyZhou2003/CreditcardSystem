from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from creditcard.admin import CreditCardExaminer


class Online_user(models.Model):
    person_id = models.AutoField(primary_key=True)
    identity_card = models.CharField(max_length=18, default='000000000000000000')


# 信用卡模型
class CreditCard(models.Model):
    objects = None
    account_id = models.AutoField(primary_key=True)  # 使用AutoField自动ID
    password = models.CharField(max_length=20, default='password')  # 设置默认密码
    card_type = models.CharField(max_length=10, default='credit')
    online_user = models.ForeignKey(Online_user, on_delete=models.CASCADE, null=True)
    credit_limit = models.FloatField(default=1000.0)
    balance = models.FloatField(default=0.0)
    is_frozen = models.BooleanField(default=False)
    is_lost = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=timezone.now)  # Automatically set to today's date as default

    DEFAULT_CREDIT_LIMIT = 1000.0  # 默认信用额度

    @staticmethod
    def newcard(online_user):
        new_card = CreditCard(online_user=online_user)
        new_card.save()
        return new_card

    def modify_password(self, new_password):
        """更改信用卡密码，输入新密码"""
        if not self.password == new_password:
            self.password = new_password
            self.save()
        else:
            raise ValueError("New password is the same as the old one")

    def report_lost(self):
        """挂失信用卡，并自动冻结卡"""
        self.is_lost = True
        self.is_frozen = True
        self.save()
        return True

    def cancel_card(self):
        """取消信用卡，删除记录"""
        self.delete()
        return True

    def update_credit_limit(self, new_limit):
        """更新信用额度"""
        if self.is_lost or self.is_frozen:
            return False
        self.credit_limit = new_limit
        self.save()
        return True

    def credit_repay(self, amount):
        """还款，输入还款金额"""
        if amount < 0.0:
            raise ValueError("Amount cannot be negative.")
        self.balance -= amount
        if self.balance <= 0.0:
            self.credit_limit = self.DEFAULT_CREDIT_LIMIT
        self.save()

    def get_lost_state(self):
        """获取挂失状态"""
        return self.is_lost

    def get_frozen_state(self):
        """获取冻结状态"""
        return self.is_frozen

    def frozen_card(self):
        """冻结信用卡"""
        self.is_frozen = True
        self.save()
        return True


class Transaction(models.Model):
    transfer_record_id = models.AutoField(primary_key=True)
    account_in_id = models.IntegerField()
    account_out_id = models.IntegerField()
    transfer_amount = models.IntegerField()
    transfer_date = models.DateTimeField()

    def __str__(self):
        return self.transfer_record_id


# 申请记录
class CreditCardApplication(models.Model):
    apply_id = models.AutoField(primary_key=True)
    online_user = models.ForeignKey(Online_user, on_delete=models.CASCADE)
    creditCardExaminer = models.ForeignKey(CreditCardExaminer, on_delete=models.CASCADE)
    apply_status = models.BooleanField(default=False)
    apply_result = models.BooleanField(default=False)
    apply_date = models.DateTimeField(default=timezone.now)

    DEFAULT_CREDIT_LIMIT = 1000.0  # 默认信用额度

    def new_apply(self):
        new_application = CreditCardApplication(online_user=self.online_user)
        new_application.save()
        return new_application

    def change_state(self, apply_result, credit_examiner_id):
        self.apply_status = True
        self.apply_result = apply_result
        self.credit_examiner_id = credit_examiner_id
        self.save()

    def get_state(self):
        try:
            application = CreditCardApplication.objects.get(apply_id=self.apply_id)
            if application.apply_status:
                return application.apply_result
            else:
                return "Not ready yet."
        except CreditCardApplication.DoesNotExist:
            raise ValueError("Application not found.")
