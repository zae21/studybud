from django.http import JsonResponse

def getRoutes(request):
    routes = [
        'GET /api/rooms',
    ]
    return JsonResponse()