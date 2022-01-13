import requests
import lxml.html

def link_globo_com():
  url = "https://www.globo.com/"
  page = requests.get(url)
  doc = lxml.html.fromstring(page.content)
  manchete_globo_com = doc.xpath('//div[@class="headline__container"]//a/@href')
  return manchete_globo_com

def link_g1():
  url = "https://g1.globo.com/"
  page = requests.get(url)
  doc = lxml.html.fromstring(page.content)
  manchete_g1 = doc.xpath('//div[@class="bastian-feed-item" and @data-index= "1"]//div[@class="feed-post-body-title gui-color-primary gui-color-hover "]//div[@class="_evt"]//a[@class="feed-post-link gui-color-primary gui-color-hover"]/@href')
  return manchete_g1

def link_valor():
  url = "https://valor.globo.com/"
  page = requests.get(url)
  doc = lxml.html.fromstring(page.content)
  manchete_valor = doc.xpath('//div[@class="highlight__title theme-title-element "]//a/@href')[0]
  return manchete_valor 

def link_uol():
  url = "https://www.uol.com.br/"
  page = requests.get(url)
  doc = lxml.html.fromstring(page.content)
  manchete_uol = doc.xpath('//article[@class = "headlineMain section__grid__main__highlight__item"]//a/@href')[0]
  return manchete_uol

def link_folha():
  url = "https://www.folha.uol.com.br/"
  page = requests.get(url)
  doc = lxml.html.fromstring(page.content)
  manchete_folha = doc.xpath('//a[@class = "c-main-headline__url"]/@href')[0]
  return manchete_folha

def link_estadao():
  url = "https://www.estadao.com.br/"
  page = requests.get(url)
  doc = lxml.html.fromstring(page.content)
  manchete_estadao = doc.xpath('//div[@class = "intro"]//a/@href')[0]
  return manchete_estadao

def link_oglobo():
  url = "https://oglobo.globo.com/"
  page = requests.get(url)
  doc = lxml.html.fromstring(page.content)
  manchete_oglobo = doc.xpath('//h1[@class = "teaser__title headline__title"]//a/@href')
  return manchete_oglobo

def link_metropoles():
  url = "https://www.metropoles.com/"
  page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.27 Safari/537.36"})
  doc = lxml.html.fromstring(page.content)
  manchete_metropoles = doc.xpath('//h2[@class= "m-title"]//a/@href')
  return manchete_metropoles
