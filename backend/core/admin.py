from django.contrib import admin
from core import models

# Register your models here.
admin.site.register(models.AiChatSession)
admin.site.register(models.AiRequest)