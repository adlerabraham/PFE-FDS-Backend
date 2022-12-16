from rest_framework.routers import DefaultRouter
from django.urls import path, include
from user.views import *
from rest_framework_simplejwt.views import TokenRefreshView



router =  DefaultRouter()

router.register('userprofile', User_viewset, basename='userprofile'),

urlpatterns= [

    path('', include(router.urls)),
    path('login',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshlogin',TokenRefreshView.as_view(), name='token_refresh'),
    path('updateuser/<int:pk>/',Update_user_view.as_view(), name='updateuser'),
    path('changepassword/<int:pk>/', Change_password_view.as_view(), name='changepassword'),
    path('verifyemail',VerifyEmail.as_view(), name='verifyemail'),
    path('registeruser',Register_user_view.as_view(), name='registeruser'),
    path('resetpassword',Reset_password_send_email_view.as_view(), name='resetpassword'),
    path('resetpassword/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='resetpasswordconfirm'),
    path('setnewpassword',set_new_password_view.as_view(), name='setnewpassword'),
    
    
]
