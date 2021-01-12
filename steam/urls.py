from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Filter/', views.filterTags, name='filterData'),
    path('fetch_all_steam_data/<filter_key>/<reversed>', views.fetch_steam_data_ajax, name='fetch_steam_apps'),
    path('Details/<appid>', views.app_details, name='open_app_details'),
    path('fetch_app_details/<appid>', views.fetch_details_ajax, name='fetch_details'),
    # path('Reverse/<reverse>', views.reverse, name='reverse'),
    # path('search/<input>', views.search, name='search')
]