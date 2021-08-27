
from django.contrib import admin
from django.urls import path, reverse_lazy

from . import views


#from django.views.decorators.cache import cache_page

app_name = "resumes"
# cache_page(60*15)(view)

urlpatterns = [

    #path('', cache_page(60*15, key_prefix="resume_list")(views.home), name="home"),
    path('', views.home, name="home"),

    # Resumes CRUD
    # path('list/', (views.ResumeListView.as_view()), name="resume_list"),
    path('list/', views.ResumeListView.as_view(), name="resume_list"),
    
]