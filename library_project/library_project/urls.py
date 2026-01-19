from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', views.index),
    path('books/', views.book_list, name='book_list'),

    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('readers/', views.reader_list, name='reader_list'),
    path('readers/<int:pk>/', views.reader_detail, name='reader_detail'),
    path('readers/add/', views.reader_create, name='reader_create'),
    path('readers/<int:pk>/edit/', views.reader_update, name='reader_update'),
    path('readers/<int:pk>/delete/', views.reader_delete, name='reader_delete'),
]