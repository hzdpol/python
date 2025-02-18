

from django_micro import configure,route,run
from django.http import HttpResponse

DEBUG = True
Limit = 10
html ="""
<div style="background-color:#77DFF5;height:100%">
    <h1 style="clock:white;text-align:center">Yeah~</h1>
    </div>

"""
configure(locals())
@route('',name='home')
def homepage(request):
    name = request.GET.get('name','world')
    return HttpResponse(html)
application = run()