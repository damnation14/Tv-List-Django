
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='tv-home'),
    path('tvdetail/<int:id>',views.tvdetails,name='tv-details'),
    path('watched/<int:id>',views.showwatched,name='tv-watched'),
    path('watching/<int:id>',views.showwatching,name='tv-watching'),
    path('watching/del/<int:id>',views.delshow,name='tv-delete'),
    #path('/login',)
]