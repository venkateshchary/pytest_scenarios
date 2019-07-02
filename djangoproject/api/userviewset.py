from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login


@csrf_exempt
@api_view(['POST'])
def userlogin(request):
    try:
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            print("request.session['username']:", request.session['username'])
            html = "<html><body>%s is logged in successfully.</body></html>" %user
            return JsonResponse({"message":"logged in successfully"})
        else:
            html = "<html><body>%s is not found.</body></html>" %username
            return HttpResponse(html)
    except AssertionError:
        return JsonResponse({"message": "user not found"})

@csrf_exempt
@api_view(['POST'])
def userregister(request):
    try:
        print(request.data)
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]
        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return HttpResponse(status=200)
    except Exception:
        return JsonResponse({"message": "registration is failed"})







