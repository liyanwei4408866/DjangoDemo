from django.contrib import admin

# Register your models here.
from .models import Snippet

@admin.register(Snippet) #admin.site.register(Grade, GradeAdmin)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'code','created','linenos','language','style']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 10
    

