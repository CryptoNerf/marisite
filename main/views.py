from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def buypage(request):
    context = {
        'title': 'Home',
        'content': 'АЛФВДЫОЖФЫО',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True
    }


    return render(request, 'main/buypage.html', context)


def about(request):
    return HttpResponse('About page')
