from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=50)
    file_field = models.FileField(upload_to='files')

    def __unicode__(self):
        return u'%s' % self.name
