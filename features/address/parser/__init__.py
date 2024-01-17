from brain.gemini import genia_address_parser
from features.address.parser.parser import AddressParser


address_parser = AddressParser(genai_parser=genia_address_parser)