from django.urls import path
from .views import TodoList, TodoCreate, TodoSearch, TodoDetail, TodoUpdate, TodoDelete



app_name = 'todo'

urlpatterns = [

    path('', TodoList.as_view(), name='todo_list'),
    path('create/', TodoCreate.as_view(), name='todo_create'),
    path('search/', TodoSearch.as_view(), name='todo_search'),
    path('<slug:slug>/<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
    path('<slug:slug>/<int:id>/update/', TodoUpdate.as_view(), name='todo_update'),
    path('<slug:slug>/<int:pk>/delete/', TodoDelete.as_view(), name='todo_delete'),
    
]
