from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Events, name='Events'),
    path('events/', views.Events, name='Events'),
    path('event/<int:event_id>',views.detailEvent,name='detailEvent'),
    path('createEvent/', views.createEvent, name='createEvent'),
    path('createPost/', views.createPost, name='createPost'),
    path('profile/', views.Profile, name='Profile'),
    path('edit_profile/', views.EditProfile, name='EditProfile'),
    path('my_content/', views.myContent, name ='myContent'),
    path('search/', views.SearchResult, name='SearchResult'),
    path('friends/', views.FriendsList, name='FriendsList'),
    path('profileview/<username>', views.get_user_profile),
    path('event_edit/<id>', views.EditEvent),
    path('add_friend/<username>', views.AddFriend),
    path('privacy/', views.Privacy),
     path('about_us/', views.AboutUs),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('friendship/', include('friendship.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)