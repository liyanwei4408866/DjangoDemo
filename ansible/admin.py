from django.contrib import admin

# Register your models here.
from .models import Grade,Student

class StudentInfo(admin.TabularInline):#StackedInline
    model = Student
    extrm = 2

@admin.register(Grade) #admin.site.register(Grade, GradeAdmin)
class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentInfo]
    list_display = ['pk', 'gname', 'gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 10
    # 分组
    fieldsets=[
        ("base",{"fields":["gname","gdate","isDelete"]}),
        ("num",{"fields":["ggirlnum","gboynum"]}),
    ]

@admin.register(Student) #admin.site.register(Student, StudentAdmin)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"
    list_display = ['pk', 'sname', gender,'sage','scontend','isDelete']
    list_filter = ['sname']
    search_fields = ['sname']
    