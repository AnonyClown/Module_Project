import netifaces

def get_gateway_address():
	return netifaces.gateways()['default'][2][0]

HOST = get_gateway_address()
PORT = 3306
USER = "root"
PASSWD = "rootpass"
CHARSET = "utf8"
DB_NAME = 'travel'
TABLE_NAME = ['countries_location', 'status']
COUNTRY_NAME = ['뉴질랜드', '러시아', '미국', '영국', '우즈베키스탄', '유럽 (EU 가입국)', 
            '캐나다', '호주', '대만', '일본', '중국', '홍콩', '말레이시아', '미얀마', 
            '베트남', '싱가포르', '인도네시아', '캄보디아', '태국', '필리핀', '대한민국']
EUROPE_NAME = ['그리스','네덜란드','덴마크','독일','라트비아','루마니아','룩셈부르크',
            '리투아니아','몰타','벨기에','불가리아','스웨덴','스페인','슬로바키아','슬로베니아',
            '아일랜드','에스토니아','오스트리아','이탈리아','체코','크로아티아','키프로스',
            '포르투갈','폴란드','프랑스','핀란드','헝가리']
