from django.shortcuts import render
import requests
import json

# Create your views here.

def index(request):
    #diction = {}
    user = False
    if request.method == 'POST':
        country_name = request.POST.get('country_name')
        country = country_name.upper()
        url = 'https://coronavirus-19-api.herokuapp.com/countries/' + str(country) 
        response = requests.get(url)
        user = response.json()
    #diction = {'user':user}
    return render(request, 'index.html', context={'user':user})