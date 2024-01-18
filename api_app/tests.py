from django.urls import reverse
from django.test import TestCase, Client

from rest_framework import status

from .models import Expense
from django.contrib.auth.models import User

from api_app.ApiFiles.serializers import ExpenseSerializer

# api urls reverse 
get_all_articles = "get_all_expenses"


# client
client = Client()

# Expense Test Setup here for testing

class ExpenseTestSetUp(TestCase):
    """This is base class for doing test setup to performing testing """

    def setUp(self):

        # expense user here
        self.users = [
            User.objects.create(username="bhole"),
            User.objects.create(username="krish"),
        ]

        self.exp_titles  = ('Examination Fees', 'Car Repair and Servicing Charge', 'Travelling Charges')
        self.description = ('Examination Fees of LPU', "Car Repairs and service charges", "Travelling Charges here")
        self.amount      = (233, 334, 545)


        # expense objs
        def expense_creator(no_of_obs:int):

            for i in range(0, no_of_obs+1):
                Expense.objects.create(
                    title          = self.exp_titles[i],
                    description    = self.description[i],
                    expense_amount = self.amount[i],
                    expense_user   = self.users[0] if i < 2 else self.users[1]
                      )
        
        expense_creator(no_of_obs=2)

class TestExpenseListAPI(ExpenseTestSetUp):

    def test_all_expenses(self):

        api_response = client.get(reverse(get_all_articles))

        
        # test status code of api response
        try:
            self.assertEqual(api_response.status_code, status.HTTP_200_OK)

        except:
            print('API Response mis matched')

        
        # test response data

        exps       = Expense.objects.all()
        serializer = ExpenseSerializer(exps, many=True)

        # test expense counts
        json_res = api_response.json()

        try:
            self.assertEqual(exps.count(), len(json_res))
        except:
            print('API Response Content Count Mis Matched')

        # test api response data with database data is same or not

        try:
            self.assertEqual(json_res, serializer.data)
        
        except:
            print('API Response data mis-matched ')

        
        # test expense titles 
        for index in range(0, 3):
            try:
                self.assertEqual(json_res[index]['title'], self.exp_titles[index])
            
            except:
                print('Expense title mis matched at index: ', index)

        # test expese descriptions
        for index in range(0, 3):
            try:
                self.assertEqual(json_res[index]['description'], self.description[index])
            
            except:
                print('Expense Description mis matched at index: ', index)
        
        # test expense amount
        for index in range(0, 3):

            try:
                self.assertEqual(json_res[index]['expense_amount'], self.amount[index])
            
            except:
                print('Expense Amount mis matched at index: ', index)
        
        print('\n ExpenseListAPI Test Case are Passed ')

      
        




    
        

