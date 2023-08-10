from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html', {
        'title': 'Галерея',
        'page': 'index',
        'app': 'catalog'
    })


def service(request):
    return render(request, 'catalog/service.html', {
        'title': 'Ціни',
        'page': 'service',
        'app': 'catalog'
    })