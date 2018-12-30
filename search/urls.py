from django.urls import path 
from . import views

app_name = 'search'

urlpatterns = [
    #post views
    path('', views.thesis_list, name='thesis_list'), 
    path('<int:year>/<int:month>/<int:day>/<slug:thesis>/',
        views.thesis_detail,
        name='thesis_detail'),

]