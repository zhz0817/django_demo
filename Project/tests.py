import json

from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def test1(request):
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))
    return JsonResponse(data={"sum": a+b}, safe=False)


@require_POST
def test2(request):
    params = json.loads(request.body)
    a = int(params["a"])
    b = int(params["b"])
    print(a + b)
    return JsonResponse(data={"sum": a + b}, safe=False)
