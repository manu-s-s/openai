import pandas as pd
from datetime import datetime
from  io import StringIO
def diff_days(csv_contents):
    contents=pd.read_csv(StringIO(csv_contents))
    return (datetime.strptime(max(contents['Date']),'%Y-%m-%d')-datetime.strptime(min(contents['Date']),'%Y-%m-%d')).days
   
print(diff_days("""Date,Price,Volume
2014-01-27,550.50,1387
2014-06-23,910.83,4361
2014-05-20,604.51,5870"""))