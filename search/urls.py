from django.urls import path 
from . import views

app_name = 'search'

urlpatterns = [
    #post views
    path('', views.thesis_list, name='thesis_list'), 
    path('tag/<slug:tag_slug>/',views.thesis_list, name='post_list_by_tag'), 
    path('<int:year>/<int:month>/<int:day>/<slug:thesis>/',
        views.thesis_detail,
        name='thesis_detail'),

]