from django.shortcuts import render, get_onject_or_404
from .models import artistProfile, art

# Create your views here.
def index(request):
    all_artists = Album.objects.all()
    context = {'all_artists': all_artists}
    return render(request, 'artistProfile/index.html', context)
