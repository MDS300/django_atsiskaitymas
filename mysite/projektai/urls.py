from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projektai/', views.projektai, name='projektai'),
    path('projektai/<int:pavadinimas>', views.projektas, name='projektas'),
    path('register/', views.register, name='register'),
    path('priskirti_projektai/', views.ProjektasListView.as_view(), name='priskirti_projektai'),
]
