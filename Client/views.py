from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate , login
def register(request):
    if request.method =='POST':
        try:
           name1 = request.POST.get('name')
           email1 = request.POST.get('email')
           age1 = request.POST.get('age')
           user=User(
           name=name1,
           email=email1,
           age=age1
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
        if trueage ==age1:
            data = User.objects.all()
            context = {'data':data,'name':name1}
            return redirect('espace',name=name1)
        elif trueage == 'False':
            content = {'message': f'this user {name1} is not existe .'}
            return render(request,'mainpage/login.html',content)
        else:
            content = {'message': 'Password incorrect .'}
            return render(request, 'mainpage/login.html', content)
    return render(request,'mainpage/login.html')
def espace(request,name):
    context = {'name': name }
    return render(request, 'mainpage/espaceclient.html', context)
def post(request,name):
    if request.method=="POST":
        pub = request.POST.get('pub')
        user = User.objects.get(name=name)
        posts = Post(
            content=pub,
            user=user
        )
        posts.save()
        data = Post.objects.all()
        context = {'name': name, 'message': 'post success','data':data , 'user':user}
        return render(request, 'mainpage/post.html', context)
    user = User.objects.get(name=name)
    data = Post.objects.all()
    context = {'name': name, 'message': 'post success', 'data': data , 'user':user}
    return render(request,'mainpage/post.html',context)
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