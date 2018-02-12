from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
# Register your models here.

class PageInline(admin.ModelAdmin):
    #    fieldsets = [
    #           ('TITLE',{'fields':['title']}),
    #            ('CATEGORY',{'fields':['category']}),
    #            ('URL',{'fields':['url']}),
    #            ]
    
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
#    fieldsets = [
#                (None,{'fields':['date']}),
#                ('Date information',{'fields':['name']}),
#               ]
#    inlines = [PageInline]
#   list_display = ('name','date','was_published_recently')
#   list_filter = ['date']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageInline)
admin.site.register(UserProfile)
