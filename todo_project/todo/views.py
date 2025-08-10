from django.shortcuts import render, redirect
from .models import Task
from django.views.decorators.csrf import csrf_exempt

def home(request):
    tasks = Task.objects.all().order_by('-id')
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('home')
    return render(request, 'todo/home.html', {'tasks': tasks})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')
