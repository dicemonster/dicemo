from django.contrib import admin
from mygallery.models import *

class GalleryAdmin(admin.ModelAdmin):
        list_display = ('name','category',)
        search_fields = ['name', 'description',]
        prepopulated_fields = {'slug': ('name',)}
	class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class GalleryImageAdmin(admin.ModelAdmin):
	list_display = ['name','posted']
	search_fields = ['name','description',]
	prepopulated_fields = {'slug': ('name',)} 
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class GalleryCategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name', 'description')
	class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(GalleryCategory, GalleryCategoryAdmin)
