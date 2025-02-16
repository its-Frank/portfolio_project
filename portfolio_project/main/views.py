from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def base(request):
    return render(request, 'main\\base.html')
def about(request):
    return render(request, 'main\\about.html')
def projects(request):
    return render(request, 'main\\projects.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main\\contact.html', {'form': form})
