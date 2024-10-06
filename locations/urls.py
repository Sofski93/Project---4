from . import views
from django.urls import path


urlpatterns = [
    path('', views.LocationList.as_view(), name='home'),
    path('<slug:location_slug>/',
         views.LocationSingle.as_view(), name='location_single'),
    path('like/<slug:slug>',
         views.LocationLike.as_view(), name='location_like'),
    path('my_locations', views.MyLocations.as_view(), name='my_locations'),
    path('add_location', views.AddLocation.as_view(), name='add_location'),
    path('edit_location/<int:pk>',
         views.EditLocation.as_view(), name='edit_location'),
    path('publish_location/<int:location_id>',
         views.publish_location, name='publish_location'),
    path('delete_location/<int:location_id>',
         views.delete_location, name='delete_location'),
]