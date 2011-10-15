from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'addressbook.contacts.controllers.home.home'),
    url(r'^signout/$', 'addressbook.contacts.controllers.home.signout'),
    url(r'^groups/$', 'addressbook.contacts.controllers.group.group'),
    url(r'^groups/delete/$', 'addressbook.contacts.controllers.group.delete'),
    url(r'^setting/$', 'addressbook.contacts.controllers.setting.account'),
    url(r'^dashboard/$', 'addressbook.contacts.controllers.contact.list'),
    url(r'^contacts/$', 'addressbook.contacts.controllers.contact.list'),
    url(r'^contacts/list/$', 'addressbook.contacts.controllers.contact.list'),
    url(r'^contacts/show/$', 'addressbook.contacts.controllers.contact.show'),
    url(r'^contacts/create/$', 'addressbook.contacts.controllers.contact.create'),
    url(r'^contacts/edit/$', 'addressbook.contacts.controllers.contact.edit'),
    url(r'^contacts/delete/$', 'addressbook.contacts.controllers.contact.delete'),
    (r'^web/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)
