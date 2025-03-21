from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [

    # Genera el archivo schema.yml/json:
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Documentación interactiva (Swagger UI):
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('admin/', admin.site.urls),
    path('account/', include("user_app.urls")),
]
