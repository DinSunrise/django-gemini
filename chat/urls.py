from django.urls import path
from .views import *

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('', list_messages, name='list_messages'),
    path('delete/', delete_chat_history, name='delete_chat_history'),
]
