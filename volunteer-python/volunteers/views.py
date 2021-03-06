from django.shortcuts import render


# Create your views here.
from volunteers.models import Topic


def index(request):
    """The home page for Learning Log"""
    return render(request, 'index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)