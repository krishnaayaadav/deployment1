
from django.urls import path, include
from api_app.ApiFiles import api_views

urlpatterns = [

    # Expense API Endpoints
    path('api/', include('api_app.ApiFiles.api_urls')),
]