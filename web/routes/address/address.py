from fastapi import APIRouter

from features.address import address_parser, AddressParseResult
from logger import logger

address_routes = APIRouter()


# ai/addresses/parse
@address_routes.post("/ai/addresses/parse")
async def parse_address(bodyForm: dict) -> AddressParseResult:
    """
    Dado una direccion devuelta por una api de geolocalizacion, evalua este texto y extrae la calle y el numero de esta.
    Si no se puede extraer la calle y el numero, devuelve success=false
    :return:
    """
    raw_address = bodyForm["raw_address"]
    parse_result = None
    try:
        parse_result = address_parser.parse(raw_address)
        logger.info(f"[ AI_ADDRESS_PARSE ] parsing {raw_address}", extra=parse_result.model_dump())
    except Exception as e:
        logger.error(f"[ AI_ADDRESS_PARSE ] error parsing {raw_address}", exc_info=True)
        raise e

    return parse_result


