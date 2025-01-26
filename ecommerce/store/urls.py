from django.urls import path
from store import views

urlpatterns = [
    path("",views.home,name='home'),
    path("men/",views.men,name='men'),
    path("women/",views.women,name='women')
    
]
