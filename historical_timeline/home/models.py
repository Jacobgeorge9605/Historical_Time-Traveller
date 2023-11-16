from django.db import models

# # Create your models here.

# # class

class Events(models.Model):
    user_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    is_admin = models.BooleanField(default = False)
    
    def __str__(self):
      return self.name
    
    
class Category(models.Model):
   category_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length = 255)

   def __str__(self):
      return self.name


class Events(models.Model):
   eve_id = models.AutoField(primary_key = True)
   eve_name = models.CharField(max_length = 255)
   link = models.CharField(255)
   description = models.CharField(255)
   eve_date = models.DateTimeField(blank=True , null=True)
   likes = models.IntegerField()
   eve_tag = models.IntegerField(unique = True)
   eve_image = models.ImageField(upload_to='home/Event_images',null=True)
   
   def __str__(self):
      return self.name
   

class Tags(models.Model):
   tag_id = models.AutoField(primary_key=True)
   name = models.CharField(255)

   def __str__(self):
      return self.name
   

class Tag_table(models.Model):
   tag_tab = models.AutoField(primary_key=True)
   tag_id = models.IntegerField()
   eve_tag = models.IntegerChoices()
   




    
   
