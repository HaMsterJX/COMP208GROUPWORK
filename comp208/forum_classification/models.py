from django.db import models
from django.utils import timezone

# 论坛分类
class ForumClassification(models.Model):
    # 论坛id
    type_id = models.AutoField(primary_key=True)
    # 论坛分类的名称
    name = models.CharField(max_length=100, help_text='Enter the name of the forum type')
    # 论坛描述
    description = models.TextField(help_text='Enter a description of the forum type')
    # 论坛图标
    icon = models.ImageField(upload_to='forum_type_icons/', blank=True, null=True, help_text='Upload an icon for the forum type')
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now, help_text='Enter the creation time of the forum type')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True, help_text='Enter the last update time of the forum type')

    def __str__(self):
        return str(self.type_id)
