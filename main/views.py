from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views import View

from main.forms import TaskEditForm
from main.models import List, Complete


class MainView(View):
    """Вывод Задач"""

    def get(self, request):
        tasks = List.objects.all()
        completed_tasks = Complete.objects.all()
        return render(request, 'home/home.html', {'tasks': tasks,
                                                  'completed_tasks': completed_tasks})

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
        return render(request, 'task/task_add.html', {'form': form})

    def post(self, request):
        form = TaskEditForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('/')
        else:
            raise ValidationError
