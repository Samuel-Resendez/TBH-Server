from django.contrib import admin
from TBHServer.models import Entry

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ("id","qOneResponse","qTwoResponse","qThreeResponse","qFourResponse")


admin.site.register(Entry, EntryAdmin)