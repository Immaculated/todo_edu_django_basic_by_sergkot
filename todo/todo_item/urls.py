from django.urls import path
from todo_item.views import (
    item_view,
    create_view,
    edit_item_view,
    delete_item_view,
    is_done_item_view,
    ItemView,
    CreateItemView,
)

app_name = 'item'

urlpatterns = [
    path('<int:pk>', ItemView.as_view(), name='item'),
    path('create/<int:pk>', CreateItemView.as_view(), name='create'),
    path('delete/', delete_item_view, name='delete'),
    path('edit/<int:pk>', edit_item_view, name='edit'),
    path('is_done/', is_done_item_view, name='is_done'),
]
