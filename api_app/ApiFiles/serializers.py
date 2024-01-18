
from rest_framework import serializers

from api_app.models import Expense
from django.contrib.auth.models import User

class ExpenseSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=False, read_only=True)
    title = serializers.CharField(max_length = 200)
    description  = serializers.CharField(style={
        'base_template': 'textarea.html'
    })
    expense_user = serializers.CharField()
    expense_amount = serializers.FloatField()
    expense_date   = serializers.DateField()

    

