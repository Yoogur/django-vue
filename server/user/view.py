from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from server.tool.response_handler import simple_response, packet_response, err_response
from server.user.model import User


@require_http_methods(["POST"])
@simple_response
def user_register(request):
    content = request.POST
    username, nickname, password = content.get("username"), content.get("nickname"), content.get("password")
    if User.objects.filter(username=username):
        response = packet_response(False, "has such username")
        return response
    user = User()
    user.Config(username, nickname, password)
    user.save()
    response = packet_response(True, "success")
    return response


@require_http_methods(["GET"])
@simple_response
def user_login(request):
    content = request.GET
    username, password = content.get("username"), content.get("password")
    if not username or not password:
        response = packet_response(False, "username or password is null")
        return response
    if not User.objects.filter(username=username):
        response = packet_response(False, "username or password is error")
        return response
    user = User.objects.get(username=username)
    if not user.password == password:
        response = packet_response(False, "username or password is error")
        return response
    response = packet_response(False, "success login")
    return response
