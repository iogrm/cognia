from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.LoginPage.as_view(), name='home'),
    path('passport/', views.PassportPage.as_view(), name='passport'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('test/', views.test_page, name='test'),
    path('account_sttings/', views.AccountSettings.as_view(), name='account_sttings'),
    url(r'^character/$', views.SingleCharacterAPIView.as_view(), name='single_character'),
    url(r'^character/all/$', views.AllCharacterAPIView.as_view(), name='all_characters'),
    url(r'^character/search/$', views.SearchCharacterAPIView.as_view(), name='search_character'),
    url(r'^character/submit/$', views.SubmitCharacterAPIView.as_view(), name='submit_character'),
    url(r'^character/update-cover/$', views.UpdateCharacterAPIView.as_view(), name='update_character'),
    url(r'^character/delete/$', views.DeleteCharacterAPIView.as_view(), name='delete_character'),

]
