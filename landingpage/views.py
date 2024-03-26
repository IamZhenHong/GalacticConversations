from django.shortcuts import render

# Create your views here.
def CharacterSelection(request):
    return render(request, 'CharacterSelection.html')
