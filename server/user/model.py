from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def Config(self, username, nickname, password):
        self.username = username
        self.nickname = nickname
        self.password = password
