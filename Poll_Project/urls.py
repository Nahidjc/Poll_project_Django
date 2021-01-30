from django.contrib import admin
from django.urls import path
from Poll_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('vote/', views.vote, name='vote'),
    path('results/', views.results, name='results'),
]
