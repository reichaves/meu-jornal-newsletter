import requests
import lxml.html

capa_links = ["https://www.vercapas.com.br/capa/folha-de-s-paulo/", "https://www.vercapas.com.br/capa/estadao/", 
              "https://www.vercapas.com.br/capa/o-globo/", "https://www.vercapas.com.br/capa/valor-economico/"]

impressa_links = []

def capa_jornal():
  for url in capa_links:
    page = requests.get(url)
    doc = lxml.html.fromstring(page.content)
    capa_jornal_impresso = doc.xpath('//figure//a//img[@id="img1"]/@src')[0]
    impressa_links.append(capa_jornal_impresso)
  return impressa_links
