from django.shortcuts import render

def index(request):
	context = {
	 	'title':'Dashboard',
	 	'heading':'Dashboard',
	 	
	}
	return render(request,'index.html',context)