"""
 Main REST API file
"""
# Import libraries
from typing import Optional

# Import Fast API to build REST API
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from starlette.exceptions import HTTPException as StarletteHTTPException

# Import internal files
from password import PasswordGenerator
import sys


# Initiate the FastApi app
app = FastAPI()

# Password generator
@app.get("/password")
def get_password(min_length: Optional[int] = 6,
                 schars_num: Optional[int] = 1,
                 numbers_num: Optional[int] = 1,
                 count: Optional[int] = 1):

    
    # Initiate the Password Generator class
    p = PasswordGenerator(min_length, schars_num, numbers_num, count)

    # Create the password list
    passwords_list = p.generate_passwords_list()

    # Return the response in Json format
    response = {"passwords_list": passwords_list}
    return JSONResponse(response)


# Handle 404 error
@app.get("/404", summary="Page Not Found", tags=['Views'])
async def root():
    return FileResponse('templates/404.html')


# Redirection to 404 page
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/404")
