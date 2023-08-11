from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('Espace-Client/<str:name>/',views.espace,name='espace'),
    path('Espace-Client/post/<str:name>/',views.post,name='post'),
    path('Espace-Client/post/done<str:name>',views.publier,name='publier'),

]