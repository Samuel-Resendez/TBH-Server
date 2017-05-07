from django.contrib import admin
from toBeHuman.models import Entry
# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entry, EntryAdmin)