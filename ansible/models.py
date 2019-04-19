from django.db import models

# Create your models here.


class Grade(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname

    class Meta:
        db_table:"grade"

    
class StudentManager(models.Manager):
    def get_queryset(self):
        models.Manager.get_queryset(self)
        return super(StudentManager, self).get_queryset().filter(isDelete=False)
    
    def createStudent(self, name, age, gender, contend):
        stu = self.model()
        stu.sname=name
        stu.sage=age
        stu.sgender=gender
        stu.scontend=contend
        return stu

    
class Student(models.Model):
    # 自定义模型管理器
    # stuObj = models.Manager()
    stuObj2 = StudentManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField(db_column="sage")
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grade", on_delete=models.CASCADE)
    createTime = models.DateTimeField(auto_now_add=True)  # auto_now_add 新增时赋值
    updateTime = models.DateTimeField(auto_now=True)  # auto_now 修改时赋值

    def __str__(self):
        return self.sname

    class Meta:
        db_table:"student"  # 设置表名，默认为appname_classname
        ordering:['-createTime']  # 默认排序 + asc - desc
        
    # 定义一个类方法创建对象  cls==Stundent
    @classmethod
    def createStudent(cls, name, age, gender, contend):
        stu = cls(sname=name , sage=age , sgender=gender, scontend=contend)
        return stu
        
