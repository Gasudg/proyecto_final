# mensajeria/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Comentario
from .forms import ComentarioForm
from paginas.models import Pagina

@login_required
def agregar_comentario(request, pagina_id):
    pagina = get_object_or_404(Pagina, id=pagina_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.pagina = pagina
            comentario.autor = request.user
            comentario.save()
            return redirect('pagina_detalle', pk=pagina.id)
    else:
        form = ComentarioForm()
    
    return render(request, 'mensajeria/agregar_comentario.html', {'form': form, 'pagina': pagina})
