from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('item/', include('todo_item.urls')),
    path('registration/', include('registration.urls')),
]
