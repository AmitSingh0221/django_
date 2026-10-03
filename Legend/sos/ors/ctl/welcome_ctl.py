from django.shortcuts import render

from .base_ctl import BaseCtl


class WelcomeCtl(BaseCtl):

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})
