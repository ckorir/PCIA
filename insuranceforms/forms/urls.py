from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^inquiry/', views.inquiry, name='inquiry'),
    url(r'^privatemotor/', views.privatemotor, name='privatemotor'),
    url(r'^psv/', views.psv, name='psv'),
    url(r'^commercial/', views.commercial, name='commercial'),
    url(r'^fire/', views.fire, name='fire'),
    url(r'^liability/', views.liability, name='liability'),
    url(r'^marine/', views.marine, name='marine'),
    url(r'^property/', views.property1, name='property'),
]

urlpatterns += staticfiles_urlpatterns()