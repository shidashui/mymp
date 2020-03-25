import hashlib
import time

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import User
from utils import wx_login


class Login(APIView):
    def post(self, request):
        param = request.data
        if param.get('code'):
            # Wx_login是微信为我们提供的登录方法，这里的data已经有一个session_key和openid了
            data = wx_login.login(param.get("code"))
            if data:
                md5 = hashlib.md5()
                md5.update(data.get("session_key").encode("utf8"))
                md5.update(str(time.time()).encode("utf8"))
                token = md5.hexdigest()
                if not User.objects.filter(open_id=data.get("openid")).first():
                    User.objects.create(
                        open_id=data.get("openid"),
                        session_key=data.get("session_key"),
                        token=token
                    )
                return Response({"code":200, "msg":"suc", "data":{"token":token}})
            else:
                return Response({"code":202, "msg":"code无效"})
        else:
            return Response({"code":201, "msg":"缺少参数"})

