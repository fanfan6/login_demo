# coding=utf-8
# 中间件， 用户未登录时跳转到登录页面

from django.shortcuts import HttpResponseRedirect

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class QtsAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path != '/login/':
            if request.COOKIES.get('username', None):
                pass
            else:
                return HttpResponseRedirect('/login/')
