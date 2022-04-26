# 1. https://trandon.herokuapp.com/users/register/
This api is used to register/create a new account. Accept only POST request. It takes json arguments-
  {
    "username" : "<user_name>",
    "first_name" : "<first_name>",
    "last_name" : "<last_name>",
    "email" : "<email (should be unique)>",
    "password" : "<password>",
    "password2" : "<confirm_password>"
  }
  
Response --
    {
      "response": "Registration Successful",
      "username": "<user_name>",
      "email": "<email>",
      "token": {
          "refresh": "eyJ3eXAiOiJKV1QiLCJhbGciOiJIUzI5NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MTA0MjAzNiwiaWF0IjoxNjUwOTY1NjM8LCJqdGkiOiJjMDI0MjUzZThmZGE0OTg5YTZlYzVhOTY1YzA0M2Q2OCIsInVzZXJfaWQiOjN9.bP92h9L3VarUeNFDeCdhvm4wwRLdXys_XRzdSsg2r9o",
          "access": "eyJ1eXAiOiJKV0QiLCJhbGciOiJIUzI1NiJ3.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwOTY3OTM2LCJpYXQiOjE2NTA1NjU2MzYsImp0aSI6IjViNjM5NmMyZjQxOTQ2OTg5NjEzMWE1MzIzOTdkYzA5IiwidXNlcl9pZCI6M30.UvLEp_xMIE9utsVamF38qe-FeBtnHU-w0CjJCM5hzhw"
         }
     }
  
# 2. https://trandon.herokuapp.com/users/api/token/
  This api is used to login a user, it will give the refresh and access token as a response. Accept only POST request. It takes json arguments-
  
    {
      "email" : "smtptesting409@gmail.com",
      "password" : "smtp@409"
    }
Response --
    {
      "refresh": "eyJ3eXAiOiJKV1QiLCJhbGciOiJIUzI5NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MTA0MjAzNiwiaWF0IjoxNjUwOTY1NjM8LCJqdGkiOiJjMDI0MjUzZThmZGE0OTg5YTZlYzVhOTY1YzA0M2Q2OCIsInVzZXJfaWQiOjN9.bP92h9L3VarUeNFDeCdhvm4wwRLdXys_XRzdSsg2r9o",
      "access": "eyJ1eXAiOiJKV0QiLCJhbGciOiJIUzI1NiJ3.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwOTY3OTM2LCJpYXQiOjE2NTA1NjU2MzYsImp0aSI6IjViNjM5NmMyZjQxOTQ2OTg5NjEzMWE1MzIzOTdkYzA5IiwidXNlcl9pZCI6M30.UvLEp_xMIE9utsVamF38qe-FeBtnHU-w0CjJCM5hzhw"
    }

 # 3. https://trandon.herokuapp.com/users/api/token/refresh/
  This api will take refresh token as an argument and will give access token as a response. Accept only POST request.
    {
      "refresh": "eyJ3eXAiOiJKV1QiLCJhbGciOiJIUzI5NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MTA0MjAzNiwiaWF0IjoxNjUwOTY1NjM8LCJqdGkiOiJjMDI0MjUzZThmZGE0OTg5YTZlYzVhOTY1YzA0M2Q2OCIsInVzZXJfaWQiOjN9.bP92h9L3VarUeNFDeCdhvm4wwRLdXys_XRzdSsg2r9o",
    }
  Response --
    {
      "access": "eyJ1eXAiOiJKV0QiLCJhbGciOiJIUzI1NiJ3.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwOTY3OTM2LCJpYXQiOjE2NTA1NjU2MzYsImp0aSI6IjViNjM5NmMyZjQxOTQ2OTg5NjEzMWE1MzIzOTdkYzA5IiwidXNlcl9pZCI6M30.UvLEp_xMIE9utsVamF38qe-FeBtnHU-w0CjJCM5hzhw"
    }
  
# 4. https://trandon.herokuapp.com/files/document/
  
  This api accepts GET and POST request.
  For POST request, need to pass two arguments first one is the name of the file that you are going to upload and second argument is the file that you want to upload.
  
  For GET request, it give response as (Note- This is a single response.)--
    {
      "id": 1,
      "description": "song",
      "document": "https://trandon.herokuapp.com/intern/MEDIA_ROOT/documents/Falak_Tu_Garaj_Tu_-_KGF_Chapter_2_128_Kbps.mp3",
      "uploaded_at": "2022-04-26T09:58:53.768688Z"
    }
  
  # 5. https://trandon.herokuapp.com/files/document/<intger: id>/
    This api accepts GET, PUT, PATCH, DELETE requests.
  
