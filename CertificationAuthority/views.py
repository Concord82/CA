# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()

from forms import AuthForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if not request.user.is_authenticated():
        form = AuthForm (request.POST or None)
        if request.POST and form.is_valid():
            user = form.login (request)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect("/")# Redirect to a success page.


        return render(request, 'index.html', {'login_form': form })
    else:
        auth.logout(request)
        form = AuthForm()
        return render(request, 'index.html', {'login_form': form })

# Вывод страницы с пользовательским профилем.
def userpage(request, username=None):

    if username == None:
        username = request.user.get_username()
    try:
        userprofile = User.objects.get(login_name=username)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'userpage.html', {'userprofile': userprofile})


def detail(request, question_id):
    return HttpResponse(_("You're looking at question %s." % question_id))