from django.contrib import admin
from factorfiction.models import Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','url')


admin.site.register(Page, PageAdmin,)
admin.site.register(UserProfile)

# Register your models here.
