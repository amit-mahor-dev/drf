"""
URL configuration for drf project.

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
from api.views import create, list, retrive, delete, partial_update,student_form_view, books

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create", create.as_view()),
    path("list", list.as_view()),
    path("ret/<int:pk>/", retrive.as_view()),
    path("delete/<int:pk>/", delete.as_view()),
    path("partial_update/<int:pk>", partial_update.as_view()),
    path("add-student/", student_form_view, name="add_student"),
    path("books", books.as_view())
]

"commit"
