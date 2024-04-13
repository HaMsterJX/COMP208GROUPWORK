from django.db import models
from django.utils import timezone

# 用户数据库
class user(models.Model):
    # 用户id
    user_id = models.IntegerField(primary_key=True)
    # 性别
    gender = models.CharField(max_length=100, help_text='Please enter the gender')
    # 年龄
    age = models.IntegerField(default=0, help_text='Please enter the age')
    # 登录状态
    login_state = models.CharField(max_length=100, help_text='Please enter the user state')
    # 电话
    phone = models.CharField(max_length=100, help_text='Please enter the phone number')
    # 用户名
    username = models.CharField(max_length=100, help_text='Please enter the username')
    # 昵称
    nickname = models.CharField(max_length=100, help_text='Please enter the nickname')
    # 密码
    password = models.CharField(max_length=100, help_text='Please enter the password')
    # 邮箱
    email = models.EmailField(help_text='Please enter the email')
    # 头像
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text='Please upload the avatar')
    # 生日
    birthday = models.DateField(help_text='Please enter the user\'s birthday')
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now, help_text='Please enter the account creation time')
    # 是否注册
    examine_state = models.IntegerField(default=0, help_text='Please enter if it has been registered')

    def __str__(self):
        return self.username
