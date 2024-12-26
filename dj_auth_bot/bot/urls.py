from django.urls import path


from .views import VerifyUserCodeView


urlpatterns = [
    path('verify/', VerifyUserCodeView.as_view(), name='verify')
]