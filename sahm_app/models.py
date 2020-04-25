from django.db import models
from django.db.models import F, Q, When
from django.template.defaultfilters import truncatechars  # or truncatewords
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
       



CHOICES = (
    ('1', 'Full time'),
    ('2', 'Part time'),
    ('3', 'Full time or Part time'),
    ('4', 'Freelance'),
)

CHOICES_PAY = (
    ('1', 'Pay hourly'),
    ('2', 'Daily'),
    ('3', 'Weekly'),
    ('4', 'Monthly'),
)

CHOICES_GENDER = (
    (1, 'Male'),
    (2, 'Fe-male'),
)

CHOICES_PHONE = (
    (1, 'Yes'),
    (2, 'No'),
)

class Users(models.Model):
   # google_id = models.TextField()
  #  facebook_id = models.TextField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255,blank=False)
    email = models.CharField(max_length=100)
    gender = models.IntegerField(blank=True, null=True,choices=CHOICES_GENDER)
    date_birth = models.CharField(max_length=100, blank=True, null=True)
    phonecodecountry = models.CharField(max_length=10)
    phonecode = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    show_phone = models.IntegerField(choices=CHOICES_PHONE)
   # password = models.CharField(max_length=250)
   # address = models.TextField()
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
   # profile_image = models.CharField(max_length=100)
  # profile_image_verified = models.IntegerField()
    designation = models.CharField(max_length=255)
    # company_name = models.CharField(max_length=255)
    # experience_year = models.IntegerField()
    # experience_month = models.IntegerField()
    #industry_id = models.IntegerField()
    summary = models.TextField()
    education = models.TextField()
    # full_work_type = models.IntegerField()
    # part_work_type = models.IntegerField()
    # fullpart_work_type = models.IntegerField()
    # freelance_work_type = models.IntegerField()
    # fixed_price = models.CharField(max_length=50)
    # fixed_price_currency = models.IntegerField()
    perhour_price = models.CharField(max_length=50)
    perhour_price_currency = models.IntegerField()
    # phoneopt = models.CharField(max_length=50)
    # phoneotpstatus = models.IntegerField()
    # otpdatetime = models.DateTimeField()
    # emailotp = models.CharField(max_length=50)
    # emailotpstatus = models.IntegerField()
    # emailotpdatetime = models.DateTimeField()
    # registration_date = models.DateTimeField()
    # lastupdate_date = models.DateTimeField()
    # activation_status = models.IntegerField() 
    # status = models.IntegerField()
    work_type = models.CharField(max_length=45, blank=True, null=True,choices=CHOICES)
    pay_type = models.CharField(max_length=45, blank=True, null=True,choices=CHOICES_PAY)
    # lat = models.CharField(max_length=45, blank=True, null=True)
    # long = models.CharField(max_length=45, blank=True, null=True)
    # is_live = models.IntegerField(blank=True, null=True)
    # show_map = models.IntegerField(blank=True, null=True)
    
    

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name_plural = "user"
        

class Settings(models.Model):
    field = models.CharField(max_length=250)
    value = models.TextField(blank=True, null=True)

    #description = models.TextField()

    @property
    def short_description(self):
        return truncatechars(self.value, 100)

    class Meta:
        managed = False
        db_table = 'settings'
        verbose_name_plural = "setting"


class Skills(models.Model):
    title = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skills'
        verbose_name_plural = "skill"

class NewSkills(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'new_skills'
        verbose_name_plural = "skill"

class Category(models.Model):
   
    title = models.CharField(max_length=255)
    title_ae = models.CharField(max_length=200, blank=True, null=True)
    title_he = models.CharField(max_length=250, blank=True, null=True)
    title_ur = models.CharField(max_length=250, blank=True, null=True)
    title_ch = models.CharField(max_length=250, blank=True, null=True)
    title_ru = models.CharField(max_length=250, blank=True, null=True)
    title_gr = models.CharField(max_length=250, blank=True, null=True)
    title_sp = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name_plural = "category"    

class UserContact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    contacted_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_contact'
        verbose_name_plural = "Contact Queries"   

class ManagePosts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    post_type = models.IntegerField()
    title = models.CharField(max_length=255)
    category = models.IntegerField()
   # othercategory = models.CharField(max_length=255)
    candidate_jobtype = models.IntegerField()
    description = models.TextField()
    #uploaded_file = models.CharField(max_length=255)
    pay_type = models.IntegerField(blank=True, null=True)
    pay_amount = models.IntegerField()
    pay_currency = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=255)
    experience = models.CharField(max_length=50)
    status = models.IntegerField()
    lang_id = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    expirydate = models.DateField()
    is_deleted = models.IntegerField(blank=True, null=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    class Meta:
        managed = False
        db_table = 'manage_posts'
        verbose_name_plural = "Job Posts"

class Emails(models.Model):
    emails_id = models.AutoField(primary_key=True)
    from_name = models.CharField(max_length=250)
    from_email = models.CharField(max_length=250)
    subject = models.TextField()
    body = models.TextField()
    email_type = models.CharField(max_length=100)
    status = models.IntegerField()

    @property
    def short_description(self):
        return truncatechars(self.body, 100)

    class Meta:
        managed = False
        db_table = 'emails' 
        verbose_name_plural = "Email Templates" 

