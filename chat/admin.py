
from .models import Feedback, ChatHistory, account, APICallCount, ButtonClick
from django.contrib import admin




class APICallCountAdmin(admin.ModelAdmin):
    list_display = ('function_name', 'count', 'last_called')
    list_filter = ('last_called',)  # Enables filtering by the `last_called` field (time)

admin.site.register(APICallCount, APICallCountAdmin)



admin.site.register(Feedback)
admin.site.register(ChatHistory)
admin.site.register(account)
admin.site.register(ButtonClick)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'bot_message', 'feedback', 'feedback_type', 'created_at')