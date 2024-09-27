from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_page'},
        {'title': 'Leave Feedback', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        ]

data_db = [
            {'id': 1, 'title': 'Анджелина Джоли', 'content': """<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.\
            Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».""",
            'is_published': True}, 
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False}, 
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True}, ]
    

# Create your views here.
def index(request): # HttpRequest
    data = {"title": "Main page",
            "menu": menu,
            "posts": data_db, 
            }
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {"title": "About this site", "menu": menu,})

def show_post(request, post_id):
    return HttpResponse(f"Showing post with id={post_id}")

def addpage(request):
    return HttpResponse(f"Add post")
    
def contact(request):
    return HttpResponse(f"Contact us")

def login(request):
    return HttpResponse(f"Login to the system")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
