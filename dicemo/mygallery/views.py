from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from mygallery.models import * 

def GalleryAll(request):
        galleries = Gallery.objects.all().order_by('name')
        context = {'galleries': galleries}
        return render_to_response('galleriesall.html', context, context_instance=RequestContext(request))

@login_required
def SpecificGallery(request):
	gallery = Gallery.objects.get(pk=1)
	context	= {'gallery', gallery }
	return render_to_response('singlegallery.html', context, context_instance=RequestContext(request))

def ImagesAll(request):
        images = GalleryImage.objects.all().order_by('name')
        context = {'images': images}
        return render_to_response('galleryimagesall.html', context, context_instance=RequestContext(request))

