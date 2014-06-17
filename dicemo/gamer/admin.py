from django.contrib import admin
from gamer.models import Gamer

class GamerAdmin(admin.ModelAdmin):
	list_display = ('name','user','img')
	search_fields = ['name','user', 'description',]
	
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)


admin.site.register(Gamer, GamerAdmin)
