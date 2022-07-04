# This REST API was developed with Python3
# FastApi is the main library that used in this code.For more details about FastApi visit this link:
- https://fastapi.tiangolo.com
 
# Before you start make sure that you have install python3 and the library in the requirments file
# navigate to the src folder and run the following command:
> pip install -r requirements.txt

# To run the server start uvicorn in your terminal
> uvicorn main:app --reload

# Go to http://127.0.0.1:8000/password
# You can then make requests to the api by specifying a url with parameters if need be.

Args:
        min_length: minimum password length.
        schars_num: number of special characters in the password.
        numbers_num: number of numbers in the password.
        count: number of passwords that must be created.

# For example: http://127.0.0.1:8000/password?min_length=6&schars_num=5&numbers_num=5&count=5
# To see what requests can be made navigate to the /docs