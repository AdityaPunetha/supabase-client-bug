from config import settings
from supabase._async.client import AsyncClient as Client, create_client


async def create_supabase() -> Client:
    return await create_client(settings.supabase_url, settings.supabase_key)
