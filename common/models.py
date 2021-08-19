from django.db import models


class Users_info(models.Model):
    username= models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)
    pin = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_info'