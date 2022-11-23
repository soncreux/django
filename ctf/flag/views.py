from django.shortcuts import render

def flag(request):
    return render(request, 'flag/flag.html', {})
