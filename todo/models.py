from django.db import models

# Create your models here.
class todoItem(models.Model):
    content = models.TextField()
    parent_id = models.IntegerField()
    description = models.CharField(max_length=200, blank=True, default='')
    listId = models.IntegerField()

class todoList(models.Model):
    userId = models.IntegerField()
    listId = models.IntegerField()
