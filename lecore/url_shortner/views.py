from django.http import HttpResponse
from django.shortcuts import render,redirect
import uuid
from .models import Url
import socket #for our IP address

# Create your views here.
s =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IPAddress = s.getsockname()[0]

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == "POST":
        url = request.POST['link']
        url = url.replace('http://','')
        uid = str(uuid.uuid4())[:6] #creating a unique string with 6 letters
        smol_url = Url(link=url,uuid=uid)
        smol_url.save() #saving to db
        return HttpResponse(IPAddress+":8000/"+uid)
    else:
        return HttpResponse("Please try again later")

def go(request,dynvar):# dynvar is the dynamic variable we created in urls.py
    url_details = Url.objects.get(uuid=dynvar) #find the url with the uuid that was sent in dynvar var
    return redirect("https://"+url_details.link)
