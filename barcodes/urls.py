from django.urls import path
from .views import generate_barcode, barcode_form

urlpatterns = [
    path('barcode/<str:code>/', generate_barcode, name='generate_barcode'),
    path('generate/', barcode_form, name='barcode_form'),
]
