from django.shortcuts import render,redirect

from ..service.role_service import RoleService


class RoleListCtl:

    def __init__(self):
        self.form = {}
        self.form['id'] = 0
        self.form['message'] = ''
        self.form['error'] = False
        self.form['input_error'] = {}
        self.form['page_no'] = 1
        self.form['page_size'] = 5
        self.form['list'] = []

    def request_to_form(self,request):
       self.form['name'] = request.POST.get('Name')

    def display(self,request,operation = '',id=0):
        if operation == 'delete':
            RoleService().delete(id)
            return redirect('/ors/RoleList/')
        self.form['list'] = RoleService().search(self.form)
        return render(request, "role_list.html", {"form": self.form})

    def submit(self,request):
        if request.POST['operation'] == "next":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] += 1

        if request.POST['operation'] == "previous":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] -= 1

        if request.POST['operation'] == "search":
            self.form['page_no'] = 1
            self.request_to_form(request)

        self.form['list'] = RoleService().search(self.form)
        return render(request, "role_list.html", {"form": self.form})

