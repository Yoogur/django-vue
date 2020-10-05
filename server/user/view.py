from django.views.decorators.http import require_http_methods

from server.tool.response_handler import simple_response, fail_response, success_response
from server.user.model import User


@require_http_methods(["POST"])
@simple_response
def user_register(request):
    content = request.POST
    username, nickname, password = content.get("username"), content.get("nickname"), content.get("password")
    if User.objects.filter(username=username):
        return fail_response("has such username")
    user = User()
    user.Config(username, nickname, password)
    user.save()
    return success_response("success register")


@require_http_methods(["GET"])
@simple_response
def user_login(request):
    content = request.GET
    username, password = content.get("username"), content.get("password")

    if not username or not password:
        return fail_response("username or password is null")
    if not User.objects.filter(username=username):
        return fail_response("username or password is error")
    user = User.objects.get(username=username)
    if not user.password == password:
        return fail_response("username or password is error")

    return success_response("success login")
