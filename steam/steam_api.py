import requests, json, collections

# Get all steamSpy Apps from SteamSpy api
def fetch_all_apps_steamspy():

    url = "https://steamspy.com/api.php?request=all"
    response = requests.request("GET", url).json()
    resp = response.values()
    return list(resp)

# Get all apps from Steam API
def fetch_all_apps():
    url = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=264F85DF8998D2B69F9CA82C2DEF7A9B&format=json"
    response = requests.request("GET", url).json()
    apps = response['applist']['apps']
    return apps

# Get Details from app through SteamAPI. (appid needed ofcourse)
def fetch_details(appid):
    url = f"http://store.steampowered.com/api/appdetails?appids={appid}"
    response = requests.request("GET", url).json()
    apps = response
    return apps

# get details of app through steamspy api
def fetch_details_steamspy(appid):
    url = f"https://steamspy.com/api.php?request=appdetails&appid={appid}"
    response = requests.request("GET", url).json()
    return dict(response)

# get top 100 games
def get_top_100():
    url = 'https://steamspy.com/api.php?request=top100in2weeks'
    response = requests.request("GET", url).json()
    resp = response.values()
    return list(resp)

# return available keys to filter through
def getKeys():
    return [
        'appid',
        'name',
        'developer',
        'publisher',
        'positive',
        'negative',
        'owners',
        'price',
    ]

# get all key-values from apps. (enter specific keys). Used for stats
def get_data(apps, key, force_int=True):
    dict_values = {}

    for app in apps:
        try:
            if force_int:
                value = int(app[key])
            else:
                value = app[key]

            if value in dict_values:
                dict_values[value] += 1
            else:
                dict_values[value] = 1
        except KeyError:
            print('No value')
    return dict(sorted(dict_values.items()))

