from django.shortcuts import render
import json

from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from .models import Users_info
import bcrypt


class SignUpView(View):
    def get(self,request):
        return render(request,'common/signup.html')

    def post(self, request):

        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            print(request)
        # if Users_info.objects.filter(user_id=data['id']).exists():
        #   return JsonResponse({"중복된 아이디 입니다."},status=400)
        else:
            data = Users_info(
                user_id=request.POST['user_id'],
                email=request.POST['email'],
                username=request.POST['username'],
                password1=request.POST['password1'],
                password2=request.POST['password2'],
                pin=request.POST['pin'],
                height=request.POST.get('height', 0),
                weight=request.POST.get('weight', 0),
                create_date=request.POST.get('create_date')
            )
            print(data)
        data.save()
        return render(request,'common/login.html')

    # def post(self, request):
    #     """
    #     계정생성
    #     """
    #     # if request.method == "POST":
    #     #     print("post")
    #     data = json.loads(request.body)
    #     #data = request.body
    #     print(data)
    #     password_not_hashed = data('password1')
    #     hashed_password = bcrypt.hashpw(password_not_hashed.encode("utf-8"), bcrypt.gensalt())
    #
    #     try:
    #
    #         Users_info(
    #             user_id =data['user_id'],
    #             email =data['email'],
    #             username =data['username'],
    #             password1 = hashed_password.decode("utf-8"),
    #             password2 = data['password2'],
    #             pin = data['pin'],
    #             weight =data['weight'],
    #             height =data['height']
    #         ).save()
    #
    #
    #         # 7.성공적으로 저장이 되었으면 성공 메시지를 보낸다.
    #         return JsonResponse({'message': '회원가입 성공'}, status=200)
    #
    #
    #     # 8.예외처리
    #     except KeyError:
    #         return JsonResponse({'message': "INVALID_KEYS"}, status=400)
    #
    #     return render(request, 'common/signup.html')

    # def get(self, request):
    #     user_data = Users_info.objects.values()
    #     return JsonResponse({'users':list(user_data)}, status=200)


def rankingpage(request):
    return render(request, 'common/ranking.html')


def introductionpage(request):
    return render(request, 'common/introduction.html')


def calendarpage(request):
    return render(request, 'common/calendar.html')


def mypage(request):
    return render(request, 'common/mypage.html')
