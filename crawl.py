from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
#import urllib.request as req

basic_url = 'https://www.yogiyo.co.kr/mobile/#/{number}/'
store_list = [303034,322384,84346,557879,567198,581501,529147,417885,1080034,549637,567227,1081111,1003224,1014497,523072,554635,1000704,1056724,1059569,223184,471590,1071888,1101907,1128292,1037740,321118,1013425,282002,1075369,547320,1039183,1089995,525701,542343,1047218,509000,364026,1051835,470393,534736,471514,368585,505341,301095,1018586,1017833,541103,1097083,554810,313468,535517,536927,77951,328995,496997,1139238,1002890,1007107,248386,514602,1121580,550033,420995,1095258,319053,1002554,1002167,433454,504801,436782,1040995,357844,322238,513927,1127887,452353,513930,513989,304979,1067303,571638,300967,1112063,1005455,1014767,550422,357844,243398,1004185,489697,1104764,1020059,227569,1142449,1001833,1001892,420664,453621,1063745,1049484,79314, 578176, 580464, 524379, 376524, 41679, 376524, 1097864, 253965, 231224, 80287, 382456,1138081,538678,1044912,262185,422978,561858,237355,321825,337667,217204,374044,578879,1005245,412198,543300,513843,1049353,69362,415411,1056964,487664,355616,551690,496327,1134588,259568,322784,386151,375045,296619,365573,376325,81720,366046,536356,451079,1135263,557098,1032508,314501,358081,1115180,1145184,53440,1090773,1135499,487239,1049133,1108679,386158,1084334,1043219,322624,1008596,484486]
#store_list = list(range(10000, 1000000))

# with open('store_list.pickle', 'rb') as handle:
#     store_list = pickle.load(handle)
# print(store_list[:3])
review_data = []
    
for store in store_list:
    try:
        driver = webdriver.Chrome("C:/Users/hw309/Downloads/chromedriver_win32/chromedriver.exe")
        url = basic_url.replace("{number}", str(store))
        driver.implicitly_wait(3)
        driver.get(url)
        driver.set_window_size(1024, 768)
        #driver.execute_script('toggle_tab("review")')
        #driver.implicitly_wait(2)
        #driver.execute_script('get_next_reviews()')
        #driver.implicitly_wait(2)
        html = driver.page_source
        soup = BeautifulSoup(html ,"html.parser")
        reviews = soup.select('ul#review > li.list-group-item')

        for review in reviews:
            
            review_exist = len(review.select('p')) 
            point_exist = len(review.select('span.points'))
            if review_exist and point_exist:
                review_text = review.select('p')[0].get_text()
                
                points = review.select('span.points')
                pt = True
                #pt = 0
                for point in points[:2]:
                    #print(point.get_text())
                    pt = pt and ( int(point.get_text()) == 5)
                    #pt += int(point.get_text())
                print(pt, review_text)
                review_data.append([review_text, int(pt)])
                with open('review_data.pickle', 'wb') as f:
                    pickle.dump(review_data, f)
                    
    except:
        store_list.remove(store)
        with open('store_list.pickle', 'wb') as handle:
            pickle.dump(store_list, handle)
        continue


#print(reviews)
#review > li:nth-child(3) > div:nth-child(2) > div > span.category > span:nth-child(3)
# ul#review > li.list-group-item > p
# span.points
# req = requests.get(url).text
# print(req)
# 
# reviews = soup.select('ul#review')
# print(reviews)