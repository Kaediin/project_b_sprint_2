from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch_all_steam_data', views.fetch_steam_data_ajax, name='fetch_steam_apps'),
    path('Details/<appid>', views.app_details, name='open_app_details'),
    path('fetch_app_details/<appid>', views.fetch_details_ajax, name='fetch_details'),
    path('Reverse/<reverse>', views.index, name='reverse'),
    path('search/<input>', views.search, name='search')
]