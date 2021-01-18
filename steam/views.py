import json, pickle

from django.contrib import messages
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from steam import steam_api, search_sort_utils, utils, bst


# Redirects to the index.html page
def index(request, reverse=False, key='appid', checked_button='binary'):
    # render index page with the necessary values
    return render(request, 'index.html', {
        'reverse': reverse,
        'filter_key': key,
        'checked_button': checked_button
    })

# This is an async task in which the api's will be called
def fetch_steam_data_ajax(request, filter_key, sort_type, reversed):
    print(f'Key: {filter_key}')

    # Gather apps from API
    apps = steam_api.fetch_all_apps_steamspy()

    # sets the filter_key if none is set (usually on first load)
    if filter_key not in steam_api.getKeys():
        print('Filterkey is none')
        filter_key = 'appid'

    # Check which sort type is selected on the main screen
    if sort_type == 'merge':
        sorted_apps = search_sort_utils.merge_recursive(apps, key=filter_key)
    elif sort_type == 'insertion':
        sorted_apps = search_sort_utils.insertionsort(apps, key=filter_key)
    else:
        tree = bst.createbst(apps, filter_key)
        sorted_apps = tree.collapse()

    # Gets the owners dictionary (to know in which percentage the game is)
    # This data will be used in the index.html Javascript
    owners_apps = steam_api.get_data(sorted_apps, 'owners', force_int=False)
    owners_scaled, frac_labels = utils.get_scaled_data(owners_apps)

    # Get all the keys in which you can filter on
    keys = steam_api.getKeys()

    # group all the values
    context = {
        'apps': sorted_apps,
        'reverse': reversed,
        'keys': keys,
        'fraction_labels': frac_labels
    }

    # create json data and send that to the index.html. This will be retrieved in the JS - Ajax portion
    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')

# Render the details page
def app_details(request, appid):
    return render(request, 'details.html', {
        'appid': appid
    })

# Async call in which the details of a page are retrieved
def fetch_details_ajax(request, appid):

    # gatehr details from api. Both Steam and SteamSpy API's are used
    details = steam_api.fetch_details(appid)
    details_ss = steam_api.fetch_details_steamspy(appid)

    # check if the details returned are actually completen. The key 'success' will be False if this is the case
    success = utils.isValidDetails(details, appid)
    if not success:
        messages.info(request, f'Game id {appid} does not have any details :(')

    # group together
    context = {
        'details': details,
        'details_ss': details_ss,
        'success': success
    }

    # Create json and then to the details page
    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')

# Logic that runs when you filter on the index page
def filterTags(request):
    # get the key (which you want to filter on) from the page with the GET method
    key = request.GET.get('key')
    # Get reverse value (true of false)
    reverse = request.GET.get('reverse_list')
    # Get the sorting style from the index page
    radio_sort = request.GET.get('radio_sort')
    # render index page with the new values
    return index(request, reverse=reverse, key=key, checked_button=radio_sort)

# Load stats template
def stats(request):
    return render(request, 'stats.html', {})

# Async task that runs when generating the bar graph
def populate_prices(request):
    # init
    labels = []
    data = []

    # Gather all apps from API's and sort them
    sorted_apps = search_sort_utils.merge_recursive(steam_api.fetch_all_apps_steamspy(), key='appid')
    # Get prices from the apps since we are showing the prices in the graphs
    prices = steam_api.get_data(sorted_apps, 'price')
    prices_scaled, frac_labels = utils.get_scaled_data(prices)

    # add the prices (in dollars. They are retrieved from the API in cents)
    for k, v in prices_scaled.items():
        labels.append('${:.2f}'.format(float(k) / 100))
        data.append(v)

    # return values in JSON to the stats html
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

# Async task that runs when generating the ownerd pychart
def games_sequence(request):
    # init
    labels = []
    data = []
    # Gather all apps from API's and sort them
    sorted_apps = search_sort_utils.merge_recursive(steam_api.fetch_all_apps_steamspy(), key='appid')
    # get all appids and amount of games
    appids = steam_api.get_data(sorted_apps, 'appid')
    appidsScaled, frac_labels = utils.get_scaled_data(appids)

    # fill lists with values
    for k, v in appidsScaled.items():
        labels.append(k)
        data.append(k)

    # return to charts
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def populate_owners(request):
    labels = []
    data = []
    sorted_apps = search_sort_utils.merge_recursive(steam_api.fetch_all_apps_steamspy(), key='appid')
    owners = steam_api.get_data(sorted_apps, 'owners', force_int=False)
    owners_scaled, frac_labels = utils.get_scaled_data(owners)



    for k, v in owners_scaled.items():
        labels.append(k)
        data.append(v)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def boxplot_stats(request, type):
    # get all apps and sort them
    sorted_apps = search_sort_utils.merge_recursive(steam_api.fetch_all_apps_steamspy(), key='appid')

    # gather all the stats from the function
    stats_all = search_sort_utils.stats(sorted_apps, type, force_int=True)

    return JsonResponse(data={
        'stats': stats_all,
        'chart_type': type
    })

# def fetch_binary_search_tree(request, filter_key, reversed):
#
#     # gather all apps
#     apps = steam_api.fetch_all_apps_steamspy()
#     # retrieve tree from all apps
#     tree = bst.createbst(apps, filter_key)
#     # collapse the tree into a list with all nodes (apps)
#     result = tree.collapse()
#
#     # group all values together
#     context = {
#         'apps': result,
#         'keys': {
#             'appid',
#             'name'
#         },
#         'filter_key': filter_key,
#         'reversed': reversed,
#
#     }
#     # generate JSON and return
#     data = json.dumps(context, default=serialize_sets)
#     return HttpResponse(data, content_type='application/json')
#
# # This is used to serialize the json. Otherwise it will cause an exception
# def serialize_sets(obj):
#     if isinstance(obj, set):
#         return list(obj)
#
#     return obj
