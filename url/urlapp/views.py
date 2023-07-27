from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Url
import random, string
# Create your views here.

def home(request):
    return render(request,'urlapp/home.html')
    
def shorten(request):
	if request.method == "POST":
		#s_url : short url(slug)
		#l_url : original url
		s_url =''.join(random.choice(string.ascii_letters) for x in range(4))
		l_url = request.POST["url"]
		url = Url(url=l_url, slug=s_url)
		url.save()
		messages.info(request,'New URL is created you can check it on view urls')
		return redirect('/')     

def created(request):
	url = Url.objects.all()
	return render(request,'urlapp/url.html',{'url':url})
