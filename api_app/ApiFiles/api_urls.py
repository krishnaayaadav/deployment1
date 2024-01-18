
from django.urls import path
from api_app.ApiFiles import api_views

urlpatterns = [

    # API Endpoitns here
    path('expenses/all/', api_views.ExpenseListAPI.as_view(), name='get_all_expenses' ),
]