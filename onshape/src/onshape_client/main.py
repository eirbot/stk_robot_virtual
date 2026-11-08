"""FastAPI server to retrieve a temporary user authorization token."""

import os

from authlib.integrations.starlette_client import OAuth
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware

load_dotenv(find_dotenv(usecwd=True))

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ["SESSION_SECRET_KEY"])

oauth = OAuth()
oauth.register(
    name="onshape",
    client_id=os.environ["ONSHAPE_CLIENT_ID"],
    client_secret=os.environ["ONSHAPE_CLIENT_SECRET"],
    authorize_url="https://oauth.onshape.com/oauth/authorize",
    access_token_url="https://oauth.onshape.com/oauth/token",
    client_kwargs={"token_endpoint_auth_method": "client_secret_post"},
)

REDIRECT_URI = "http://localhost:8080/callback"  # register this exact URL in Onshape


@app.get("/")
async def login(request: Request):
    return await oauth.onshape.authorize_redirect(request, REDIRECT_URI)


@app.get("/callback")
async def callback(request: Request):
    token = await oauth.onshape.authorize_access_token(request)
    return {
        "access_token": token["access_token"],
        "refresh_token": token.get("refresh_token"),
        "expires_in": token.get("expires_in"),
    }
