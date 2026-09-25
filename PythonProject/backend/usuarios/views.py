from django.http import JsonResponse

from .models import Usuario


def listar_usuarios(request):
	usuarios = Usuario.objects.values('id', 'nome')
	return JsonResponse({'usuarios': list(usuarios)})
