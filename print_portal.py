import os
from urllib.parse import urlencode
from urllib.request import urlretrieve
from base64 import b64encode
from sendgrid.helpers.mail import Attachment

API_FLASH_KEY = os.environ["API_FLASH_KEY"]

def print_g1():
  params = urlencode(dict(access_key=API_FLASH_KEY,
                          url="https://g1.globo.com"))
  urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "print_portal_g1.jpeg")
  
  image = open('print_portal_g1.jpeg', 'rb')
  contents = image.read()
  image.close()

  contents
  data = b64encode(contents).decode()
  anexo_g1 = Attachment(file_content = data, file_name = 'print_portal_g1.jpeg')
  return anexo_g1

def print_globo_com():
  params = urlencode(dict(access_key=API_FLASH_KEY,
                          url="https://globo.com"))
  urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "print_portal_globo_com.jpeg")
  
  image = open('print_portal_globo_com.jpeg', 'rb')
  contents = image.read()
  image.close()

  contents
  data = b64encode(contents).decode()
  anexo_globo_com = Attachment(file_content = data, file_name = 'print_portal_globo_com.jpeg')
  return anexo_globo_com

def print_oglobo():
  params = urlencode(dict(access_key=API_FLASH_KEY,
                          url="https://oglobo.globo.com/"))
  urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "print_portal_oglobo.jpeg")
  
  image = open('print_portal_oglobo.jpeg', 'rb')
  contents = image.read()
  image.close()

  contents
  data = b64encode(contents).decode()
  anexo_oglobo = Attachment(file_content = data, file_name = 'print_portal_oglobo.jpeg')
  return anexo_oglobo

def print_uol():
  params = urlencode(dict(access_key=API_FLASH_KEY,
                          url="https://www.uol.com.br/"))
  urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "print_portal_uol.jpeg")
  
  image = open('print_portal_uol.jpeg', 'rb')
  contents = image.read()
  image.close()

  contents
  data = b64encode(contents).decode()
  anexo_uol = Attachment(file_content = data, file_name = 'print_portal_uol.jpeg')
  return anexo_uol
