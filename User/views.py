from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from User.models import User


class U_P_Register(APIView):

    def get(self, request):
        data = {
            'status': 200,
            'msg': 'request ok'
        }
        return Response(data)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password is not None:

            if password == re_password:
                user = User()
                user.username = username
                user.password = user.set_password(password)
                user.save()

                data = {
                    'status': 200,
                    'msg': 'register ok'
                }
                return Response(data)
            else:
                data = {
                    'status': 201,
                    'msg': 'register error'
                }
                return Response(data)
        else:
            data = {
                'status': 202,
                'msg': 'password is None'
            }
            return Response(data)


class t_Register(APIView):
    def get(self,request):
        data = {
            'stauts': 200,
            'msg': 'request ok'
        }
        return Response(data)

    def post(self,request):
        phone = request.POST.get('phone')
        yzm = request.POST.get('yzm')
        data = {
            'stauts': 200,
            'msg': 'request ok'
        }
        return Response(data)