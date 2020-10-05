from django.http import JsonResponse


def simple_response(func):
    def handle(request):
        response = packet_handle(func, request)
        return JsonResponse(response)

    def packet_handle(func, request):
        try:
            response = func(request)
        except Exception as e:
            response = err_response(e)
        return response

    return handle


def success_response(sMsg=""):
    response = {}
    response['result'] = True
    response['msg'] = sMsg
    return response


def fail_response(sMsg=""):
    response = {}
    response['result'] = False
    response['msg'] = sMsg
    return response


def err_response(exception):
    response = {}
    response['result'] = False
    response['msg'] = str(exception)
    return response
