from django.http import JsonResponse



def IndexPrint(request):
    results = {}
    results["hello"] = "Hello World"
    return JsonResponse(results)