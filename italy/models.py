# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
class Regioni(models.Model):
    id =  models.BigIntegerField(primary_key=True, db_column='codice_regione_istat')
    name = models.CharField(max_length=765)
    slug = models.CharField(max_length=765)
    codice_regione_istat = models.CharField(max_length=765)
    class Meta:
        db_table = u'regioni'
    def __unicode__(self):
        return self.name
        
class Provincie(models.Model):
    id =  models.BigIntegerField(primary_key=True, db_column='codice_provincia_istat')
    name = models.TextField()
    slug = models.CharField(max_length=765)
    abbr = models.CharField(max_length=63)
    models.CharField(max_length=765, unique=True)
    codice_regione_istat = models.ForeignKey(Regioni, db_column='codice_regione_istat')
    class Meta:
        db_table = u'provincie'
    def __unicode__(self):
        return self.name

class Comuni(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id') # Field name made lowercase.
    name = models.TextField()
    slug = models.CharField(max_length=765)
    lat = models.CharField(max_length=765)
    lng = models.CharField(max_length=765)
    codice_provincia_istat = models.ForeignKey(Provincie, db_column='codice_provincia_istat')
    codice_comune_istat = models.CharField(max_length=765)
    codice_alfanumerico_istat = models.CharField(max_length=765)
    capoluogo_provincia = models.IntegerField()
    capoluogo_regione = models.IntegerField()
    class Meta:
        db_table = u'comuni'
    def __unicode__(self):
        return self.name





