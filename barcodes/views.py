from django.shortcuts import render, redirect
from .forms import BarcodeForm
from django.http import HttpResponse
from .models import Barcode
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files.base import ContentFile

def generate_barcode(request, code):
    # Check if the barcode already exists
    barcode_instance, created = Barcode.objects.get_or_create(code=code)

    if created or not barcode_instance.image:
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(code, writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        
        # Save the barcode image to the model
        barcode_image = ContentFile(buffer.getvalue())
        barcode_instance.image.save(f'{code}.png', barcode_image)
        barcode_instance.save()

    # Return the barcode image as response
    return HttpResponse(barcode_instance.image.open(), content_type='image/png')



def barcode_form(request):
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            return redirect('generate_barcode', code=code)
    else:
        form = BarcodeForm()
    return render(request, 'barcode_form.html', {'form': form})
