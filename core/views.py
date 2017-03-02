from django.shortcuts import render
from .models import Message

def index(request):
	message = Message.objects.all()
	return render(request,"core/index.html",{"message":message})
	
