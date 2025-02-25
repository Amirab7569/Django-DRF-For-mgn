from django.urls import path
from  . import views 
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.schemas import get_schema_view

app_name = 'accounts'

router = routers.SimpleRouter()
router.register('user', views.UserViewset)


urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls


# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNjI2ODYyMSwiaWF0IjoxNzM2MTgyMjIxLCJqdGkiOiJhMjMxM2IyYmVkNjA0NjFkYWJkNGVjMTRhNjllNGI0ZiIsInVzZXJfaWQiOjF9.Pswkk7yAlws56jag9EgflkZ3P13Fpv9NEeKZQMColuo",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM2MTgyNTIxLCJpYXQiOjE3MzYxODIyMjEsImp0aSI6IjY3YTExOTMyMjU5YTQ4Y2E5MGE1MjBlMmMzZTVlNWViIiwidXNlcl9pZCI6MX0.eJ-_tJo1w1Dfcr27sDxZCs-pXo7jPSU1TxfpjbbvrME"
# }