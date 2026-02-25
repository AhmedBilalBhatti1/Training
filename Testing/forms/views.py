from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import MyForm
from .models import MyModel


def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form submitted successfully")
    else:
        form = MyForm()
    return render(request, 'my_form.html', {'form': form})