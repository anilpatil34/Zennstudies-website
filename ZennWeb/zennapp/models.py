from django.db import models # type: ignore

# Create your models here.

# Here we create our contact models data base and we store user information section vise we make the columns of every part

# migration - create changes and store in file 
# migrate - apply the pending changes created by makemigrations


# This below code is python code
class Contact(models.Model):
    # This is our contact app and we store user information in below columns section
# This above class name is our database table name and below names are colums of the table
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

#   If we want to showcase the user name in database wich person try to contact us we can use this below method

    def __str__(self):
        return self.name