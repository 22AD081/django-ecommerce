from django.urls import path
from .views import example_views, mysecond_views, shop_views, access_views, lakme_views,maybelline_views, dazler_views, nyka_views
urlpatterns=[path('',example_views, name='example'),
             path('app1/', mysecond_views,name='app1'),
             path('shop/', shop_views,name='shop'),
             path('accessory/', access_views,name='accessory'),
             path('lakme/', lakme_views,name='lakme'),
             path('maybelline/', maybelline_views,name='maybelline'),
             path('dazler/', dazler_views,name='dazler'),
             path('nyka/', nyka_views,name='nyka'),
             ]