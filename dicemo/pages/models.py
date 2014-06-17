from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

# Create your models here.

SECTION_CHOICES = (
        ('1', 'Main'),
        ('2', 'Carousel 1'),
        ('3', 'Carousel 2'),
        ('4', 'Carousel 3'),
        ('5', 'Carousel 4'),
	('6', 'Footer'),
	('7', 'Column 1'),
	('8', 'Column 2'),
	('9', 'Column 3'),
	('0', 'Unassigned'),
)


class HomePage(models.Model):
    hero_copy_section	= models.CharField(unique=True, max_length=1, choices=SECTION_CHOICES)
    hero_copy_title	= models.CharField(max_length=100)
    hero_copy		= models.TextField()
    hero_img		= FilerImageField(null=True, blank=True, help_text='Upload content image')

    def __unicode__(self):
        return self.hero_copy_title
