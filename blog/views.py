from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':'Documents',
		'heading':'Documents',
		
	}
	return render(request, 'blog/index.html',context)