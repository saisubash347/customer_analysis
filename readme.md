
📊 Raw Data Preview:
   Index  ...                      Website
0      1  ...   http://www.stephenson.com/
1      2  ...        http://www.hobbs.com/
2      3  ...     http://www.lawrence.com/
3      4  ...   http://www.good-lyons.com/
4      5  ...  https://goodwin-ingram.com/

[5 rows x 12 columns] 
```
🧹 Checking for missing values:
Index                0
Customer Id          0
First Name           0
Last Name            0
Company              0
City                 0
Country              0
Phone 1              0
Phone 2              0
Email                0
Subscription Date    0
Website              0
dtype: int64 
```
ℹ️ Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 12 columns):
```
 #   Column             Non-Null Count  Dtype         
---  ------             --------------  -----         
 0   Index              100 non-null    int64         
 1   Customer Id        100 non-null    object        
 2   First Name         100 non-null    object        
 3   Last Name          100 non-null    object        
 4   Company            100 non-null    object        
 5   City               100 non-null    object        
 6   Country            100 non-null    object        
 7   Phone 1            100 non-null    object        
 8   Phone 2            100 non-null    object        
 9   Email              100 non-null    object        
 10  Subscription Date  100 non-null    datetime64[ns]
 11  Website            100 non-null    object
dtypes: datetime64[ns](1), int64(1), object(10)



memory usage: 9.5+ KB
None
```

```



👥 Total Customers: 100
``
🌍 Customers by Country:
Country
Solomon Islands                     4
Saint Vincent and the Grenadines    2
Bulgaria                            2
Oman                                2
Netherlands                         2
                                   ..
United States of America            1
Liechtenstein                       1
Denmark                             1
Tanzania                            1
Honduras                            1
Name: count, Length: 85, dtype: int64 

🏢 Top 5 Companies with Most Customers:
Company
Simon LLC                     2
Rasmussen Group               1
Knight, Abbott and Hubbard    1
Parrish Ltd                   1
Huynh and Sons                1
Name: count, dtype: int64 

📅 Subscriptions per Year:
Year
2020    38
2021    43
2022    19
Name: count, dtype: int64 

📧 Top Email Domains:
Email Domain
colon.com       2
phelps.com      2
bernard.com     1
oconnell.com    1
odonnell.net    1
Name: count, dtype: int64
root@localhost ~/customer_analysis # 
```
