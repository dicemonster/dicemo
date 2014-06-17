from django.contrib import admin
from pages.models import HomePage 

class HomePageAdmin(admin.ModelAdmin):
	list_display = ['pk','hero_copy_title']
        search_fields = ['hero_copy','hero_copy_title']
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

admin.site.register(HomePage, HomePageAdmin)
