from django.shortcuts import render, redirect
from .models import blog
from .forms import blogform

def blogviews(request):
    blog_form =blogform(request.POST or None)
    if request.method == 'POST':
        if blog_form.is_valid:
            simpan_data =  blog.objects.create(
               judul = blog_form.cleaned_data.get('judul'),
                penulis = blog_form.cleaned_data.get('penulis'),
                penerbit = blog_form.cleaned_data.get('penerbit'),

            )
            return redirect(' blog: blogList')
    context = {
        'form': blog_form
    }
    return render(request, 'blog.html', context)