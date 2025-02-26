import reflex as rx
import Creyente.constants as const
from Creyente.model.MUEBLES import MUEBLES
from Creyente.model.MODELOS import MODELOS
from .client_supabase import BaseAPI
from  Creyente.api.Muebles_api import MueblesAPI
from  Creyente.api.Modelos_api import ModelosAPI




SUPABASE_API = BaseAPI()
muebles_api_instance = MueblesAPI()
modelos_api_intance= ModelosAPI()

async def repo () -> str:
    return const.CATALOGO


async def api_Muebles() -> list[MUEBLES]:
    return muebles_api_instance.Muebles()

async def api_Modelos() -> list[MODELOS]:
    return modelos_api_intance.Modelos()



async def api_SQL_Modelos() -> list[MODELOS,MUEBLES]:
    return SUPABASE_API.SQL_Modelos()
