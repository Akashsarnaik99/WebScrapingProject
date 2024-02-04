# project flipkart webscrap
import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
MRP = []
discounts = []
prices = []
sellers = []
ratings = []
reviews = []
categories = []
sub_categories = []
images = []


def showData(link):
    url = link
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'lxml')

    title = soup.find('span', {'class': 'B_NuCI'})
    title = (title.text)

    price = soup.find('div', {'class': '_30jeq3 _16Jk6d'})
    price = (price.string)

    discount = soup.find_all('div', {'class': '_3Ay6Sb _31Dcoz'})
    for i in discount:
        discount = (i.string)
    discount = (discount)

    mrp = soup.find('div', {'class': '_3I9_wc _2p6lqe'})
    mrp = mrp.text

    category = soup.find_all('a', {'class': '_2whKao'})
    category = (category[1].text)

    category1 = soup.find_all('a', {'class': '_2whKao'})
    for i in category1[:4]:
        sub_category = (i.text)
    sub_category = (sub_category)

    rating = soup.find('span', {'class': '_2_R_DZ'})
    for i in rating:
        rating = (i.text)
    rating = rating.split("&")
    rating = (rating[0].split(' '))
    rating=(rating[0])

    review = soup.find_all('span', {'class': '_2_R_DZ'})
    for i in review[:1]:
        review = (i.text)
    review = review.split('&')
    review = review[1].split(' ')
    review = review[0]

    seller = soup.find_all('div', {'class': '_1RLviY'})
    seller = (seller[0].text)
    seller = (seller)

    image = soup.find_all('img', {'class': '_396cs4 _2amPTt _3qGmMb'})
    for i in image:
        img_link = i['src']
    img = (img_link)

    return title, price, discount, mrp, category, sub_category, rating, review, seller, img


