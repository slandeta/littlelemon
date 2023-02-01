from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('about/', include('restaurant.urls')),
    path('book/', include('restaurant.urls')),
    path('menu/', include('restaurant.urls')),
    path('menu_item/', include('restaurant.urls')),
]