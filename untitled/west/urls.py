from django.conf.urls import include,url
#from west import views
import west

urlpatterns = [
    #url(r'^$', west.views.templay),
    #url(r'^templay', west.views.staff),
    url(r'^zzz', west.views.staff),
    url(r'^form', west.views.form),
    url(r'^investigate', west.views.investigate),
]