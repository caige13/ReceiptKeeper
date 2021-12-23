from . import views
from django.urls import path
app_name = 'Job_Manager'

urlpatterns = [
    path('add/', views.create_job, name='add_job')
]