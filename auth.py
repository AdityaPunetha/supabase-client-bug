from fastapi import APIRouter, Depends
from oauth2 import get_current_user
from supabase_client import Client, create_supabase

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/google")
async def google(supabase: Client = Depends(create_supabase)):
    data = await supabase.auth.sign_in_with_oauth(
        {
            "provider": "google",
        }
    )
    return data


@router.post("/github")
async def github(supabase: Client = Depends(create_supabase)):
    data = await supabase.auth.sign_in_with_oauth(
        {
            "provider": "github",
        }
    )
    return data


@router.get("/protected")
async def protected_route(session: dict = Depends(get_current_user)):
    return {"message": "You are authorized to access this route"}


@router.post("/signout")
async def sign_out(supabase: Client = Depends(create_supabase)):
    await supabase.auth.sign_out()
