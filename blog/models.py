from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class Post(models.Model):
    """Model definition for Post."""
    title = models.CharField(unique=True, max_length=50, verbose_name='标题')
    slug = models.SlugField(max_length=50,unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts',verbose_name='作者')
    updated_on = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    content = models.TextField(verbose_name='内容')
    created_on = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    status = models.IntegerField(choices=STATUS, default=0,verbose_name='状态')
    class Meta:
        """Meta definition for Post."""
        ordering = ['-created_on']
    def __str__(self):
        """Unicode representation of Post."""
        return self.title

