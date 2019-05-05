from django.db import models

# Create your models here.
class todoItem(models.Model):
    content = models.TextField()
    parent_id = models.ForeignKey("todoItem", on_delete=models.CASCADE, null=True) # changed this to an object, need to make subsequent changes to views
    description = models.CharField(max_length=200, blank=True, default='')
    # listId = models.IntegerField()

class todoList(models.Model):
    userId = models.IntegerField()
    listId = models.IntegerField()
