from django.urls import path

from Libraryapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('logread',views.log_read),
    path('ahome',views.ahome,name='ahome'),
    path('books',views.Books,name='books'),
    path('new',views.New,name='new'),
    path('addbook',views.add_book,name='addbook'),
    path('delete/<int:id>',views.delete_book,name='del'),
    path('update<int:id>',views.update_book,name='update'),

    ]