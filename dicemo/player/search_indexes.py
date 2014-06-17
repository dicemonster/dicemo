from haystack import indexes
from player.models import *


class SkillIndex(indexes.SearchIndex, indexes.Indexable):
    text 		= indexes.CharField(document=True, use_template=True)
    name 		= indexes.CharField(model_attr='name')

    def get_model(self):
        return Skill 

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text                = indexes.CharField(document=True, use_template=True)
    name                = indexes.CharField(model_attr='name')

    def get_model(self):
        return Item 

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class PlayerIndex(indexes.SearchIndex, indexes.Indexable):
    text                = indexes.CharField(document=True, use_template=True)
    name                = indexes.CharField(model_attr='name')

    def get_model(self):
        return Player

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

