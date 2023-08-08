from django.urls import path
from apps import views
app_name='apps'
urlpatterns = [
    # path('index/', views.attendance_list, name='attendance_list'),
    path('index/',views.index,name='index'),
    path('',views.login,name='Login'),
    path('tabls/',views.atts,name='atts'),
    # path('atts/', views.filter_by_name, name='filter_by_name'),
]


