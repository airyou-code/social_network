from distutils.command.upload import upload
import logging
import hashlib
import os
from django.db import models


def get_image_path(instance, filename):
    hashname = hashlib.sha1(filename.encode()).hexdigest() + '.jpg'
    return os.path.join('profimg', hashname[:2], hashname[2:4], hashname[4:6], hashname)

class User(models.Model):
    login = models.CharField('login', max_length=25)
    password = models.CharField('password', max_length=20)
    token = models.CharField('token', max_length=20)
    mail = models.CharField('mail', max_length=30)
    phone = models.CharField('phone', max_length=20)
    profImg = models.ImageField('profImg', upload_to=get_image_path)
    description = models.CharField('description', max_length=250)
    confirm = models.CharField('confirm', max_length=3)
    dateTime = models.DateTimeField('dateTime', auto_now=True)

    def __str__(self):
        return f"{self.id}. {self.login}"


