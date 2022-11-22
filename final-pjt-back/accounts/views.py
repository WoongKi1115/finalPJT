from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def signup(request):
    password = request.data.get("password")
    password_confirm = request.data.get("passwordConfirm")

    if password != password_confirm:
        return Response({"error: 비밀번호가 일치하지 않습니다!"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def whoareyou(request):
    you = request.user
    print(you)
    if not request.user.is_authenticated:
        return Response({"message": "no auth"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        serializer = UserSerializer(you)
        return Response(serializer.data,)