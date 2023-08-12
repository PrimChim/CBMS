from django.shortcuts import render
import requests

app_name = 'adddelete'
def add(request):
    if request.method == 'POST':
        url = 'https://cbapi.ird.gov.np/api/bill'
        data = request.POST.dict()
        if 'csrfmiddlewaretoken' in data:
            del data['csrfmiddlewaretoken']
        print(data)
        # response = requests.post(url, data=data)
    return render(request,'adddelete/index.html')