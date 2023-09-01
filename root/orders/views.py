from django.shortcuts import render, redirect
from .models import Application






def index(request):
    transit_data = dict()
    transit_data['title'] = 'Додати заявку'
    # all_application = Application.objects.all()
    if request.method == 'POST':
        filled_form = ApplicationForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('orders/index.html')


    return render(request, 'orders/index.html', {
        'title': 'Заявка',
        'page': 'index',
        'app': 'orders'
    })

