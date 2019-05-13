"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from todo.views import todoView, addTodoView, removeTodoView, homeView, get_data
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homeView),
    path('todo/', todoView),
    path('todo/<int:par_id>', todoView),
    path('addTodo/', addTodoView),
    path('removeTodo/<int:todo_id>', removeTodoView),
    url(r'^getData/', get_data),
    url(r'^.*', TemplateView.as_view(template_name="home.html"), name="homes"),

]
