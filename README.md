# File-Sharing
Django


## steps

###  Define a folder structure


### Define REST API Endpoints

1. User Registration:
    - Method: POST
    - Endpoint: http://127.0.0.1:8000/api/register/
    - Body (JSON):
        {
            "email": "sopan@example.com",
            "password": "password",
            "roles": "admin(Ops) / client"              # choose any one of them
        }
    - Headers:
        Content-Type: application/json


2. User Login:
    - Method: POST
    - Endpoint: http://127.0.0.1:8000/api/<User-Type>/login/
    - Body (JSON):
        {
            "email": "sopan@example.com",
            "password": "password"
        }
    - Headers:
        Content-Type: application/json


3. Upload File:
    - Method: POST
    - Endpoint: http://127.0.0.1:8000/api/upload-file/<user_type>
    - Headers:
        Content-Type: multipart/form-data
        Authorization: Bearer <your_access_token> (Use the access token obtained after login)


4. Download File:
    - Method: GET
    - Endpoint: http://127.0.0.1:8000/api/download-file/<file_id>/
    - Headers:
        Authorization: Bearer <your_access_token> (Use the access token obtained after login)


5. Get All Upload Files (by Ops User):
    - Method: GET
    - Endpoint: http://127.0.0.1:8000/api/get-all-files/<user_type>
    - Headers:
        Authorization: Bearer <your_access_token> (Use the access token obtained after login)


#### important point to remember:
- For endpoints requiring authorization (Bearer token), you need to obtain the access token by successfully logging in.
- Replace <your_access_token> with the actual access token obtained after login.
- File upload requires sending a multipart/form-data request, so set the appropriate headers for file upload.


