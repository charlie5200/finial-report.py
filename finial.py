import streamlit as st
import datetime                             # import datetime 標準函式
today = datetime.date.today()               # 使用 datetime.date 取得今天的日期
age = st.text_input ('輸入生日 ( YYYY/MM/DD )：')      # 讓使用者輸入生日，格式為 YYYY/MM/DD
age_list = age.split('/')                   # 將使用者輸入的日期，使用「/」拆成串列

confirm_input = st.button('輸入確認')
if confirm_input:
    year = today.year - int(age_list[0])        # 用今天的年份，減去使用者的生日年份 ( 年份差 )
    month = today.month - int(age_list[1])      # 用今天的月份，減去使用者生日的月份 ( 月份差 )
    if month<0:                                 # 如果月份差的數字小於零，表示生日還沒到
        year = year - 1                         # 再將年份差減少 1 ( 表示跨了一年 )
        month = 12 + month                          # 將月份差改成 12 + 月份差
day_list = [31,28,31,30,31,30,31,31,30,31,30,31]  # 建立一個每個月有多少天的串列
day = today.day - int(age_list[1])          # 用今天的日期，點去使用者生日的日期 ( 月份差 )
if day<0:                                   # 如果月份差的數字小於 0，表示生日還沒到
  month = month - 1                         # 將月份差減少 1
  if month<0:                               # 如果月份差減少後小於 0
    year = year - 1                         # 再將年份差減少 1 ( 表示跨了一年 )
    month = 12 + month                      # 將月份差改成 12 + 月份差
  day = day_list[month] + day       # 將日期差改成該月的天數 + 日期差
  st.write(f'{year} 歲 {month} 個月 {day} 天')
a = [int(i) for i in age.split('/')]   # 將輸入的文字轉換成串列 ( 使用串列生成式 )
s = (a[0]*2+a[1])%3                        # 根據規則公式，計算出 s 的數值
if s==0:                                   # 依據 s 的數值，給予普通、吉、大吉
  st.write('今年運勢:普通')
if s==1:
  st.write('今年運勢:吉')
if s==2:
  st.write('今年運勢:大吉')
