from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Filter/', views.filterTags, name='filterData'),
    path('fetch_all_steam_data/<filter_key>/<sort_type>/<reversed>', views.fetch_steam_data_ajax, name='fetch_steam_apps'),
    path('Details/<appid>', views.app_details, name='open_app_details'),
    path('fetch_app_details/<appid>', views.fetch_details_ajax, name='fetch_details'),
    path('Stats/', views.stats, name='stats'),
    path('Stats/Populate_prices', views.populate_prices, name='populate_prices'),
    path('Stats/Games_sequence', views.games_sequence, name='games_sequence'),
    path('Stats/Populate_owners', views.populate_owners, name='populate_owners'),
    path('Stats/Boxplot/<type>', views.boxplot_stats, name='boxplot_stats'),
    path('Top-100/', views.top100, name='top100'),
    path('Top-100/Fetch', views.fetch_top100, name='fetch_top100')
]