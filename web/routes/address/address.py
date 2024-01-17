from fastapi import APIRouter

from features.address import address_parser, AddressParseResult

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
    parse_result = address_parser.parse(raw_address)

    return parse_result


