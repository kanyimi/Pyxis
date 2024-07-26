from django.urls import path
from .views import index, home, send_message_to_external_api, submit_feedback, register, login_view, logout_view, testwidget

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path("testwidget",testwidget, name = "testwidget"),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/send_message', send_message_to_external_api, name='send_message_to_external_api'),
    path('api/submit_feedback/', submit_feedback, name='submit_feedback'),
]
