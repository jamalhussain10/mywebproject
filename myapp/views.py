from django.shortcuts import render, HttpResponse

def index(request):
	return render(request,'index.html')


def add(request):
	return render(request,'add.html')