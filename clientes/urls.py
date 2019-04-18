from django.urls import path
from .views import listagem, create, update, delete

urlpatterns = [
    path('list/', listagem, name='lista_pessoa'),
    path('new/', create, name="nova_pessoa"),
    path('update/<int:id>/', update, name="update_pessoa"),
    path('delete/<int:id>/', delete, name="delete_pessoa"),
]
