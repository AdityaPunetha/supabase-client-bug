from fastapi import APIRouter, Depends
from supabase import Client, create_client

from config import settings
from oauth2 import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])
supabase: Client = create_client(settings.supabase_url, settings.supabase_key)


@router.post("/google")
def google():
    data = supabase.auth.sign_in_with_oauth(
        {
            "provider": "google",
        }
    )
    return data


@router.get("/protected")
async def protected_route(session: dict = Depends(get_current_user)):
    return {"message": "You are authorized to access this route"}
