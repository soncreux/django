from django.shortcuts import render


def sadeness(request):
    return render(request, 'sadeness/sadeness.html', {})
# Create your views here.
