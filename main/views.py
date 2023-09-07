from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views import View

from main.forms import TaskEditForm, RegistrationForm, LoginForm
from main.models import List, Complete, Users

from rest_framework import viewsets
from .serializers import ListSerializer

user_id = 0

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class MainView(View):
    """Вывод Задач"""

    def get(self, request):
        tasks = List.objects.all()
        completed_tasks = Complete.objects.all()
        return render(request, 'home/home.html', {'tasks': tasks,
                                                  'completed_tasks': completed_tasks,
                                                  'user_id': user_id})

class CompleteView(View):
    """Успешное окончание задачи"""

    def get(self, request, task_id):
        tasks = List.objects.filter(id=task_id)
        for row in tasks.values():
            Complete.objects.create(**row)
            List.objects.filter(id=task_id).delete()
        return render(request, 'home/success_finish.html')


class DeleteView(View):
    def delete_task(self, task_id):
        List.objects.filter(id=task_id).delete()
        return render(self, 'home/success_deleted.html')

    def delete_finished_task(self, task_id):
        Complete.objects.filter(id=task_id).delete()
        return render(self, 'home/success_deleted.html')


class EditView(View):
    def get(self, request, task_id):
        task = List.objects.get(id=task_id)
        form = TaskEditForm(instance=task)
        return render(request, 'task/task_update.html', {'form': form,
                                                         'task': task})

    def post(self, request, task_id):
        task = List.objects.get(id=task_id)
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect(f'/task_details/{task_id}')
        else:
            raise ValidationError


class TaskDetailView(View):
    def get(self, request, task_id):
        task = List.objects.get(id=task_id)
        return render(request, 'task/task_detail.html', {'task': task})

class AddTaskView(View):
    def get(self, request):
        form = TaskEditForm()
        form.user_id = user_id
        return render(request, 'task/task_add.html', {'form': form})

    def post(self, request):
        form = TaskEditForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('/')
        else:
            raise ValidationError


def SignUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            user_id = form.auto_id
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'home/authorization/signUp.html', {'form': form})


def SignIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = Users.objects.get(email=email)
            if user is not None:
                global user_id
                user_id = user.id
                return redirect('/')
            else:
                form.add_error(None, 'Invalid username or password')
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'home/authorization/signIn.html', {'form': form})
