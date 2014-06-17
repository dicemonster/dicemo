from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.core.urlresolvers import reverse, reverse_lazy
from gamer.models import Gamer 



class Player(models.Model):

    CHARACTER_TYPE = (('A', 'Player Character'),('B', 'NPC (private)'),('C','NPC (public)'),)
    CHARACTER_STATUS = (('A', 'Active'),('B', 'Retired'),('C','Dead'),('D','Frozen in carbonite'))
    LEVEL_CHOICES = (('A', 'Terrible'),('B', 'Poor'),('C', 'Mediocre'),('D', 'Fair'),('E', 'Good'),('F', 'Great'),('G', 'Superb'),('H', 'Legendary'),)

    name			= models.CharField(unique=True, max_length=100)
    gamer			= models.ForeignKey(Gamer)
    slug			= models.SlugField(unique=True, blank=True)
    description			= models.TextField()
    story			= models.TextField(blank=True)
    img				= models.ImageField(null=True, blank=True, help_text='Upload player image',upload_to='p_images/%Y/%m/%d/')
    dmg_capacty			= models.CharField(max_length=1, choices=LEVEL_CHOICES, default='A') 
    skills			= models.ManyToManyField('Skill',blank=True)
    gifts			= models.ManyToManyField('Gift',blank=True)
    faults			= models.ManyToManyField('Fault',blank=True)
    items			= models.ManyToManyField('Item', blank=True)
    fudge_points		= models.IntegerField(default=0)
    money			= models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    status			= models.CharField(max_length=1, choices=CHARACTER_STATUS, default='A')
    charactertype		= models.CharField(max_length=1, choices=CHARACTER_TYPE, default='A')	

    @permalink
    def get_absolute_url(self):
        return ("player-detail", [self.slug,])
        
    def save(self, **kwargs):
    	slug_str = self.name 
    	self.slug = slugify(slug_str) 
    	super(Player, self).save()

    def __unicode__(self):
        return '%s' % self.name



class Attribute(models.Model):
    name                = models.CharField(unique=True, max_length=100)                                                                        
    slug                = models.SlugField(unique=True, max_length=100, blank=True)                                                            
    description         = models.TextField()                                                                                                   
    img                 = models.ImageField(null=True, blank=True, help_text='Upload atr image',upload_to='s_images/%Y/%m/%d/')              

    def __unicode__(self):                                                                                                                     
        return '%s' % self.name                                                                                                                

    def save(self, **kwargs):                                                                                                                  
        slug_str = self.name                                                                                                                   
        self.slug = slugify(slug_str)                                                                                                          
        super(Attribute, self).save()                                                                                                              

    @permalink                                                                                                                                 
    def get_absolute_url(self):                                                                                                                
        return ("attribute-detail", [self.slug,])    



class PlayerAttribute(models.Model):                                                                                                                  
    LEVEL_CHOICES       = (('A', 'Terrible'),('B', 'Poor'),('C', 'Mediocre'),('D', 'Fair'),('E', 'Good'),('F', 'Great'),('G', 'Superb'),('H', 'Legendary'),)         
    player_id		= models.ForeignKey(Player)
    attr_name		= models.ForeignKey(Attribute)                                                                                                
    level               = models.CharField(max_length=1, choices=LEVEL_CHOICES, default='A') 

    def __unicode__(self):
        return self.attr_name


class PlayerUpdate(models.Model):

    UPDATE_TYPE = (('A', 'DM'),('B', 'Character Only'),('C', 'Public'))

    update              = models.CharField(max_length=140)
    update_type		= models.CharField(max_length=1, choices=UPDATE_TYPE, default='A')
    created_by          = models.ForeignKey(Gamer)
    created_date        = models.DateTimeField(auto_now_add=True)
    player            	= models.ForeignKey(Player)

    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return '%s' % self.update



class Skill(models.Model):
    name		= models.CharField(unique=True, max_length=100)
    slug		= models.SlugField(unique=True, max_length=100, blank=True)
    required_skill	= models.ForeignKey('self', blank=True, null=True, help_text="You must have this parent skill before you can take this one.")
    description		= models.TextField()
    benefit		= models.TextField()
    skill_cat		= models.ForeignKey('SkillCategory')
    img			= models.ImageField(null=True, blank=True, help_text='Upload skill image',upload_to='s_images/%Y/%m/%d/')

    def __unicode__(self):
        return '%s' % self.name

    def save(self, **kwargs):
    	slug_str = self.name 
    	self.slug = slugify(slug_str) 
    	super(Skill, self).save()

    @permalink
    def get_absolute_url(self):
        return ("skill-detail", [self.slug,])


class SkillCategory(models.Model):
    name                = models.CharField(unique=True, max_length=100)
    slug                = models.SlugField(unique=True, max_length=100, blank=True)
    description         = models.TextField()
    img                 = models.ImageField(blank=True, help_text='Upload skill category image',upload_to='sc_images/%Y/%m/%d/')

    def __unicode__(self):
        return '%s' % self.name
 
    def save(self, **kwargs):
    	slug_str = self.name 
    	self.slug = slugify(slug_str)  
    	super(SkillCategory, self).save()
 
 
 
