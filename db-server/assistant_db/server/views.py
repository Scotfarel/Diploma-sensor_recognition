from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Sensor


@csrf_exempt
@require_POST
def create_sensor(request):
    body_unicode = request.body.decode('utf-8')
    return HttpResponse(f"Creating sensor with params: {body_unicode}")


@csrf_exempt
@require_GET
def get_sensor(request):
    sensors_list = Sensor.objects.order_by('-name')[:5]
    return HttpResponse(sensors_list)
