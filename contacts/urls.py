from django.conf.urls import url
from contacts import views

app_name = 'contacts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<contact_id>[0-9]+)/$',
        views.show_contact, name='show_contact'),
    url(r'^add_contact/$', views.add_contact, name='add_contact'),
]
