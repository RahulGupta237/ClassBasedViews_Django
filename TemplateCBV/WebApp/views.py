from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView

# Create your views here.


class PortFolio(RedirectView):
    url='https://rahul237.herokuapp.com/'


class RahulRedirect(RedirectView):
    pattern_name='rahul'
    permanent=True
    #query_string=False # disappear string in case 12?agHSGjgj
    query_string=True # if we need construct url then used as context i.e 12?name=rahul

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)

