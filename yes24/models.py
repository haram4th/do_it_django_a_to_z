# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Yes24Bestlist(models.Model):
#     index = models.BigIntegerField(blank=True, null=True)
#     book_id = models.TextField(primary_key=True)
#     yy = models.BigIntegerField(blank=True, null=True)
#     mon = models.BigIntegerField(blank=True, null=True)
#     title_h = models.TextField(blank=True, null=True)
#     title_m = models.TextField(blank=True, null=True)
#     title_e = models.TextField(blank=True, null=True)
#     author = models.TextField(blank=True, null=True)
#     publisher = models.TextField(blank=True, null=True)
#     pub_date = models.TextField(blank=True, null=True)
#     price = models.TextField(blank=True, null=True)
#     rating = models.FloatField(blank=True, null=True)
#     page = models.TextField(blank=True, null=True)
#     weight = models.TextField(blank=True, null=True)
#     size = models.TextField(blank=True, null=True)
#     category = models.TextField(blank=True, null=True)
#     pub_book_intro = models.TextField(blank=True, null=True)
#     tags = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'yes24bestlist'

from django.db import models

class Yes24Bestlist(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    book_id = models.TextField(primary_key=True)
    yy = models.BigIntegerField(blank=True, null=True)
    mon = models.BigIntegerField(blank=True, null=True)
    title_h = models.TextField(blank=True, null=True)
    title_m = models.TextField(blank=True, null=True)
    title_e = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    pub_date = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    rating = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    page = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    pub_book_intro = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'yes24bestlist'
