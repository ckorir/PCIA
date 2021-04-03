from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^inquiry/', views.inquiry, name='inquiry'),
    url(r'^privatemotor/', views.privatemotor, name='privatemotor'),
    url(r'^psv/', views.psv, name='psv'),
    url(r'^commercial/', views.commercial, name='commercial'),
]