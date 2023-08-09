from django.urls import path

from .views import create_links, index_page, redirect_link

app_name = "app"

urlpatterns = [
    path('app/', create_links),
    path('', index_page),
    path('link/<str:short_link>', redirect_link)
]
