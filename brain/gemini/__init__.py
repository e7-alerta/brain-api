import google.generativeai as genai

from brain.gemini.client.config import GOOGLE_API_KEYS

from brain.gemini.usecases.address.address_parser import GenaiAddressParser

genai.configure(api_key=GOOGLE_API_KEYS[0])

model = genai.GenerativeModel("gemini-pro")


genia_address_parser = GenaiAddressParser(model)