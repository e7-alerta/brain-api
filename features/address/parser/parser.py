from typing import Optional

import google.generativeai as genai
from pydantic import BaseModel

from brain.gemini.usecases.address.address_parser import GenaiAddressParser


class AddressParseResult(BaseModel):
    street: Optional[str] = None
    number: Optional[str] = None
    success: bool = False


class AddressParser:
    def __init__(self, genai_parser: GenaiAddressParser):
        self.genai_parser = genai_parser
        pass

    def parse(self, address) -> AddressParseResult:
        result = self.genai_parser.parse(address)
        return AddressParseResult(**result.model_dump())


if __name__ == '__main__':
    SAMPLES = [
        "Av. Remedios de Escalada de San Martin 2639, B1822 Valentín Alsina, Provincia de Buenos Aires, Argentina",
        "CHO, Viamonte 2200, B1822 Lanús, Provincia de Buenos Aires, Argentina",
        "Liniers, Valentín Alsina, Provincia de Buenos Aires, Argentina"
    ]

    GOOGLE_API_KEY="AIzaSyBHNwhGR9g291lJ9IBNtUQQ97nq25vaQfs"      # ernestsimionato1
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    address_parser = GenaiAddressParser(model)

    parser = AddressParser(address_parser)
    for sample in SAMPLES:
        result = parser.parse(sample)
        print(result)