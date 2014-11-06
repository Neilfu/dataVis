from django.conf.urls import patterns,  url
from views import getTableList

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^tableList/$',           getTableList),

)