from django.shortcuts import render, redirect

# Create your views here.
from . import models, forms

def index (req):

    task = models.Task.objects.all()
    return render(req, 'task/index.html', {
        'data': task,
    })
def about (req):

    task = models.Task.objects.all()
    return render(req, 'task/about.html', {
        'data': task,
    })

def music (req):

    task = models.Task.objects.all()
    return render(req, 'task/music/music.html', {
        'data': task,
    })

def movie (req):

    task = models.Movie.objects.all()
    return render(req, 'task/movie/movie.html', {
        'data': task,
    })

def comic (req):

    task = models.Comic.objects.all()
    return render(req, 'task/comic/comic.html', {
        'data': task,
    })

def input (req):
    form_input = forms.TaskForm()

    if req.POST:
        form_input = forms.TaskForm(req.POST)

        if form_input.is_valid():
           form_input.save()

    task = models.Task.objects.all()
    return render(req, 'task/music/input.html', {
        'data': task,
        'form': form_input,
    })

def inputmovie (req):
    form_input = forms.MovieForm()

    if req.POST:
        form_input = forms.MovieForm(req.POST)

        if form_input.is_valid():
           form_input.save()
           
    task = models.Movie.objects.all()
    return render(req, 'task/movie/input_mov.html', {
        'data': task,
        'form': form_input,
    })

def inputcomic (req):
    form_input = forms.ComicForm()

    if req.POST:
        form_input = forms.ComicForm(req.POST)

        if form_input.is_valid():
           form_input.save()
           
    task = models.Comic.objects.all()
    return render(req, 'task/comic/input_comic.html', {
        'data': task,
        'form': form_input,
    })

def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/music/detail.html', {
        'data': task,
    })

def detailmovie(req, id):
    task = models.Movie.objects.filter(pk=id).first()
    return render(req, 'task/movie/detail_mov.html', {
        'data': task,
    })

def detailcomic(req, id):
    task = models.Comic.objects.filter(pk=id).first()
    return render(req, 'task/comic/detail_comic.html', {
        'data': task,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')

def deletemovie(req, id):
    models.Movie.objects.filter(pk=id).delete()
    return redirect('/')

def deletecomic(req, id):
    models.Comic.objects.filter(pk=id).delete()
    return redirect('/')

def update (req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(nama=req.POST['nama'], ukuran=req.POST['ukuran'], stok=req.POST['stok'], deskripsi=req.POST['deskripsi'], harga=req.POST['harga'])
        return redirect('/')

    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/music/update.html', {
        'data': task,
    })

def updatemovie (req, id):
    if req.POST:
        task = models.Movie.objects.filter(pk=id).update(nama=req.POST['nama'], stok=req.POST['stok'], kedaluarsa=req.POST['kedaluarsa'], deskripsi=req.POST['deskripsi'], harga=req.POST['harga'])
        return redirect('/')

    task = models.Movie.objects.filter(pk=id).first()
    return render(req, 'task/movie/update_mov.html', {
        'data': task,
    })

def updatecomic (req, id):
    if req.POST:
        task = models.Comic.objects.filter(pk=id).update(nama=req.POST['nama'], stok=req.POST['stok'], deskripsi=req.POST['deskripsi'], harga=req.POST['harga'])
        return redirect('/')

    task = models.Comic.objects.filter(pk=id).first()
    return render(req, 'task/comic/update_comic.html', {
        'data': task,
    })

