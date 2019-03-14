from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'welcome'),
    url(r'^search/', views.search_result, name='search_result')

]