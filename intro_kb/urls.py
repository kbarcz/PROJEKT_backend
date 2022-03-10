from django.urls import path

from intro_kb import views


urlpatterns = [
    path('home/', views.hello),
]