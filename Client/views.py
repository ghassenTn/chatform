from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate , login
from django.urls import reverse
def register(request):
    if request.method =='POST':
        try:
           nblogged1 = 1
           name1 = request.POST.get('name')
           email1 = request.POST.get('email')
           age1 = request.POST.get('age')
           user=User(
           name=name1,
           email=email1,
           age=age1,

           )
           user.save()
           txt  = {f'message':f'{name1} add avec succes'}
           return render(request,'mainpage/register.html',txt)
        except Exception as ex:
            if name1=='' or email1=='' or age1=='':
                txt = {'message':'please fill all champs'}
                return render(request,'mainpage/register.html',txt)
            txt = {'message': f' username {name1} deja existe'}
            return  render(request,'mainpage/register.html',txt)
    return render(request,'mainpage/register.html')


def login(request):
    if request.method =='POST':
        name1 =request.POST.get('name')
        age1  = request.POST.get('age')
        trueage = str(rech(name1))
        user = User.objects.get(name=name1)
        currentnblogged = user.getnblogged()
        if trueage ==age1:
            user = User.objects.get(name=name1)
            user.setnblogged()
            user.save()
            data = User.objects.all()

            return redirect('espace',name=name1)
        elif trueage == 'False':
            content = {'message': f'this user {name1} is not existe .'}
            return render(request,'mainpage/login.html',content)
        else:
            content = {'message': 'Password incorrect .'}
            return render(request, 'mainpage/login.html', content)
    return render(request,'mainpage/login.html')
def espace(request,name):
    name1 = name
    try:
        user = User.objects.get(name=name)
        if name1 != user.name:
           return redirect('login')
        context = {'name': name }
        return render(request, 'mainpage/espaceclient.html', context)
    except:
        return redirect('login')

def post(request,name):
    try:
        if request.method == "POST":
            pub = request.POST.get('pub')
            user = User.objects.get(name=name)
            if pub != '':
                posts = Post(
                    content=pub,
                    user=user
                )
                posts.save()
                data = Post.objects.all()
                context = {'name': name, 'message': 'post success', 'data': data, 'user': user}
                return render(request, 'mainpage/post.html', context)
            else:
                return redirect('post')
        try:
            user = User.objects.get(name=name)
            data = Post.objects.all()
            context = {'name': name, 'message': 'post success', 'data': data, 'user': user}

        except:
            redirect('login')
        user = User.objects.get(name=name)
        data = Post.objects.all()
        context = {'name': name, 'message': 'post success', 'data': data, 'user': user}
        return render(request, 'mainpage/post.html', context)
    except:
        return redirect('login')

# Create your views here.
def publier(request,name):
    context  = {'name1':name}
    return render(request,'mainpage/post.html',context)
def rech(keyword):
    users =User.objects.all()
    for user in users:
        if user.name==keyword:
            return user.age
    return False