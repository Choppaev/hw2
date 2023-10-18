from django.shortcuts import render
from .models import Sneaker

def sneaker_list(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'sneaker_shop/sneaker_list.html', {'sneakers': sneakers})

from django.shortcuts import render, get_object_or_404
from .models import Sneaker

def sneaker_detail(request, pk):
    sneaker = get_object_or_404(Sneaker, pk=pk)
    return render(request, 'sneaker_shop/sneaker_detail.html', {'sneaker': sneaker})