import hashlib
from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64, null=False)
    password = models.CharField(max_length=256, null=False, default='123456')

    def set_password(self, password):

        m = hashlib.md5(password)

        s = m.hexdigest()
        return s

    class Meta:
        db_table = 'user'
