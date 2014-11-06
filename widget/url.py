from django.conf.urls import patterns, include, url
from widget import views

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^create/$',           views.CreateWidget),

)