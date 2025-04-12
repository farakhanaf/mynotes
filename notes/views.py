from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
def home(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Note.objects.create(text=text)
        return redirect('home')

    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/home.html', {'notes': notes})