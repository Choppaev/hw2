from django.urls import path
from .views import sneaker_list

app_name = 'sneaker_shop'

urlpatterns = [
    path('', sneaker_list, name='sneaker_list'),
]

from .views import sneaker_detail

urlpatterns = [
    # ...
    path('<int:pk>/', sneaker_detail, name='sneaker_detail'),
]