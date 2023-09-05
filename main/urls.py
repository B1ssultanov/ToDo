"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import MainView, CompleteView, DeleteView, EditView, TaskDetailView, AddTaskView

urlpatterns = [
    path('',                                   MainView.as_view()),
    path('complete/<int:task_id>',             CompleteView.as_view()),
    path('remove_task/<int:task_id>',          DeleteView.delete_task),
    path('remove_finished_task/<int:task_id>', DeleteView.delete_finished_task),
    path('edit_task/<int:task_id>',            EditView.as_view()),
    path('task_details/<int:task_id>',         TaskDetailView.as_view()),
    path('add_task',                           AddTaskView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

