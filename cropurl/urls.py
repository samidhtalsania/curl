from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$','curl_app.views.hello'),
    url(r'^([0-9A-Za-z]{1,10})$','curl_app.views.cropurl_redirect'),
    url(r'^generate/$','curl_app.views.generate'),
)
