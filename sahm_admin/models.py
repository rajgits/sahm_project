from django.db import models

# Create your models here. 
# class employees(models.Model):
#     firstname=models.CharField(max_length=100)
#     lastname=models.CharField(max_length=50)
#     emp_id=models.IntegerField()

#     def _str_(self):
#         return self.firstname

# class blogs(models.Model):
#     firstnameblog=models.CharField(max_length=100)
#     lastnameblog=models.CharField(max_length=50)
#     blog_id=models.IntegerField()
    
#     def __str__(self):
#         return self.firstnameblog
       

class quetion(models.Model):
    firstq=models.CharField(max_length=100)
    seconq=models.CharField(max_length=45)
    lastq=models.CharField(max_length=50)
    queition_id=models.IntegerField()
     
class About(models.Model):
    about_id = models.IntegerField()
    heading1 = models.CharField(max_length=245, blank=True, null=True)
    description1 = models.TextField()
    description2 = models.TextField()
    heading2 = models.CharField(max_length=245, blank=True, null=True)
    description3 = models.TextField()
    status = models.IntegerField(blank=True, null=True)
    lang_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'about'

    

   

