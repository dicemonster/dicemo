from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils import timezone
from player.forms import *
from player.models import * 




##### Player View Classes

# Player List
class PlayerList(ListView):
	model = Player
	context_object_name = 'players'


# Player Detail
class PlayerDetail(DetailView):
	model = Player
	context_object_name = 'player'
	

# Create New Player form
class PlayerCreate(CreateView):
	model = Player
	success_url = reverse_lazy('player-list')
	form_class	= PlayerForm
	
	def get_initial(self, *args, **kwargs):
		gamer = Gamer.objects.get(user = self.request.user)
		return {'gamer': gamer}
    
  
    
    
# Update Player form    
class PlayerUpdate(UpdateView):
	model = Player
	form_class = PlayerForm
	
class PlayerUpdateList(ListView):
        model = PlayerUpdate
        context_object_name = 'player-updates'


# Update Player form    
class PlayerAddon(UpdateView):
    model = Player
    form_class = PlayerAddonForm
    

# Delete Existing Player form
class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')
    
 

# Create New Player form
class PlayerUpdateCreate(CreateView):
        model = PlayerUpdate
        success_url = reverse_lazy('player-update-list')
        form_class      = PlayerUpdateForm

        def get_initial(self, *args, **kwargs):
                gamer = Gamer.objects.get(user = self.request.user)
                return {'gamer': gamer}




##### Campaign View Classes

class CampaignList(ListView):
	model = Campaign
	context_object_name = 'campaigns'



class CampaignDetail(DetailView):
    model = Campaign
    context_object_name = 'campaign'


# Create New Campaign form
class CampaignCreate(CreateView):
	model = Campaign
	success_url = reverse_lazy('campaign-list')
	form_class = CampaignForm
    
	def get_initial(self, *args, **kwargs):
		dm = Gamer.objects.get(user = self.request.user)
		return {'dm': dm}
    
    
# Update Campaign form    
class CampaignUpdate(UpdateView):
    model = Campaign
    form_class = CampaignForm


# Delete Existing Campaign form
class CampaignDelete(DeleteView):
    model = Campaign
    success_url = reverse_lazy('campaign-list')       
         
         
##### Item View Classes

class ItemList(ListView):
	model = Item
	context_object_name = 'items'
	
class ItemDetail(DetailView):
    model = Item
    context_object_name = 'item'


# Create New Player form
class ItemCreate(CreateView):
	model = Item
	success_url = reverse_lazy('item-list')
	form_class	= ItemForm
    
# Update Player form    
class ItemUpdate(UpdateView):
	model = Item
	form_class	= ItemForm

# Delete Existing Player form
class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('item-list')


##### Skill Category View Classes

# Skill Category List View
class SkillCategoryList(ListView):
	model = SkillCategory
	context_object_name = 'skill_cats'



# Skill Category Detail View
class SkillCategoryDetail(DetailView):
    model = SkillCategory
    context_object_name = 'skill_cat'






##### Skills View Classes

class SkillList(ListView):
	model = Skill
	context_object_name = 'skills'
	

class SkillDetail(DetailView):
    model = Skill
    context_object_name = 'skill'
    
    def get_object(self):
    	# Call the superclass
        object = super(SkillDetail, self).get_object()
        # Return the object
        return object



# Create New Skill form
class SkillCreate(CreateView):
	model = Skill
	success_url = reverse_lazy('skill-list')
	form_class	= SkillForm

    
# Edit Skill form    
class SkillUpdate(UpdateView):
    model = Skill
    form_class = SkillForm



# Delete Existing Player form
class SkillDelete(DeleteView):
    model = Skill
    success_url = reverse_lazy('skill-list')  


##### Gift View Classes

class GiftList(ListView):
	model = Gift
	context_object_name = 'gifts'

class GiftDetail(DetailView):
    model = Gift
    context_object_name = 'gift'


# Create New Gift form
class GiftCreate(CreateView):
	model = Gift
	success_url = reverse_lazy('gift-list')
    

    
# Edit Gift form    
class GiftUpdate(UpdateView):
    model = Gift



# Delete Existing Player form
class GiftDelete(DeleteView):
    model = Gift
    success_url = reverse_lazy('gift-list')



##### Fault View Classes
class FaultList(ListView):
    model = Fault
    context_object_name = 'faults'

class FaultDetail(DetailView):
    model = Fault
    context_object_name = 'fault'


# Create New Fault form
class FaultCreate(CreateView):
	model = Fault
	success_url = reverse_lazy('fault-list')
    

    
# Edit Gift form    
class FaultUpdate(UpdateView):
    model = Fault



# Delete Existing Player form
class FaultDelete(DeleteView):
    model = Fault
    success_url = reverse_lazy('fault-list')
