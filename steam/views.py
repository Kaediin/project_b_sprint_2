import json

from django.contrib import messages
from django.shortcuts import render, HttpResponse

from steam import steam_api, search_sort_utils, utils


# Create your views here.
def index(request, reverse=False):
    return render(request, 'index.html', {
        'reverse': reverse
    })


def fetch_steam_data_ajax(request, reverse=False):
    apps = steam_api.fetch_all_apps()
    sorted_apps = search_sort_utils.merge_recursive(apps, key='appid')
    context = {
        'apps': sorted_apps,
        'reverse': reverse
    }

    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')


def app_details(request, appid):
    return render(request, 'details.html', {
        'appid': appid
    })


def fetch_details_ajax(request, appid):
    details = steam_api.fetch_details(appid)
    success = utils.isValidDetails(details, appid)
    if not success:
        messages.info(request, f'Game id {appid} does not have any details :(')

    context = {
        'details': details,
        'success': success
    }

    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')

def search(request, input):
    apps = steam_api.fetch_all_apps()
    searched = search_sort_utils.binary_recursive(apps, input)

    context = {
        'app': searched
    }

    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')

# Handles the filter request
# def filter(request):
#     return index(request)
# Retrieve the key from the view
# key = request.GET.get('key')

# Sort the data with the key
# data = sort(jsonData, key)

# Retrieve the key index value
# value = keys.index(key)

# Render template and pass the values on onto it
# return render(request, 'index.html', {
#     'keys': keys,
#     'data': data,
#     'filter': key,
#     'option_value': value
# })


# def reverse(request, key):
#     return index(request)
# try:
# Sort the data with the key
# data = sort(jsonData, key)
# Retrieve the key index value
# value = keys.index(key)
# except:
#     data = jsonData
#     value = None


# data.reverse()

# Render template and pass the values on onto it
# return render(request, 'index.html', {
#     'keys': keys,
#     'data': data,
#     'filter': key,
#     'option_value': value
# })
