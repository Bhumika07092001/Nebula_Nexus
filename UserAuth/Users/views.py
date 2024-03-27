from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer, EmailOTPSerializer, ForgotPasswordSerializer, LoginOTPSerializer,ResetPasswordSerializer

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerificationAPIView(APIView):
    def post(self, request):
        serializer = EmailOTPSerializer(data=request.data)
        #
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginOTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            try:
                user = CustomUser.objects.get(email=email)
                print(user.email)
            except CustomUser.DoesNotExist:
                return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
            
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message':'login sucessful',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        # 
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

class ResetPasswordAPIView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        # 
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

