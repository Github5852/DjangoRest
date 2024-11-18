from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router = DefaultRouter()

router.register('studentapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
    path('admin',admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='Token_Obtain_Pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='Token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='Token_verify'),


]

# http POST http://127.0.0.1:8000/gettoken/ username="superuser" password="superuser"
# acess="xxxx"
# refresh="xxxx"

# http POST http://127.0.0.1:8000/verifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODEyNjQyLCJpYXQiOjE3MzE4
# MTIzNDIsImp0aSI6IjAzOTRmYjlhZDU2NDQzZGRhMzRlMWMwNTdmZjY4MzAwIiwidXNlcl9pZCI6MX0.E9Ww9A-K6Hm1ngYE3_d3Kjz19K_7KQ3pX89mdTt_XDo"

# http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTg5ODc0MiwiaWF0IjoxNzM
# xODEyMzQyLCJqdGkiOiI1NjFhMGRlMjNiMTA0NmI3OTc0YjFkMTIwMDVjOTY3YyIsInVzZXJfaWQiOjF9.X8OJ0wkv9xEF2fyEFkr2oFUBOT9TkZddwfuu06_WAfc"

# http command to get data
# http http://127.0.0.1:8000/studentapi/

# This is GET Request:
# below token is generated from refresh token , it is new Access Token. it will give acces to the API
# http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODEyNjQyLCJpYXQiOjE3MzE4
# MTIzNDIsImp0aSI6IjAzOTRmYjlhZDU2NDQzZGRhMzRlMWMwNTdmZjY4MzAwIiwidXNlcl9pZCI6MX0.E9Ww9A-K6Hm1ngYE3_d3Kjz19K_7KQ3pX89mdTt_XDo'

# This is POST Request:
# http -f POST http://127.0.0.1:8000/studentapi/ name=Akshay roll=102 city=nsk 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODE0MzM1LCJpYXQiOjE3MzE4
# MTQwMzUsImp0aSI6ImRhNTc3NmJiYTRhNjRmOTc5OGQ2ZTA1NjA2NjYzYzllIiwidXNlcl9pZCI6MX0.s4fws718WVp-7rH12lepG4WDXX2Ku08O_xyHf0C-wAY'

# This is PUT Request:
# http PUT http://127.0.0.1:8000/studentapi/2/ name=Ramesh roll=103 city=Nagar 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODE0MzM1LCJpYXQiOjE3MzE4
# MTQwMzUsImp0aSI6ImRhNTc3NmJiYTRhNjRmOTc5OGQ2ZTA1NjA2NjYzYzllIiwidXNlcl9pZCI6MX0.s4fws718WVp-7rH12lepG4WDXX2Ku08O_xyHf0C-wAY'

# http DELETE http://127.0.0.1:8000/studentapi/2/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODE0MzM1LCJpYXQiOjE3MzE4
# MTQwMzUsImp0aSI6ImRhNTc3NmJiYTRhNjRmOTc5OGQ2ZTA1NjA2NjYzYzllIiwidXNlcl9pZCI6MX0.s4fws718WVp-7rH12lepG4WDXX2Ku08O_xyHf0C-wAY'


