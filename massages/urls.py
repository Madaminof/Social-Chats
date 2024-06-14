from django.urls import path
from .views import MessagesListView, HomeView, SendMessage

app_name = 'conversation'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('message-list/', MessagesListView.as_view(), name='message-list'),
    path('message-list/<int:user_id>/', MessagesListView.as_view(), name='message-with-user'),
    path('send-message/<int:user_id>/', SendMessage.as_view(), name='send-message'),
]
