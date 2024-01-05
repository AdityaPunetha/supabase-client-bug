from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from supabase import Client, create_client

from config import settings

supabase: Client = create_client(settings.supabase_url, settings.supabase_key)


token_key = APIKeyHeader(name="Authorization")


async def get_current_user(authorization: str = Security(token_key)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Unauthorized")
    tokens = authorization.split(" ")

    if len(tokens) != 2:
        raise HTTPException(
            status_code=401, detail="Invalid authorization header format"
        )

    access_token, refresh_token = tokens
    try:
        session = supabase.auth.set_session(
            access_token=access_token, refresh_token=refresh_token
        )
        return session
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid token")
