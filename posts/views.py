from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from .models import Post
# Create your views here.

def hello(r):
    return HttpResponse('<h1>Hello world!</h1>')


def name(r):
    name = 'Islam'
    return HttpResponse(f'Hello {name}!')

def time(r):
    dt = datetime.now()
    return HttpResponse(f'NOW: {dt.strftime("%d/%m/%Y, %H:%M:%S")}')

def joke(r):
    return HttpResponse("""
        <div style="text-align: center; margin-top: 100px;">
            <h1 style="font-size: 60px;">404</h1>
            <p style="font-size: 30px;">Not Found ;(</p>
        </div>
    """)

#HW3
def posts(r):
    posts = Post.objects.all()

    result = ""

    for post in posts:
        result += f"""
        <h2>{post.title}</h2>
        <p>{post.description}</p>
        <p>Активен: {post.is_active}</p>
        <hr>
        """

    return HttpResponse(result)
