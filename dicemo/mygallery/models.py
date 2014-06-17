from django.db import models
from django.db.models import permalink
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

class Gallery(models.Model):
        name		= models.CharField(max_length=100, unique=True)
        slug            = models.SlugField(max_length=100, unique=True)
        description	= models.TextField()
        category	= models.ForeignKey('GalleryCategory')
	img		= FilerImageField(null=True, blank=True) 

        def __unicode__(self):
            return '%s' % self.name


class GalleryImage(models.Model):
	name		= models.CharField(max_length=100, unique=True)
	slug		= models.SlugField(unique=True)
	description	= models.CharField(max_length=200)
	body		= models.TextField()
	gallery		= models.ForeignKey('Gallery')
	img		= FilerImageField(null=True, blank=True)
	posted		= models.DateTimeField()

	def __unicode__(self):
		return '%s' % self.name


class GalleryCategory(models.Model):
        name           	= models.CharField(max_length=100, db_index=True)
        description     = models.TextField(blank=True)
	img 		= FilerImageField(null=True, blank=True)

        def __unicode__(self):
            return '%s' % self.name

