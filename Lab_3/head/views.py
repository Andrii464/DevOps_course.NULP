from django.shortcuts import render
from django.http import JsonResponse
from datetime import date as d


def index(request):
    return render(request=request, template_name='index.html')


def health(request):
    response = {
        'date': d.today(),
        'current_page': request.build_absolute_uri(),
        'server_info': request.META['SERVER_NAME'],
        'client_info': {
            'user_agent': request.META['HTTP_USER_AGENT'],
            'user_ip': request.META['REMOTE_ADDR'],
            'user_host': request.META['REMOTE_HOST']
        }}
    return JsonResponse(response)