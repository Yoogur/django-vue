from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=128)
    post_content = models.CharField(max_length=128,default="")
    user_name = models.CharField(max_length=128)
    post_time = models.DateTimeField(auto_now_add=True)

    def config(self, title, content):
        self.post_title = title
        self.post_content = content