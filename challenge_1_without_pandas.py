from datetime import datetime
import csv
from  io import StringIO
# def diff_days(csv_contents):
#     contents=csv.reader(StringIO(csv_contents))
#     contents=[row[0] for row in contents]
#     contents.remove('Date')
#     print(max(contents))
#     return (datetime.strptime(max(contents),'%Y-%m-%d')-datetime.strptime(min(contents),'%Y-%m-%d')).days
   
# print(diff_days("""Date,Price,Volume
# 2014-01-27,550.50,1387
# 2014-06-23,910.83,4361
# 2014-05-20,604.51,5870"""))
with open(r'C:\Users\Manu\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\master_combined.csv','r') as file:
    contents=csv.reader(file)
    contents=[row[4] for row in contents if row[4] not in ['Order Date','']]
    print(max(contents))
    print(min(contents))
    print((datetime.strptime(max(contents),'%m/%d/%y %H:%M')-datetime.strptime(min(contents),'%m/%d/%y %H:%M')).days)
