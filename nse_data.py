# import requests
# import json
# import pandas as pd
#
# tickers = ['ABSA', 'ARM', 'BAT','ARM','BAMB','BAT','BKG','BOC','BRIT','CABL','CARB','CGEN','CIC','COOP','CRWN','CTUM','DCON','DTK','EABL','EGAD','EQTY','EVRD','FAHR','TGH','GLD','HAFR','HBE','HFCK','I&M,''JUB','KAPC','KCB','KEGN','KNRE','KPLC','KPLC-P4','KPLC-P7','KQ','KUKZ','KURV','LBTY','LIMT','LKL','MSC','NBK','NBV','NCBA','NMG','NSE','OCH','ORCH','PORT','SASN','SBIC','SCAN','SCBK','SCOM', 'SGL','SLAM','SMER','TCL','TOTL','TPSE','UCHM','UMME','UNGA','WTK','XPRS']
# df = pd.DataFrame()
# for ticker in tickers:
#     f'df_{ticker}'
#     name = 'df_' +str(ticker)
#     url = f'http://nse-data-api.herokuapp.com/data/{ticker}'
#     response = requests.get(url)
#     data = json.loads(response.text)
#     name = pd.json_normalize(data)
#     pd.set_option('display.max_columns',None)
#     df.merge(name, on='ticker')
#     # print(name.head())
#     # print(df.head)

sales = ["Vauxhall Corsa 2011", "Nissan Note 2014", "Honda Civic 2012", "Vauxhall Corsa 2015", "Vauxhall Mokka 2013", "Hyundai I20 2016"]
for sale in range(0, len(sales)):
    print(sales[sale])

    # Python program to remove to every third element until list becomes empty
    # def removeThirdNumber(int_list):
    # list starts with 0 index
    #     pos = 3 - 1
    #     index = 0
    #     len_list = (len(int_list))
    #
    #     # breaks out once the list becomes empty
    #     while len_list > 0:
    #         index = (
    #                             pos + index) % len_list  # for first iteration 2%3 remainder 2 so element in 2nd index will be deleted and it will be continued untill the list become empty.
    #
    #         # removes and prints the required element
    #         print(int_list.pop(index))
    #         len_list -= 1
    #
    #
    # nums = [1, 2, 3, 4]
    # removeThirdNumber(nums)


# """""""""
# def freq(str):
#
#     """break sgtring into list of words"""
#     str = str.split()
#     str2 = []
#
#     """loop till string values present in list str"""
#     for i in str:
#         """checking duplicacy"""
#         if i not in str2:
#             """insert value in str2"""
#             str2.append(i)
#     for i in range(0, len(str2)):
#         """count the frequency of each word (present in str2) in str and print"""
#         print('Frequency of', str2[i], 'is:', str.count(str2[i]))
#
#     def main():
#         str = 'apple mango orange orange apple quava mango mango'
#         freq(str)
#
#     if __name__=="__main__":
#         print(main())
