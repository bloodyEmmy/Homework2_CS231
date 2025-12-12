from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Task, Category
from .forms import TaskForm


def index(request):
    return HttpResponse("Привет, это мой первый Django-проект")


def tasks_list(request):
    tasks = Task.objects.all()
    category = request.GET.get('category')
    status = request.GET.get('status')
    if category:
        tasks = tasks.filter(category__id=category)
    if status == 'done':
        tasks = tasks.filter(is_done=True)
    elif status == 'not_done':
        tasks = tasks.filter(is_done=False)
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)
    paginator = Paginator(tasks, 5)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    return render(request, "tasks_list.html", {
        "tasks": tasks,
        "categories": Category.objects.all()
    })


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.executor = request.user
            task.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, "task_form.html", {"form": form})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm(instance=task)
    return render(request, "task_form.html", {"form": form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('tasks_list')
    return render(request, "task_confirm_delete.html", {"task": task})

# Create your views here.
