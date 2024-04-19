

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView



urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('api/products/',include('api.urls.products')),
    path('api/categories/',include('api.urls.categories')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/',include('users.urls')),
    path('api/',include('cart.urls')),
    path('api/razorpay/', include('accounts.urls')),
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)