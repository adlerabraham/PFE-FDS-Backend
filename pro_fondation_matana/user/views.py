from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from user.models import *
from user.serializers import *
from rest_framework.generics import UpdateAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
import jwt
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util


# Create your views here.

#################### AUTHENTIFICATION ######################

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


#################################################################




################## REGISTRATION #################################

class User_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = User_serializer



class Super_admin_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Super_admin_serializer



class Admin_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Admin_serializer



class Teacher_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Teacher_serializer



class Student_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Student_serializer





class Register_user_view(GenericAPIView):

    serializer_class = Register_user_serializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('verifyemail')
        absurl = 'http://'+ current_site + relativeLink + "?token=" + str(token)
        email_body = 'Hi ' + user.username + ',' + '\n I am Levilson Palanquet, your registration assistant. Please, use the link below to verify your email account ! \n \n \n ' + absurl
        data = {'email_body': email_body, 'to_email':user.email ,'email_subject' : 'VERIFY YOUR EMAIL'}

        Util.send_email(data)

        return Response (user_data, status=status.HTTP_201_CREATED)
 
    
class VerifyEmail (GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response ({'email' : 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier :
            return Response({'error': 'Activation Expired'}, status= status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier :
            return Response({'error': 'Invalid Token'}, status= status.HTTP_400_BAD_REQUEST)




class Update_user_view(UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = Update_user_serializer






class Change_password_view(UpdateAPIView):

    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = Change_password_serializer


class Reset_password_send_email_view(GenericAPIView):
    
    serializer_class = Reset_password_send_email_serializer

    def post (self, request):
        data = request.data
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception= True)

        email = request.data['email']
        
        if User.objects.filter(email=email).exists():
                user= User.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
                token = PasswordResetTokenGenerator().make_token(user)
                current_site = get_current_site(request= request).domain
                relativeLink = reverse('resetpasswordconfirm', kwargs={'uidb64':uidb64, 'token': token})
                absurl = 'http://'+ current_site + relativeLink 
                email_body = 'Hello, \n I am Levilson Palanquet, your registration assistant. Please, use the link below to reset your password \n \n \n ' + absurl
                data = {'email_body': email_body, 'to_email':user.email ,'email_subject' : 'RESET YOUR PASSWORD'}

                Util.send_email(data)

        return Response ({'success':'We have sent you a link to reset your password'}, status = status.HTTP_200_OK )




class PasswordTokenCheckAPI(GenericAPIView):
    

    def get(self, request, uidb64, token):
    
        try:
            id=smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error':'Token is not valid, please request a new one'},status = status.HTTP_401_UNAUTHORIZED)

            return Response({'success': True, 'message': 'Credentials valid', 'uidb64': uidb64, 'token':token}, status = status.HTTP_200_OK)
           
        except DjangoUnicodeDecodeError as identifier :
            #if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error':'Token is not valid, please request a new one'},status = status.HTTP_401_UNAUTHORIZED)



class set_new_password_view(GenericAPIView):
    serializer_class = Set_new_password_serializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception= True)
        return Response({'success': True, 'message': 'Password reset success'}, status = status.HTTP_200_OK)

              
