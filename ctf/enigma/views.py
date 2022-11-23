from django.shortcuts import render


def enigma(request):
    return render(request, 'enigma/enigma.html', {})

# Create your views here.
