from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from pages.views import *
from player.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^search/$', include('haystack.urls')),

    url(r'^$', 'pages.views.MainHomeCopy'),


    url(r'^players/$',login_required(PlayerList.as_view()), name='player-list'),
    url(r'^players/(?P<slug>[-_\w]+)/$', login_required(PlayerDetail.as_view()), name='player-detail'),
    url(r'^add-player/$', login_required(PlayerCreate.as_view()), name='player-add'),
    url(r'^players/(?P<slug>[-_\w]+)/addon/$', login_required(PlayerAddon.as_view()), name='player-addon'),
    url(r'^players/(?P<slug>[-_\w]+)/update/$', login_required(PlayerUpdate.as_view()), name='player-update'),
    url(r'^players/(?P<slug>[-_\w]+)/delete/$', login_required(PlayerDelete.as_view()), name='player-delete'),

    url(r'^player-updates/$',login_required(PlayerUpdateList.as_view()), name='player-update-list'),
    url(r'^add-player-update/$', login_required(PlayerUpdateCreate.as_view()), name='player-add-update'),


    url(r'^items/$', login_required(ItemList.as_view()), name = 'item-list'),
    url(r'^items/(?P<slug>[-_\w]+)/$', login_required(ItemDetail.as_view()), name='item-detail'),    
    url(r'^add-item/$', login_required(ItemCreate.as_view()), name='item-add'),
    url(r'^items/(?P<slug>[-_\w]+)/update/$', login_required(ItemUpdate.as_view()), name='item-update'),
    url(r'^items/(?P<slug>[-_\w]+)/delete/$', login_required(ItemDelete.as_view()), name='item-delete'),

    url(r'^skills/$', login_required(SkillList.as_view()), name='skill-list'),
    url(r'^skills/(?P<slug>[-_\w]+)/$', login_required(SkillDetail.as_view()), name='skill-detail'),    
    url(r'^add-skill/$', login_required(SkillCreate.as_view()), name='skill-add'),
    url(r'^skills/(?P<slug>[-_\w]+)/update/$', login_required(SkillUpdate.as_view()), name='skill-update'),
    url(r'^skills/(?P<slug>[-_\w]+)/delete/$', login_required(SkillDelete.as_view()), name='skill-delete'),
        
    url(r'^skillcats/$', login_required(SkillCategoryList.as_view())),
    url(r'^skillcats/(?P<slug>[-_\w]+)/$', login_required(SkillCategoryDetail.as_view()), name='skillcat-detail'),        
        
    url(r'^gifts/$', login_required(GiftList.as_view()), name='gift-list'),
    url(r'^gifts/(?P<slug>[-_\w]+)/$', login_required(GiftDetail.as_view()), name='gift-detail'),    
    url(r'^add-gift/$', login_required(GiftCreate.as_view()), name='gift-add'),
    url(r'^gifts/(?P<slug>[-_\w]+)/update/$', login_required(GiftUpdate.as_view()), name='gift-update'),
    url(r'^gifts/(?P<slug>[-_\w]+)/delete/$', login_required(GiftDelete.as_view()), name='gift-delete'),

    url(r'^faults/$', login_required(FaultList.as_view()), name='fault-list'),
    url(r'^faults/(?P<slug>[-_\w]+)/$', login_required(FaultDetail.as_view()), name='fault-detail'),    
    url(r'^add-fault/$', login_required(FaultCreate.as_view()), name='fault-add'),
    url(r'^faults/(?P<slug>[-_\w]+)/update/$', login_required(FaultUpdate.as_view()), name='failt-update'),
    url(r'^faults/(?P<slug>[-_\w]+)/delete/$', login_required(FaultDelete.as_view()), name='fault-delete'),

    url(r'^campaigns/$', CampaignList.as_view(), name = 'campaign-list'),
    url(r'^campaigns/(?P<slug>[-_\w]+)/$', login_required(CampaignDetail.as_view()), name='campaign-detail'),
    url(r'^add-campaign/$', login_required(CampaignCreate.as_view()), name='campaign-add'),
    url(r'^campaigns/(?P<slug>[-_\w]+)/update/$', login_required(CampaignUpdate.as_view()), name='campaign-update'),
    url(r'^campaigns/(?P<slug>[-_\w]+)/delete/$', login_required(CampaignDelete.as_view()), name='campaign-delete'),    

    url(r'^register/$', 'gamer.views.GamerRegistration'),
    url(r'^profile/$', 'gamer.views.Profile'),
    url(r'^login/$', 'gamer.views.LoginRequest'),
    url(r'^logout/$', 'gamer.views.LogoutRequest'),
    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

    url(r'^admin/', include(admin.site.urls)),
)
