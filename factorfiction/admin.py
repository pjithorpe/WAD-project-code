from django.contrib import admin
from factorfiction.models import Page, UserProfile, GameArticle, Comment

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','url')

admin.site.register(Page, PageAdmin,)
admin.site.register(GameArticle)
admin.site.register(UserProfile)
admin.site.register(Comment)

# These register our models to the admin site
