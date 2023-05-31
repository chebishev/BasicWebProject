from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    # you can rewrite __self__ method for custom view of the database data in the admin panel
    # it can be overriden in the admin.py with list_display = ('id', 'name', 'number')
    def __str__(self):
        return f"ID: {self.id}; Name: {self.name}; Number: {self.number}"
