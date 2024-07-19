from django.contrib import admin

# Register your models here.
# chat/admin.py
from django.contrib import admin
from .models import Feedback, ChatHistory, account

admin.site.register(Feedback)
admin.site.register(ChatHistory)
admin.site.register(account)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'bot_message', 'feedback', 'feedback_type', 'created_at')