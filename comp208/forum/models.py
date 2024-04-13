from django.db import models
from django.utils import timezone

# 论坛
class forum(models.Model):
    # 论坛id
    forum_id = models.IntegerField(primary_key=True)
    # 发论坛的用户id
    user = models.ForeignKey('user.user', on_delete=models.CASCADE, help_text='Please select the user')
    # 点击数
    hits = models.IntegerField(default=0, help_text='Enter the number of hits')
    # 标题
    title = models.CharField(max_length=200, help_text='Enter the title of the post')
    # 论坛内容
    comment = models.TextField(help_text='Enter the comment')
    # 标签
    tag = models.CharField(max_length=100, help_text='Enter the tag for the post')
    # 上传图片
    img = models.ImageField(upload_to='forum_images/', blank=True, null=True, help_text='Upload an image for the post')
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now, help_text='Enter the creation time of the post')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True, help_text='Enter the last update time of the post')
    # 所属的父论坛的id
    type_id = models.ForeignKey('forum_classification.ForumClassification', on_delete=models.CASCADE, help_text='Select the type of the post')

    def __str__(self):
        return str(self.forum_id)


