from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_index, name="about_index"),
    path('FAQs/', views.faqs_index, name="faqs_index"),
    path('coming-soon/', views.coming_soon, name="coming_soon"),
]

urlpatterns += staticfiles_urlpatterns()