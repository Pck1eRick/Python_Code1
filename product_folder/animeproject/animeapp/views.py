from django.shortcuts import render, redirect

from .forms import AnimeForm
from . models import Anime

# Create your views here.
def index(request):
    anime=Anime.objects.all()
    context={
        'anime_list':anime
    }
    return render(request,'index.html',context)

def detail(request,anime_id):
    anime=Anime.objects.get(id=anime_id)
    return render(request,"detail.html",{'anime':anime})

def add_anime(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        anime=Anime(name=name,desc=desc,year=year,img=img)
        anime.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    anime=Anime.objects.get(id=id)
    form=AnimeForm(request.POST or None, request.FILES, instance=anime)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'anime':anime})

def delete(request,id):
    if request.method=='POST':
        anime=Anime.objects.get(id=id)
        anime.delete()
        return redirect('/')
    return render(request,'delete.html')