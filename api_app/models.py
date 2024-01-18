from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    title  = models.CharField(max_length=200)
    description  = models.TextField()
    expense_date = models.DateField(auto_now_add=True)
    expense_amount = models.FloatField()
    expense_user   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_expenses')