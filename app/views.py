from django.shortcuts import render
from app.models import *

# Create your views here.
def insert_topic(request):
    tn = input('Enter the name:')
    TO = Topic.objects.get_or_create(topic_name =tn )
    if TO[1]:
        return HttpResponse("Topic is created successfully.......!")
    else:
        return HttpResponse("Topic is already exits .......!")
def TopWeb(request):
    LTWO = Topic.objects.prefetch_related('webpage_set').all()
    d    = {'LTWO':LTWO}
    return render(request,'TopWeb.html',d)