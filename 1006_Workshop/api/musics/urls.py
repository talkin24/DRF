from django.urls import path
from . import views 


urlpatterns = [
    path('artists/', views.artist_list_create),
    path('artists/<artist_pk>/', views.artist_detail),
    path('artists/<artist_pk>/music/', views.artist_music_create),

    path('music/', views.music_list),
    path('music/<music_pk>', views.music_detail_update_delete),
]