d = {
    'url1': 'https://www.flipkart.com/five-o-tempered-glass-guard-iqoo-neo-7-pro-5g-11-5g/p/itme0da61cb33a4c?pid=ACCGNZ6YGDB7K4RR&lid=LSTACCGNZ6YGDB7K4RRESH2L3&marketplace=FLIPKART&store=tyy%2F4mr%2Flrv&srno=b_1_2&otracker=nmenu_sub_Electronics_0_Screenguards&fm=search-autosuggest&iid=en_wLpNO7f-hdVJu1GhTkgFpgYvD1PPcAVDt28t5VCMmSMdnJTiZ41vQTY8nJ90QpevgZm1NWuEhd0ybXSPIFgxVA%3D%3D&ppt=browse&ppn=browse&ssid=s7k1kg8xzcgevj0g1702304814580',
    'url2': 'https://www.flipkart.com/gamloid-capital-alphabets-letters-learning-educational-puzzle-toy-kids/p/itmf7a7f96c08d87?pid=BLCGPZTGBY2W66JG&lid=LSTBLCGPZTGBY2W66JGEM46QZ&marketplace=FLIPKART&store=tng%2Fll1&srno=b_1_2&otracker=nmenu_sub_Baby%20%26%20Kids_0_Educational%20Toys&fm=search-autosuggest&iid=en_z7UcCkIgJVxN2MAwunZFVa5tuTgAJiC1ny1v3K4C6e4BNmQYmcOhX7V675e_SafvjMUmVaYUbgMUPnFtFa_zjg%3D%3D&ppt=browse&ppn=browse&ssid=ogl3kg4hevnjcgzk1702356694966',
    'url3':'https://www.flipkart.com/samsung-crystal-vision-4k-ismart-voice-assistant-138-cm-55-inch-ultra-hd-4k-led-smart-tizen-tv-2023-video-calling-iot-sensors-light-camera/p/itma0ae071154d5a?pid=TVSGRNGZXD8QWSJJ&lid=LSTTVSGRNGZXD8QWSJJGRPQHF&marketplace=FLIPKART&store=ckf%2Fczl&srno=b_1_1&otracker=browse&fm=search-autosuggest&iid=en_kiRQTO1Yvw9aBGFsFFyUT7XvyJ-T8u0FcHbptr2DU9iLYUPpdIootuu4oyRRadBaCrVXeK33Z2k1QDvWn38E1w%3D%3D&ppt=pp&ppn=pp&ssid=k9ow3cotufp472f41702356900389',
    'url4':'https://www.flipkart.com/fresh-up-sofa-cum-bed-jute-fabric-78x36x14-inches-4-cushion-cover-seater-double-foam-fold-out/p/itmc1b106c88f9b1?pid=SBEG7PSDFYMH5W9D&lid=LSTSBEG7PSDFYMH5W9DEWG9GU&marketplace=FLIPKART&store=wwe%2Fosg&srno=b_1_2&otracker=nmenu_sub_Home%20%26%20Furniture_0_Sofa%20Beds&fm=search-autosuggest&iid=en_x5yaLB-8fDXWsJvSyY324zb4hx7HqEjZFDdwF3yDx_47jtGZO5I8rQ1qnG3zkfylD5kYjmQSEPFEEtQs0si2zg%3D%3D&ppt=browse&ppn=browse&ssid=hpe38bfz74erxs741702359986410',
    'url5':'https://www.flipkart.com/old-natural-sandal-twig-mystic-berry-moods-car-freshener/p/itm446e32cd38e28?pid=AIRGRFQHFGMFHYGH&lid=LSTAIRGRFQHFGMFHYGHSMGENP&marketplace=FLIPKART&store=1mt%2Fbpx%2Fbij&srno=b_4_121&otracker=clp_omu_Auto%2BAccessories_4_6.dealCard.OMU_big-saving-days-sale-store_big-saving-days-sale-store_7QNJHV1LZBI6_5&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Auto%2BAccessories_NA_dealCard_cc_4_NA_view-all_5&fm=neo%2Fmerchandising&iid=en_2SLkixS9z2m6HNcrvd4r4T5ifQxo3v8OUVSXsP6lfOKBXQ4AXH9yzHBVf8GXxj6fB8yq2WET4uC13DunN4S0Vg%3D%3D&ppt=browse&ppn=browse&ssid=bzik7khyow2ahgjk1702378180369',
    'url6':'https://www.flipkart.com/rich-dad-poor-20th-anniversary-robert-t-kiyosaki/p/itm62e9ee3f7ade2?pid=9788186775219&lid=LSTBOK9788186775219V4TEN9&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_5bbb71c8-3f21-4c7b-8cc0-1f522583d0c8_3_JU86FN3T7U6E_MC.9788186775219&ppt=browse&ppn=browse&ssid=wqd4s0ziqhidqb5s1702378240210&otracker=clp_pmu_v2_Self%2BHelp%2BBooks_3_3.productCard.PMU_V2_Rich%2BDad%2BPoor%2BDad%2B20th%2BAnniversary%2BEdition%2B%2B-%2BRobert%2BT%2BKiyosaki_the-non-fiction-store_9788186775219_neo%2Fmerchandising_2&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Self%2BHelp%2BBooks_LIST_productCard_cc_3_NA_view-all&cid=9788186775219',
    'url7':'https://www.flipkart.com/kent-ace-8-l-ro-uv-uf-tds-water-purifier-4-year-free-service/p/itm9bf11047176bd?pid=WAPFSJZAEKGQCNZF&lid=LSTWAPFSJZAEKGQCNZFCLIFVL&marketplace=FLIPKART&store=j9e%2Fabm%2Fi45&srno=b_1_4&otracker=nmenu_sub_Appliances_0_Water%20Purifiers&fm=neo%2Fmerchandising&iid=1492012d-9fec-43b6-b8bd-a93e7b255965.WAPFSJZAEKGQCNZF.SEARCH&ppt=clp&ppn=the-non-fiction-store&ssid=hnvvsdt61vkoyzgg1702378389462',
    'url8':'https://www.flipkart.com/leo-natura-inner-lid-5-l-induction-bottom-pressure-cooker/p/itmb260859d9d5ca?pid=PRCGFP5CHNZFSBHG&lid=LSTPRCGFP5CHNZFSBHGXEL3TY&marketplace=FLIPKART&store=upp%2Ftnx%2Fgsl&srno=b_1_2&otracker=nmenu_sub_Home%20%26%20Furniture_0_Pressure%20Cookers&fm=organic&iid=7f5e4061-6033-4d99-9072-5f6ca781b308.PRCGFP5CHNZFSBHG.SEARCH&ppt=browse&ppn=browse&ssid=6tw570cs7xryby801702382995818',
    'url9':'https://www.flipkart.com/redmi-note-12-pro-5g-glacier-blue-128-gb/p/itm8fbee21008560?pid=MOBGH2UVZHHQGRRP&lid=LSTMOBGH2UVZHHQGRRPHJOZCG&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=browse&fm=organic&iid=48c73fc0-a023-4bf3-bf8f-9e8359daab59.MOBGH2UVZHHQGRRP.SEARCH&ppt=hp&ppn=homepage&ssid=bck3d1t2upwknojk1702382930961',
    'url10':'https://www.flipkart.com/samsung-7-5-kg-5-star-air-turbo-drying-semi-automatic-top-load-washing-machine-blue-grey/p/itmecde21cc327fa?pid=WMNGGSK86PGTMGHX&lid=LSTWMNGGSK86PGTMGHXKGVJOS&marketplace=FLIPKART&store=j9e%2Fabm%2F8qx&srno=b_1_3&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Semi%20Automatic%20Top%20Load&fm=neo%2Fmerchandising&iid=472d3e24-6b5f-40c8-aa3c-6ef735976c19.WMNGGSK86PGTMGHX.SEARCH&ppt=pp&ppn=pp&ssid=udgzi3eelodrw83k1702379863948',

}

for i in d:
    link = d.get(i)
    title, price, discount, mrp, category, sub_category, rating, review, seller, img = showData(link)
    titles.append(title)
    prices.append(price)
    discounts.append(discount)
    MRP.append(mrp)
    categories.append(category)
    sub_categories.append(sub_category)
    ratings.append(rating)
    reviews.append(review)
    sellers.append(seller)
    images.append(img)

df = pd.DataFrame({'product_name': titles, 'MRP': MRP, 'discount': discounts, 'price': prices, 'category': categories,
                   'sub_category': sub_categories,
                   'seller': sellers, 'Rating': ratings, 'review': reviews, 'Image': images
                   })
print(df)

df.to_excel('flipkart_scrap.xlsx')
