from django.urls import path

from .views import create_links, index_page

app_name = "app"

urlpatterns = [
    path('app/', create_links),
    path('', index_page)
]
