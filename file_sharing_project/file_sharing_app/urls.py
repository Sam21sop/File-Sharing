from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    FileUploadView,
    FileDownloadView,
    GetAllUploadFilesView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('upload-file/', FileUploadView.as_view(), name='file-upload'),
    path('download-file/<int:file_id>/', FileDownloadView.as_view(), name='file-download'),
    path('get-all-files/', GetAllUploadFilesView.as_view(), name='get-all-files'),
]




# from django.urls import path
# from .views import SignupView, LoginView, ClientSignupView, EmailVerifyView, ClientDownloadView, OpsGetAllFilesView


# urlpatterns = [
#     # operation routes
#     path('signup/', SignupView.as_view(), name='signup'),
#     path('login/', LoginView.as_view(), name='login'),

#     # Client routes
#     path('client/signup/', ClientSignupView.as_view(), name='client-signup'),
#     path('client/email-verify/<str:email_token>/', EmailVerifyView.as_view(), name='email-verify'),

#     path('client/download-file/<int:file_id>/', ClientDownloadView.as_view(), name='client-download'),
#     path('ops/get-all-files/', OpsGetAllFilesView.as_view(), name='ops-get-all-files'),
# ]
