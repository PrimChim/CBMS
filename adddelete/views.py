from django.shortcuts import render
import requests
import json

app_name = 'adddelete'

def add(request):
    if request.method == 'POST':
        url = "https://cbapi.ird.gov.np/api/bill"
        headers = {'content-type': 'application/json'}
        data = request.POST.dict()
        if 'csrfmiddlewaretoken' in data:
            del data['csrfmiddlewaretoken']
        if data['isrealtime'] == 'true' or data['isrealtime'] == 'True':
            data['isrealtime'] = True
        else:
            data['isrealtime'] = False
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.text == '100':
              return render(request, 'adddelete/index.html', {'message': 'API credentials do not match'})
        elif response.text == '101':
              return render(request, 'adddelete/index.html', {'message': 'Bill already exists'})
        elif response.text == '102':
              return render(request, 'adddelete/index.html', {'message': 'BException while saving bill details, Please check model fields and values'})
        elif response.text == '103':
              return render(request, 'adddelete/index.html', {'message': 'Unknown exceptions, Please check API URl and model fields and values'})
        elif response.text == '104':
              return render(request, 'adddelete/index.html', {'message': 'model invalid'})
        elif response.text == '200':
              return render(request, 'adddelete/index.html', {'message': 'Bill added successfully'})
    return render(request, 'adddelete/index.html')
