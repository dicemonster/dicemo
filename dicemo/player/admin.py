from django.contrib import admin
from player.models import *

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ['name','gamer', 'description',]
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ['gamer','status']
	
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class PlayerAttributeAdmin(admin.ModelAdmin):
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class AttributeAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class PlayerUpdateAdmin(admin.ModelAdmin):
	list_display = ('created_date','created_by','player')
	search_fields = ['update']
	list_filter = ['created_date','created_by','player']

	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)




class SkillAdmin(admin.ModelAdmin):
	list_display = ['name','benefit','required_skill']
	search_fields = ['name','description','benefit','required_skill',]
	prepopulated_fields = {'slug': ('name',)} 
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class ItemAdmin(admin.ModelAdmin):
        list_display = ('name',)
	prepopulated_fields = {'slug': ('name',)}
        search_fields = ['name','description',]
	class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class GiftAdmin(admin.ModelAdmin):
        list_display = ('name',)
        prepopulated_fields = {'slug': ('name',)}
        search_fields = ['name','description',]
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class FaultAdmin(admin.ModelAdmin):
        list_display = ('name',)
        prepopulated_fields = {'slug': ('name',)}
        search_fields = ['name','description',]
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)


class SkillCategoryAdmin(admin.ModelAdmin):
        list_display = ('name',)
        prepopulated_fields = {'slug': ('name',)}
        search_fields = ['name','description',]
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class CampaignAdmin(admin.ModelAdmin):
        list_display = ('name',)
        prepopulated_fields = {'slug': ('name',)}
        search_fields = ['name','description',]
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class GoalAdmin(admin.ModelAdmin):
        list_display = ('name',)
        prepopulated_fields = {'slug': ('name',)}
        search_fields = ['name','description', 'status',]
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

class CampaignUpdateAdmin(admin.ModelAdmin):
        list_display = ('name','created_by','created_date')
        search_fields = ['name','body','created_by',]
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)


admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerUpdate, PlayerUpdateAdmin)
admin.site.register(PlayerAttribute,PlayerAttributeAdmin)
admin.site.register(Attribute,AttributeAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Gift, GiftAdmin)
admin.site.register(Fault, FaultAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(CampaignUpdate, CampaignUpdateAdmin)
