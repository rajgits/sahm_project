# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class About(models.Model):
    about_id = models.AutoField(primary_key=True)
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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    id = models.IntegerField()
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


class Cms(models.Model):
    cms_id = models.AutoField(primary_key=True)
    link_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=100)
    status = models.IntegerField(blank=True, null=True)
    lang_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cms'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Emails(models.Model):
    emails_id = models.AutoField(primary_key=True)
    from_name = models.CharField(max_length=250)
    from_email = models.CharField(max_length=250)
    subject = models.TextField()
    body = models.TextField()
    email_type = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emails'


class ManagePosts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    post_type = models.IntegerField()
    title = models.CharField(max_length=255)
    category = models.IntegerField()
    othercategory = models.CharField(max_length=255)
    candidate_jobtype = models.IntegerField()
    description = models.TextField()
    uploaded_file = models.CharField(max_length=255)
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

    class Meta:
        managed = False
        db_table = 'manage_posts'


class NewSkills(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'new_skills'


class Settings(models.Model):
    field = models.CharField(max_length=250)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class Skills(models.Model):
    title = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skills'


class UserContact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    contacted_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_contact'


class Users(models.Model):
    google_id = models.TextField()
    facebook_id = models.TextField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    gender = models.IntegerField(blank=True, null=True)
    date_birth = models.CharField(max_length=100, blank=True, null=True)
    phonecodecountry = models.CharField(max_length=10)
    phonecode = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    show_phone = models.IntegerField()
    password = models.CharField(max_length=250)
    address = models.TextField()
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.CharField(max_length=100)
    profile_image_verified = models.IntegerField()
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    experience_year = models.IntegerField()
    experience_month = models.IntegerField()
    industry_id = models.IntegerField()
    summary = models.TextField()
    education = models.TextField()
    full_work_type = models.IntegerField()
    part_work_type = models.IntegerField()
    fullpart_work_type = models.IntegerField()
    freelance_work_type = models.IntegerField()
    fixed_price = models.CharField(max_length=50)
    fixed_price_currency = models.IntegerField()
    perhour_price = models.CharField(max_length=50)
    perhour_price_currency = models.IntegerField()
    phoneopt = models.CharField(max_length=50)
    phoneotpstatus = models.IntegerField()
    otpdatetime = models.DateTimeField()
    emailotp = models.CharField(max_length=50)
    emailotpstatus = models.IntegerField()
    emailotpdatetime = models.DateTimeField()
    registration_date = models.DateTimeField()
    lastupdate_date = models.DateTimeField()
    activation_status = models.IntegerField()
    status = models.IntegerField()
    work_type = models.CharField(max_length=45, blank=True, null=True)
    pay_type = models.CharField(max_length=45, blank=True, null=True)
    lat = models.CharField(max_length=45, blank=True, null=True)
    long = models.CharField(max_length=45, blank=True, null=True)
    is_live = models.IntegerField(blank=True, null=True)
    show_map = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
