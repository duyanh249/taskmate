from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.
class TaskList(models.Model):
    manage=models.ForeignKey(User,on_delete=CASCADE,default=None)
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)
    def __str__(self):
        return self.task+'--'+str(self.done)


