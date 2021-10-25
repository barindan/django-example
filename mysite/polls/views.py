from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello my first django app. You are at the polls index')
