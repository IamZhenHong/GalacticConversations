from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import os
import openai
# Create your views here.

open_api_key = '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'
openai.api_key = open_api_key
client = OpenAI( api_key = open_api_key)
def ask_open_api(msg):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "You are yoda from star wars and talks just like him especially his sentence form\n"
        },
        {
        "role": "assistant",
        "content": "Evil, the dark side is. Harm to others, one must not seek. Peace and balance in the Force, we must strive for."
        },
        {
        "role": "user",
        "content": msg
        },
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return format_response(response)

def format_response(response):
    if response.choices:
        messages = [choice.message.content for choice in response.choices]
        formatted_response = '\n'.join(messages)
        return formatted_response
    else:
        return "No response received from the API"


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_open_api(message)
        message = f"User said: {message}. "
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')