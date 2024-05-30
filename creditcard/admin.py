from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from creditcard.models import *


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=20, default='name')
    identity_card = models.CharField(max_length=18, default='000000000000000000')

    def newEmployee(self):
        new_employee = Employee()
        return new_employee
# 信用卡审查员

class CreditCardExaminer(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    credit_examiner_id = models.AutoField(primary_key=True)  # 设置审核员id
    check_authority = models.BooleanField(default=False)
    account = models.CharField(max_length=30, default='000000')
    password = models.CharField(max_length=20, default='password')

    def examine_application(self, apply_id, credit_state):
        application = CreditCardApplication.objects.get(apply_id=apply_id)
        application.creditCardExaminer = self
        application.apply_status = True
        if credit_state in ['good', 'excellent']:
            application.apply_result = True
            CreditCard.newcard(application.online_user)  # Assuming a method to create a credit card directly
        else:
            application.apply_id_result = False
        application.save()


class SystemManager(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sys_manager_id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=30, default='000000')
    password = models.CharField(max_length=20, default='password')


    def add_credit_examiner(self, employee_id):

        try:
            employee = Employee.objects.get(id=employee_id)

            # Check if this employee is already a system manager or a credit examiner
            if SystemManager.objects.filter(employee=employee).exists():
                raise ValueError("This employee is already a system manager.")
            if CreditCardExaminer.objects.filter(employee=employee).exists():
                raise ValueError("This employee is already a creditcard examiner.")

            # If checks pass, create a new CreditCardExaminer
            new_examiner = CreditCardExaminer(
                employee=employee,
                account=employee.identity_card,  # Example account name generation
                password='default_password'  # You would want to set a proper password mechanism
            )
            new_examiner.save()
            return new_examiner

        except ObjectDoesNotExist:
            raise ValueError("No such employee exists.")

    def delete_credit_examiner(self, employee_id):
        try:
            examiner = CreditCardExaminer.objects.get(employee__id=employee_id)
            examiner.delete()
            return f"Credit examiner with employee ID {employee_id} deleted successfully."
        except CreditCardExaminer.DoesNotExist:
            return "No such credit examiner found."

    def modify_credit_examiner(self, employee_id, new_account=None, new_password=None, new_authority=None):
        try:
            examiner = CreditCardExaminer.objects.get(employee__id=employee_id)
            if new_account:
                examiner.account = new_account
            if new_password:
                examiner.password = new_password
            if new_authority:
                examiner.check_authority = new_authority
            examiner.save()
            return f"Credit examiner with employee ID {employee_id} updated successfully."
        except CreditCardExaminer.DoesNotExist:
            return "No such credit examiner found."

    def grant_credit_examiner(self, employee_id):
        try:
            examiner = CreditCardExaminer.objects.get(employee__id=employee_id)
            examiner.check_authority = True
            examiner.save()
            return f"Credit examiner with employee ID {employee_id} granted check authority."
        except CreditCardExaminer.DoesNotExist:
            return "No such credit examiner found."

    def revoke_credit_examiner(self, employee_id):
        try:
            examiner = CreditCardExaminer.objects.get(employee__id=employee_id)
            examiner.check_authority = False
            examiner.save()
            return {"success": True}
        except CreditCardExaminer.DoesNotExist:
            return {"success": False, "error": "Examiner not found"}
