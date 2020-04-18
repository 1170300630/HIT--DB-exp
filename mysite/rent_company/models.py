# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup)
#     permission = models.ForeignKey('AuthPermission')
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group_id', 'permission_id'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     content_type = models.ForeignKey('DjangoContentType')
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type_id', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254, blank=True, null=True)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser)
#     group = models.ForeignKey(AuthGroup)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user_id', 'group_id'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser)
#     permission = models.ForeignKey(AuthPermission)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user_id', 'permission_id'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
#     user = models.ForeignKey(AuthUser)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'


class Enterprise_owner (models.Model):
    Owner_id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Address = models.CharField(max_length=255, blank=True, null=True)
    Company_type = models.CharField(max_length=255, blank=True, null=True)
    Tel = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'Enterprise_owner'


class Branch_Office (models.Model):
    Branch_id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255, blank=True, null=True)
    Address = models.CharField(max_length=255, blank=True, null=True)
    Tel = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'Branch_Office'


class Staff (models.Model):
    Staff_id = models.IntegerField(primary_key=True)
    Branch = models.ForeignKey(Branch_Office)
    Title = models.CharField(max_length=255)
    Gender = models.CharField(max_length=8)
    Positions = models.CharField(max_length=255)
    Salary = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Staff'


class  Customer (models.Model):
    Customer_id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Tel = models.IntegerField()
    Rooms_no = models.IntegerField(blank=True, null=True)
    Idel_rent = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Customer'


class Private_owener (models.Model):
    Owner_id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Tel = models.IntegerField()
    Address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Private_owener'

class House_property (models.Model):
    House_property_id = models.IntegerField(primary_key=True)
    Owner = models.ForeignKey(Enterprise_owner)
    Owner = models.ForeignKey(Private_owener)
    Rooms_no = models.IntegerField(blank=True, null=True)
    Address = models.CharField(max_length=255, blank=True, null=True)
    Rent = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'House_property'


class Advertisement (models.Model):
    Advertisement_id = models.IntegerField(primary_key=True)
    House_property = models.ForeignKey(House_property)

    class Meta:
        # managed = False
        db_table = 'Advertisement'


class News (models.Model):
    Title = models.CharField(primary_key=True, max_length=255)
    Address = models.CharField(max_length=255)
    Tel = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'News'


class Ad_details (models.Model):
    Advertisement_id = models.ForeignKey(Advertisement)
    Advertisement_id = models.IntegerField(primary_key=True)
    News_Title = models.ForeignKey(News)
    News_Title = models.CharField(primary_key=True,max_length=255)
    Start_time = models.DateField(blank=True, null=True)
    End_time = models.DateField(blank=True, null=True)
    Pay = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Ad_details'
        unique_together = (('Advertisement_id', 'News_Title'),)



class Record (models.Model):
    Staff_id = models.ForeignKey(Staff)
    Staff_id = models.IntegerField(primary_key=True)
    Customer_id = models.ForeignKey(Customer)
    Customer_id = models.IntegerField(primary_key=True)
    House_property_id = models.ForeignKey(House_property)
    House_property_id = models.IntegerField(primary_key=True)
    Timing = models.DateField(primary_key=True)
    Comments = models.CharField(max_length=1023)

    class Meta:
        # managed = False
        db_table = 'Record'
        unique_together = (('Staff_id', 'Customer_id', 'House_property_id', 'Timing'),)




class  Rent_contract (models.Model):
    Contract_id = models.IntegerField(primary_key= True)
    Customer = models.ForeignKey(Customer)
    House_property = models.ForeignKey(House_property)
    Staff = models.ForeignKey(Staff)
    Start_time = models.DateField(blank=True, null=True)
    End_time = models.DateField(blank=True, null=True)
    Rent = models.FloatField(blank=True, null=True)
    Earnest_money = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Rent_contract'
        unique_together = (('Contract_id', 'Customer', 'House_property','Staff'),)
