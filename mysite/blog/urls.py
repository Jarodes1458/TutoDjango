from django.urls import path
from . import views
#post_list  est le nom de la vue
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]