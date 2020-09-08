from django.shortcuts import render, redirect

# Create your views here.
from . import models, forms

def index (req):

    task = models.Task.objects.all()
    return render(req, 'task/index.html', {
        'data': task,
    })

def input (req):
    form_input = forms.TaskForm()

    if req.POST:
        form_input = forms.TaskForm(req.POST)

        if form_input.is_valid():
           form_input.save()

    task = models.Task.objects.all()
    return render(req, 'task/input.html', {
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
    return render(req, 'task/input_mov.html', {
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
    return render(req, 'task/input_comic.html', {
        'data': task,
        'form': form_input,
    })

def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/detail.html', {
        'data': task,
    })

def detailmovie(req, id):
    task = models.Movie.objects.filter(pk=id).first()
    return render(req, 'task/detail_mov.html', {
        'data': task,
    })

def detailcomic(req, id):
    task = models.Comic.objects.filter(pk=id).first()
    return render(req, 'task/detail_comic.html', {
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
        task = models.Task.objects.filter(pk=id).update(name=req.POST['name'], genre=req.POST['genre'], artis=req.POST['artis'], th=req.POST['th'], lirik=req.POST['lirik'], link=req.POST['link'])
        return redirect('/')

    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/update.html', {
        'data': task,
    })

def updatemovie (req, id):
    if req.POST:
        task = models.Movie.objects.filter(pk=id).update(title=req.POST['title'], gen=req.POST['gen'], rate=req.POST['rate'], years=req.POST['years'], des=req.POST['des'])
        return redirect('/')

    task = models.Movie.objects.filter(pk=id).first()
    return render(req, 'task/update_mov.html', {
        'data': task,
    })

def updatecomic (req, id):
    if req.POST:
        task = models.Comic.objects.filter(pk=id).update(judul=req.POST['judul'], author=req.POST['author'], status=req.POST['status'], genres=req.POST['genres'], update=req.POST['update'])
        return redirect('/')

    task = models.Comic.objects.filter(pk=id).first()
    return render(req, 'task/update_comic.html', {
        'data': task,
    })

