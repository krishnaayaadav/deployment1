

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api_app.models import Expense
from .serializers import ExpenseSerializer
from django.contrib.auth.models import User


class ExpenseListAPI(APIView):

    def get(self, request, format=None):

        all_exp    = Expense.objects.all()
        serializer = ExpenseSerializer(all_exp, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
