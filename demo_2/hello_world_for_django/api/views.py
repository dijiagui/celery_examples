from django.http import HttpResponse
from api import tasks
# Create your views here.


def test(request):
    tasks.run.delay()
    return HttpResponse('success')