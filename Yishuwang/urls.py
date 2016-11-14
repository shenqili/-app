"""
Definition of urls for Yishuwang.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^register$', app.views.register, name='register'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload_book/(?P<book_grade>\d)/(?P<book_major>.*)',app.views.upload_book),
    url(r'^upload_book_choice$',app.views.upload_book_choice),
    url(r'^user_book_detail$',app.views.user_book_detail),
    url(r'^delete_book/(?P<book_id>\d+)',app.views.delete_book),
    url(r'^personal_inf/(?P<c_user>\w+)$',app.views.personal_inf, name='personalinf'),
    url(r'^public_inf/(?P<c_user>\w+)$',app.views.public_inf, name='publicinf'),
    
    url(r'^login/accounts/password/reset/', django.contrib.auth.views.password_reset, { 'template_name' : 'registration/password_reset_form.html'}, name='password_reset'),
    url(r'^login/accounts/password/reset/done/', django.contrib.auth.views.password_reset_done, { 'template_name' : 'registration/password_reset_done.html'}, name='password_reset_done'),

  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
