from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'my_cars.views.home', name='home'),
    # url(r'^car_dealership/', include('car_dealership.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^car/$', 'my_cars.views.cars', name='cars'),
    url(r'^car-data/$', 'my_cars.views.get_car_data', name='car-data'),
    url(r'^car/new$', 'my_cars.views.new_car', name='new_car'),
    url(r'^car/(?P<car_id>\w+)$', 'my_cars.views.view_car', name='view_car'),
    url(r'^car/(?P<car_id>\w+)/edit$', 'my_cars.views.edit_car', name='edit_car'),
    url(r'^car/(?P<car_id>\w+)/delete$', 'my_cars.views.delete_car', name='delete_car'),


)
