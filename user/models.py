from django.db import models

class student_info(models.Model):
    # 字符
    t_name=models.CharField(max_length=20,default='fyw')
    t_pwd=models.CharField(max_length=20,default='')
    # 数字
    t_age=models.IntegerField(default=21)   # 使用数字长度设置无效
    # 图片
    t_image=models.ImageField(max_length=300,upload_to="image/%Y/%m",default="image/default.jpg")

class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"