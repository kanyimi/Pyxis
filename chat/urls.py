from django.urls import path
from .views import index, send_message_to_external_api, submit_feedback

urlpatterns = [
    path('', index, name='index'),
    path('api/send_message', send_message_to_external_api, name='send_message_to_external_api'),
    path('api/submit_feedback/', submit_feedback, name='submit_feedback'),
]
