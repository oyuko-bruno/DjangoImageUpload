from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})