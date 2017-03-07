from debug_toolbar.panels import Panel
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponseForbidden
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib import auth

from . import views
from .forms import UserForm


class UserPanel(Panel):
    """
    Panel that allows you to login as other recently-logged in users.
    """
    title = _('User')
    template = 'djdt_user_panel/panel.html'
    has_content = True

    @property
    def nav_subtitle(self):
        if self.request.user.is_authenticated():
            return "{0}".format(self.request.user)
        else:
            return 'Not currently logged in'
    @property
    def content(self):
        try:
            User = auth.get_user_model()
        except:
            from django.contrib.auth.models import User
        if not getattr(settings, 'DEBUG_TOOLBAR_USER_DEBUG', settings.DEBUG):
            return HttpResponseForbidden()

        current = []

        if self.request.user.is_authenticated():
            for field in User._meta.fields:
                if field.name == 'password':
                    continue
                current.append(
                    (field.attname, getattr(self.request.user, field.attname))
                )

        return render_to_string(self.template, {
            'user'   : self.request.user,
            'form'   : UserForm(),
            'next'   : self.request.GET.get('next'),
            'users'  : User.objects.order_by('-last_login')[:10],
            'current': current,
        })

    def process_request(self, request):
        self.request = request

    @classmethod
    def get_urls(cls):
        return [
            url(r'^users/login/$', views.login_form, name='userpanel-login-form'),
            url(r'^users/login/(?P<pk>-?\d+)$', views.login, name='userpanel-login'),
            url(r'^users/logout$', views.logout, name='userpanel-logout'),
        ]
