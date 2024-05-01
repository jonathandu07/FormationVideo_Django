from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index (request):
    context = {
        "numberNews": 15,
        "UserList": ["user1", "user2", "user3", "user4", "user5",]
        }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))