from django.shortcuts import redirect, render
from .models import ChatMessage
from django.conf import settings
import google.generativeai as genai



genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")


def send_message(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        bot_response = model.generate_content(user_message)

        ChatMessage.objects.create(
            user_message=user_message,
            bot_response=bot_response.text
        )
    
    return redirect('list_messages')


def list_messages(request):
    messages = ChatMessage.objects.all().order_by('-created_at')
    return render(request, 'chat/chat_history.html', {'messages': messages})


def delete_chat_history(request):
    if request.method == 'POST':
        ChatMessage.objects.all().delete()
    return redirect('list_messages')