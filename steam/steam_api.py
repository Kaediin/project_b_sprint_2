import requests, json


def fetch_all_apps():
    url = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=264F85DF8998D2B69F9CA82C2DEF7A9B&format=json"
    response = requests.request("GET", url).json()
    apps = response['applist']['apps']
    return apps

def fetch_details(appid):
    url = f"http://store.steampowered.com/api/appdetails?appids={appid}"
    response = requests.request("GET", url).json()
    apps = response
    return apps