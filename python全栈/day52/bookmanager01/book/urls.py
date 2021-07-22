from django.urls import path
from book.views import delete, add, update

urlpatterns = [
    path('add.html', add),
    path('update.html', update),
    path('delete.html', delete),
]