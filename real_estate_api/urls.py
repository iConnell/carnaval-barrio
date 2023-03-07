from django.urls import path
from . import views

urlpatterns = [
   path('', views.PropertyViews.as_view({'get': 'list', 'post': 'create'})),
   path('<int:pk>/', views.PropertyViews.as_view({'get': 'retrieve', 'patch': 'partial_update', 'put': 'update', 'delete': 'destroy'})),
   path('<int:property_id>/reviews/', views.ReviewViews.as_view({'get': 'list', 'post': 'create'})),
   path('<int:property_id>/reviews/<int:pk>/', views.ReviewViews.as_view({'get': 'retrieve'})),
]