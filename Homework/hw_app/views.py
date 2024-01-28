import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Client, Order, Items
from .forms import EditItemsForm, ClientForm, OrderForm



# Create your views here.

def index(request):
    return render(request, 'hw_app/index.html')
def get_all_orders(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client).all()
    context = {
        'client': client,
        'orders': orders
    }
    return render(request, 'hw_app/get_orders.html', context=context)

def get_items(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client).all()
    date = datetime.datetime.now()
    year = date - datetime.timedelta(days=365)
    year_items = set()
    month = date - datetime.timedelta(days=30)
    month_items = set()
    week = date - datetime.timedelta(weeks=1)
    week_items = set()
    for order in orders:
        if order.date >= year:
            for item in order.items.all():
                year_items.add(item)
        elif order.date >= month:
            for item in order.items.all():
                month_items.add(item)
        elif order.date >= week:
            for item in order.items.all():
                week_items.add(item)

    context = {
        'client': client,
        'year': list(year_items),
        'month': list(month_items),
        'week': list(week_items),

    }

    return render(request, 'hw_app/get_items.html', context)

def editItem(request):
    if request.method == 'POST':
        form = EditItemsForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = request.FILES['image']

            item = Items.objects.get(pk=item.pk)
            if item:
                item.title = title
                item.description = description
                item.price = price
                item.quantity = quantity
                item.picture.save(image.name, image)
                item.save()
        else:
            form = EditItemsForm()
    return render(request, 'hw_app/editform.html', {form: form})
