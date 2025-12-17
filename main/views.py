from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from .models import Task, Category
from .forms import TaskForm, CustomUserCreationForm

def tasks_list(request):
    """Список задач с фильтрацией, поиском и пагинацией"""
    # Показываем только задачи текущего пользователя
    if request.user.is_authenticated:
        tasks = Task.objects.filter(executor=request.user)
    else:
        tasks = Task.objects.none()

    # Фильтрация по категории
    category = request.GET.get('category')
    if category:
        tasks = tasks.filter(category__id=category)

    # Фильтрация по статусу
    status = request.GET.get('status')
    if status == 'done':
        tasks = tasks.filter(is_done=True)
    elif status == 'not_done':
        tasks = tasks.filter(is_done=False)

    # Поиск по названию
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)

    # Пагинация
    paginator = Paginator(tasks, 5)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)

    return render(request, "tasks_list.html", {
        "tasks": tasks,
        "categories": Category.objects.all()
    })

@login_required
def task_create(request):
    """Создание новой задачи"""
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
    """Редактирование задачи"""
    task = get_object_or_404(Task, pk=pk)

    # Проверяем, что пользователь редактирует только свою задачу
    if task.executor != request.user:
        return HttpResponseForbidden("Вы не можете редактировать чужую задачу")

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
    """Удаление задачи"""
    task = get_object_or_404(Task, pk=pk)

    # Проверяем, что пользователь удаляет только свою задачу
    if task.executor != request.user:
        return HttpResponseForbidden("Вы не можете удалить чужую задачу")

    if request.method == "POST":
        task.delete()
        return redirect('tasks_list')
    return render(request, "task_confirm_delete.html", {"task": task})

def custom_logout(request):
    """Выход из системы с перенаправлением на страницу входа"""
    logout(request)
    return redirect('login')

def register(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})