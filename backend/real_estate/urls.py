from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
import rest_framework
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/accounts/', include('accounts.urls'), name='accounts'),
    path('api/realtors/', include('realtors.urls'), name='realtors'),
    path('api/listings/', include('listings.urls'), name='listings'),
    path('api/contacts/', include('contacts.urls'), name='contacts'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
