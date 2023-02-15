import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


# 정보를 담을 빈 list 생성
list_brand = []
list_name = []
list_price = []
list_img = []

# for문을 이용해서 원하는 페이지에 접근, 정보 추출 후 리스트에 담기
for page_num in range(120):
    # range를 이용하면 0부터 인덱스가 시작되므로 page_num에 1을 더해준 url을 이용
    url = f'https://www.hfashionmall.com/display/category/list?dspCtgryNo=HFMA02&cateCd=HFMA02&currentPage={page_num+1}&sortColumn=NEW_GOD_SEQ&cateNos=&lCateFilter=&mCateFilter=&sCateFilter=&dCateFilter=&brandId=&brndId=&price=&rate=&size=&color=&matr=&modelCut=&exceptSoldout=&mallGubun=CTGRY&otltYn='
    
    # html 정보 받아와서 파싱
    response = requests.get(url)
    soup = bs(response.text , 'html.parser')
    
    # css selector로 페이지 내의 원하는 정보 가져오기
    html_brand = soup.select('figure.item-box > figcaption.item-info > a > div.item-brand')
    html_name = soup.select('figure.item-box > figcaption.item-info > a > div.item-name')
    html_price = soup.select('figure.item-box > figcaption.item-info > a > div.item-price > span.price')
    img = soup.select('figure.item-box > div.item-img > div.img-box > a > div.img > img')

    # 텍스트만 추출
    for i in html_brand:
        brands = i.get_text()
        list_brand.append(brands)
        
    for i in html_name:
        names = i.get_text()
        list_name.append(names)
        
    for i in html_price:
        prices = i.get_text()
        list_price.append(prices)
        
    for i in img:
        imgs = i['src']
        list_img.append(imgs)
        
        
# zip 모듈을 이용해서 list를 묶어주기        
list_sum = list(zip(list_brand, list_name, list_price, list_img))

col = ['브랜드','제품명','가격','이미지링크']
df_hfashion = pd.DataFrame(list_sum, columns=col)

df_hfashion.to_csv("h_fashion.csv", encoding = "utf-8-sig")