class Gift(models.Model):                                                                                                                   
    name                = models.CharField(unique=True, max_length=100)                                                                     
    slug                = models.SlugField(unique=True, blank=True)                                                                                     
    required_gift		= models.ForeignKey('self', blank=True, null=True, help_text="You must have this parent gift before you can take this one.")
    description         = models.TextField()                                                                                                
    benefit             = models.TextField()                                                                                                
    img                 = models.ImageField(null=True, blank=True, help_text='Upload gift image',upload_to='g_images/%Y/%m/%d/')                                                                            
                                                                                                                                            
    def __unicode__(self):                                                                                                                  
        return '%s' % self.name

    @permalink
    def get_absolute_url(self):
        return ("gift-detail", [self.slug,])
 
    def save(self, **kwargs):
    	slug_str = self.name 
    	self.slug = slugify(slug_str)
    	super(Gift, self).save()
    	
    	
    	       
class Fault(models.Model):                                                                                                                   
	name                = models.CharField(unique=True, max_length=100)                                                                     
	slug                = models.SlugField(unique=True, blank=True)                                                                                     
	description         = models.TextField()                                                                                                
	benefit             = models.TextField()                                                                                                
	img                 = models.ImageField(null=True, blank=True, help_text='Upload fault image',upload_to='f_images/%Y/%m/%d/')                                                                            
																																	
	def __unicode__(self):                                                                                                                  
		return '%s' % self.name

	def save(self, **kwargs):
		slug_str = self.name 
		self.slug = slugify(slug_str) 
		super(Fault, self).save()

	@permalink
	def get_absolute_url(self):
		return ("fault-detail", [self.slug,])



class Campaign(models.Model):
    name			= models.CharField(unique=True, max_length=100)
    slug			= models.SlugField(unique=True, blank=True)
    startdate		= models.DateTimeField(auto_now_add=True)
    dm 				= models.ForeignKey(Gamer)
    players			= models.ManyToManyField(Player, blank=True)
    description		= models.TextField(blank=True)
    campaign_img	= models.ImageField(null=True, blank=True, help_text='Upload campaign image',upload_to='cp_images/%Y/%m/%d/')

    def __unicode__(self):
        return '%s' % self.name

    def save(self, **kwargs):
    	slug_str = self.name 
    	self.slug = slugify(slug_str) 
    	super(Campaign, self).save()
        
    @permalink
    def get_absolute_url(self):
        return ("campaign-detail", [self.slug,])



class Goal(models.Model):

    CAMPAIGN_STATUS_CHOICES = (
        ('1', 'New'),
        ('2', 'Accepted'),
        ('3', 'Abandoned'),
        ('4', 'In progress...'),
        ('5', 'Pending'),
        ('6', 'Failed'),
        ('7', 'Rejected'),
        ('8', 'Completed'),)

    name			= models.CharField(unique=True, max_length=100)
    slug			= models.SlugField(unique=True, blank=True)
    status			= models.CharField(max_length=1, default='1', choices = CAMPAIGN_STATUS_CHOICES)
    description		= models.TextField()
    players			= models.ManyToManyField(Player, blank=True)
    img        		= models.ImageField(null=True, blank=True, help_text='Upload goal image',upload_to='goal_images/%Y/%m/%d/')
    campaign		= models.ForeignKey(Campaign)

    def __unicode__(self):
        return '%s' % self.name

    def save(self, **kwargs):
    	slug_str = self.name 
    	self.slug = slugify(slug_str)
    	super(Goal, self).save()

    @permalink
    def get_absolute_url(self):
        return ("goal-detail", [self.slug,])
        
        

class CampaignUpdate(models.Model):

    UPDATE_TYPE = (('A', 'DM'),('B', 'Character Only'),('C', 'Public'))

    name		= models.CharField(max_length=140)
    update_type         = models.IntegerField(max_length=1, choices=UPDATE_TYPE, default='A')
    body		= models.TextField(blank=True)
    created_by		= models.ForeignKey(Gamer)
    created_date	= models.DateTimeField(auto_now_add=True)
    campaign        	= models.ForeignKey(Campaign)
    update_file		= models.FileField(null=True, blank=True, help_text='Upload document',upload_to='campaign_files/%Y/%m/%d/')

    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return '%s' % self.update


class Item(models.Model):
    name                = models.CharField(unique=True, max_length=100)
    slug                = models.SlugField(unique=True, blank=True)
    description         = models.TextField()
    benefit             = models.TextField()
    img                 = models.ImageField(null=True, blank=True, help_text='Upload item image',upload_to='i_images/%Y/%m/%d/')
    campaigns           = models.ManyToManyField('Campaign' , blank=True)

    def __unicode__(self):                                                                                                                                                                
        return '%s' % self.name    

    def save(self, **kwargs):
    	slug_str = self.name 
    	self.slug = slugify(slug_str)
    	super(Item, self).save()

    @permalink
    def get_absolute_url(self):
        return ("item-detail", [self.slug,])
