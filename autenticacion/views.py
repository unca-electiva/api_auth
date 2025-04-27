from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def callback_view(request):
    code = request.GET.get('code')
    return HttpResponse(f'<h1>Código de autorización recibido: {code}</h1>')