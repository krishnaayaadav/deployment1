from django.contrib import admin
from .models import Expense

# Register your models here.

@admin.register(Expense)
class ExpenseModel(admin.ModelAdmin):
    list_display = ('pk', 'title', 'expense_user', 'expense_date', 'expense_amount', 'description', )