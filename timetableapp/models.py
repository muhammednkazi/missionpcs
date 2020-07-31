from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class data(models.Model):
    table_id=models.AutoField(primary_key=True)
    content=models.TextField(max_length=3000,default="")
    timestamp=models.DateTimeField(default=now)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    