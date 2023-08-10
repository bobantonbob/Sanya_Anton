from django.shortcuts import render


def index(request):
    return render(request, 'orders/index.html', {
        'title': 'Заявка',
        'page': 'index',
        'app': 'orders'
    })