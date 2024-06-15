from django.conf import settings
from django.conf.urls.static import static

from user.views import *
from django.urls import path


app_name = 'user'
urlpatterns = [
    path('', RegisterLoginPage.as_view(), name='page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


