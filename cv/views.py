from django.shortcuts import render

# Create your views here.

def cv(request):
	return render(request, 'templates2/cv.html')