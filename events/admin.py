from django.contrib import admin

from events.models import Topic, WebPage, AccessRecords

# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecords)
