from django.urls import include,path
from . import views
app_name = 'job'


urlpatterns = [
    path('signup',views.signup ,name='singup'),
    path('profile',views.profile,name='profile'),
    path('profile/edit',views.profile_edit,name='profile_edit'),

    
]