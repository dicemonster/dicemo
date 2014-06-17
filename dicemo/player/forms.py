# forms.py
from django import forms
from player.models import *
from crispy_forms.helper import FormHelper


class PlayerForm(forms.ModelForm):
		
	class Meta():
		model = Player
		exclude = ['slug','items','skills','gifts','faults','attributes',]
		
		
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)
		

class PlayerUpdateForm(forms.ModelForm):

        class Meta():
                model = PlayerUpdate
                exclude = ['slug',]


        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)


class PlayerAddonForm(forms.ModelForm):
		
	class Meta():
		model = Player
		fields = ['skills','gifts','items','faults',]
		template_name = 'players/player_form.html'
		
		
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)
	
	
		
class SkillForm(forms.ModelForm):
	
	class Meta():
		model = Skill
		exclude = ['slug','startdate']
		
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class CampaignForm(forms.ModelForm):
	
	class Meta():
		model = Campaign
		exclude = ['slug','startdate']
		
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)		
		
class ItemForm(forms.ModelForm):
	
	class Meta():
		model = Item
		exclude = ['slug',]
		
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)
