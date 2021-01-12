import json

from django.contrib import messages
from django.shortcuts import render, HttpResponse

from steam import steam_api, search_sort_utils, utils


# Create your views here.
def index(request, reverse=False, key='appid'):
    return render(request, 'index.html', {
        'reverse': reverse,
        'filter_key': key
    })


def fetch_steam_data_ajax(request, filter_key, reversed):
    print(f'Key: {filter_key}')

    apps = steam_api.fetch_all_apps_steamspy()
    # length = len(steam_api.fetch_all_apps())

    if filter_key not in steam_api.getKeys():
        print('Filterkey is none')
        filter_key = 'appid'

    sorted_apps = search_sort_utils.merge_recursive(apps, key=filter_key)
    keys = steam_api.getKeys()
    context = {
        'apps': sorted_apps,
        'reverse': reversed,
        'keys': keys,
        # 'length': length
    }

    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')


def app_details(request, appid):
    return render(request, 'details.html', {
        'appid': appid
    })


def fetch_details_ajax(request, appid):
    details = steam_api.fetch_details(appid)
    details_ss = steam_api.fetch_details_steamspy(appid)
    success = utils.isValidDetails(details, appid)
    if not success:
        messages.info(request, f'Game id {appid} does not have any details :(')

    print(details_ss)

    context = {
        'details': details,
        'details_ss': details_ss,
        'success': success
    }

    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')

# def search(request, input):
#     apps = steam_api.fetch_all_apps()
#     searched = search_sort_utils.binary_recursive(apps, input)
#
#     context = {
#         'app': searched
#     }
#
#     data = json.dumps(context)
#     return HttpResponse(data, content_type='application/json')

def filterTags(request):
    key = request.GET.get('key')
    reverse = request.GET.get('reverse_list')
    print(f'Reverse: {reverse}')
    return index(request, reverse=reverse, key=key)

# def reverse(request, reverse):
#     key = request.GET.get('key')
#     return index(request, )


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
