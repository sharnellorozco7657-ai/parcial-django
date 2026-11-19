

from django.shortcuts import render, redirect
from .forms import ProgramaForm


def programa_crear(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programa_crear')
    else:
        form = ProgramaForm()
    return render(request, 'myapp/programa_form.html', {'form': form})
