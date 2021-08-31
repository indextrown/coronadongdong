import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/item/main.nhn?code=005930")

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

soup.select('.wrap_company > h2')[0].text    #종목:삼성전자 크롤링

soup.select('td.first > em > span.blind')[0].text #전일가

soup.select('em.no_up > span')[0].text  #고가

soup.select('em.no_down > span')[0].text  #저가

soup.select('em.no_up > span.blind')[0].text  #현재가

soup.select('em.no_up > span.ico.up')[0].text #상승 or 하락

soup.select('em.no_up > span.blind')[1].text  # 전일대비

soup.select('#_market_sum')[0].text    #시가총액

