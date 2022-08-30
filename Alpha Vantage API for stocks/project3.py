import urllib.request
import urllib.parse
import json



def key(api_key: str) -> str:
    key = open(api_key)
    ap_ky = key.readline()
    key.close()
    return ap_ky
    

def stock_info(site_url: str, stock_name: str, api_key: str) -> str:
    query = [('function', 'TIME_SERIES_DAILY'), ('symbol', stock_name), ('apikey', api_key)]
    site = site_url + '/query?' + urllib.parse.urlencode(query)
    return site


def get_result(url: str) -> dict:
    response = None
    
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()


def final(api_key: str, site_url: str, stock_name: str) -> str:
    '''Returns the information provided by the API'''
    
    result = get_result(stock_info(site_url, stock_name, key(api_key)))
    return result


    
    
class true_range:
    def true_range_calc(self, operation: str, info: dict):
        '''This function calculates the true range'''
        lst = operation.split()
        lst2 = [lst[0], float(lst[1][1:]), float(lst[2][1:])]
        return lst2

    
class simple_moving_average:
    
    def moving_average_mp(self, operation: str):
        '''This function calculates simple moving average with closing prices'''
        lst = operation.split()
        num = int(lst[1])
        return lst
    
    def moving_average_mv(self, operation: str):
        '''This function calculates simple moving average with volume'''
        lst = operation.split()
        num = int(lst[1])
        return num


class directional_indicator:
    def directional_indicator_dp(self, operation: str):
        '''This function calculates the directional indicator'''
        lst = operation.split()
        lst3 = [lst[0], int(lst[1]), int(lst[2][1]), int(lst[3][1])]
        return lst3
    
    def directional_indicator_dv(self, operation: str):
        '''This function calculates the directional indicator'''
        lst = operation.split()
        lst3 = [lst[0], int(lst[1]), int(lst[2][1]), int(lst[3][1])]
        return lst3

x = true_range()
y = simple_moving_average()
z = directional_indicator()

def idics(operation: str) -> None:
    lst_splt = operation.split()
        
    if lst_splt[0] == 'TR':
        x.true_range_calc(operation)
    elif lst_splt[0] == 'MP':
        y.moving_average_mp(operation)
    elif lst_splt[0] == 'MV':
        y.moving_average_mv(operation)
    elif lst_splt[0] == 'DP':
        z.directional_indicator_dp(operation)
    elif lst_splt[0] == 'DV':
        z.directional_indicator_dv(operation)



def table(info: dict) -> None:
    '''This function is responsible for returing the output that would be visible on screen'''

    try:
        date_list = []
        final_date_list = []
        
        for item in info['Time Series (Daily)']:
            date_list.append(item)
        date_list.sort()

        for date in date_list:
            if date_start <= date <= date_close:
                final_date_list.append(date)

        print(stock_name)
        print(len(final_date_list))
        print(operation)
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format('Date','Open','High','Low','Volume','Close','Indicator',"Buy?",'Sell?'))
              
                                                                                                           
         
        for date in date_list:
            if date_start <= date <= date_close:
                print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(date, info['Time Series (Daily)'][date]['1. open'],info['Time Series (Daily)'][date]['2. high'],
                                              info['Time Series (Daily)'][date]['3. low'], info['Time Series (Daily)'][date]['4. close'],
                                              info['Time Series (Daily)'][date]['5. volume'], idics(operation)))
                #print('{}       '.format(), end = '')Indicators
                #print('{}       '.format(), end = '')Buy?
                #print('{}')Sell?
                print()
    except HTTPError as e:
        print('FAILED')
        print(e.code)
        if e.code != 200:
            print('NOT200')
        elif e.code == 200:
            print('FORMAT')
        elif final(api_key, site_url, stock_name) is False:
            print('NETWORK')


def run() -> None:
    table(final(api_key, site_url, stock_name))
    
if __name__ == '__main__':
    api_key = input('Enter file path for the API Key ')
    site_url = input('Enter the URL ')
    stock_name = input("Enter the stock symbol ")
    date_start = input("Starting date: YYYY-MM-DD ")
    date_close = input("Closing date: YYYY-MM-DD ")
    operation = input("Enter the operation you want to perform ")
    run()
    
