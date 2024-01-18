
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('expense/', include('api_app.urls')),

    # api documentation

    path('api/schema/', SpectacularAPIView().as_view(),    name='api_schema' ),
    path('api/docs/',   SpectacularSwaggerView().as_view(url_name='api_schema'),  ),

]
