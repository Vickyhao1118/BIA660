# coding: utf-8
###Hao Cheng(10426048)

# In[164]:


from selenium import webdriver
from selenium.webdriver.support.select import Select

# In[165]:


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# In[166]:


import requests
import bs4

# In[167]:


driver = webdriver.Firefox(executable_path=r'geckodriver')

# In[168]:


driver.get('http://www.mlb.com')

# In[169]:


stats_header_bar = driver.find_element_by_css_selector('.megamenu-navbar-overflow__menu-item-link--stats')

# In[170]:


stats_header_bar.click()

# In[171]:


stats_header_bar.click()

# ### Problem_1

# In[172]:


team_bar = driver.find_element_by_css_selector('#st_parent')

# In[173]:


team_bar.click()

# In[174]:


season_2015_bar = driver.find_element_by_css_selector('#st_hitting_season > option:nth-child(4)')

# In[175]:


season_2015_bar.click()

# In[176]:


regular_bar = driver.find_element_by_css_selector('#st_hitting_game_type > option:nth-child(1)')

# In[177]:


regular_bar.click()

# In[178]:


HR_bar = driver.find_element_by_css_selector('th.dg-hr > abbr:nth-child(1)')

# In[179]:


HR_bar.click()

# In[180]:


import pandas as pd

# In[181]:


data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df_home_run = pd.DataFrame(columns=head)

# In[182]:


data = []
table = soup.find('table', attrs={'class': 'stats_table data_grid'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
data

# In[183]:


data
for i in range(30):
    df_home_run.loc[i] = data[i]

df_home_run.drop("", axis=1)

# In[184]:


df_home_run.to_csv('Question_1.csv')

# In[187]:


Most_HR_Team = driver.find_element_by_css_selector(
    '#_475461521503719981 > tbody:nth-child(34) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)').text
Most_HR_Team

# ### Problem_2

# #### a）

# In[188]:


AL_bar = driver.find_element_by_css_selector('#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(4)')

# In[189]:


AL_bar.click()

# In[190]:


Regular_bar = driver.find_element_by_css_selector('#st_hitting_game_type > option:nth-child(1)')

# In[191]:


Regular_bar.click()

# In[192]:


data1_div = driver.find_element_by_id('datagrid')
data1_html = data1_div.get_attribute('innerHTML')
soup1 = bs4.BeautifulSoup(data1_html, "html5lib")
head1 = [t.text.replace("▼", "") for t in soup1.thead.find_all("th")]
df_home1_run = pd.DataFrame(columns=head1)

# In[193]:


data1 = []
table1 = soup1.find('table', attrs={'class': 'stats_table data_grid'})
table_body1 = table1.find('tbody')
rows1 = table_body1.find_all('tr')
for row in rows1:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data1.append([ele for ele in cols if ele])
data1

# In[194]:


data1
for i in range(15):
    df_home1_run.loc[i] = data1[i]

df_home1_run.drop("", axis=1)

# In[195]:


df_home1_run.to_csv('Question_2a_AL.csv')

# In[196]:


import numpy as np

# In[197]:


HR_average_AL = pd.DataFrame(df_home1_run['HR'], dtype=np.float)

# In[198]:


print('the average number of AL is', HR_average_AL['HR'].mean())

# In[199]:


NL_bar = driver.find_element_by_css_selector('#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(6)')

# In[200]:


NL_bar.click()

# In[201]:


Reg_bar = driver.find_element_by_css_selector('#st_hitting_game_type > option:nth-child(1)')

# In[202]:


Reg_bar.click()

# In[203]:


data2_div = driver.find_element_by_id('datagrid')
data2_html = data1_div.get_attribute('innerHTML')
soup2 = bs4.BeautifulSoup(data2_html, "html5lib")
head2 = [t.text.replace("▼", "") for t in soup2.thead.find_all("th")]
df_home2_run = pd.DataFrame(columns=head2)

# In[204]:


data2 = []
table2 = soup2.find('table', attrs={'class': 'stats_table data_grid'})
table_body2 = table2.find('tbody')
rows2 = table_body2.find_all('tr')
for row in rows2:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data2.append([ele for ele in cols if ele])
data2

for i in range(15):
    df_home2_run.loc[i] = data2[i]

df_home2_run.drop("", axis=1)

# In[205]:


df_home2_run.to_csv('Question_2a_NL.csv')

# In[206]:


HR_average_NL = pd.DataFrame(df_home2_run['HR'], dtype=np.float)

# In[207]:


print('the average number of NL is', HR_average_NL['HR'].mean())

# In[208]:


if HR_average_AL['HR'].mean() >= HR_average_NL['HR'].mean():
    print("the greatest average number of American league homeruns is AL:", HR_average_AL['HR'].mean())
else:
    print("the greatest average number of American league homeruns is NL:", HR_average_NL['HR'].mean())

# #### b)

# In[209]:


first_inning = driver.find_element_by_id("st_hitting_hitting_splits")
first_inning_select = Select(first_inning)
first_inning_select.select_by_visible_text('First Inning')

# In[210]:


first_inning.click()

# In[211]:


data3_div = driver.find_element_by_id('datagrid')
data3_html = data3_div.get_attribute('innerHTML')
soup3 = bs4.BeautifulSoup(data3_html, "html5lib")
head3 = [t.text.replace("▼", "") for t in soup3.thead.find_all("th")]
df_home3_run = pd.DataFrame(columns=head3)

# In[212]:


data3 = []
table3 = soup3.find('table', attrs={'class': 'stats_table data_grid'})
table_body3 = table3.find('tbody')
rows3 = table_body3.find_all('tr')
for row in rows3:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data3.append([ele for ele in cols if ele])
data3

for i in range(15):
    df_home3_run.loc[i] = data3[i]

df_home3_run.drop("", axis=1)

# In[213]:


df_home3_run.to_csv('Question_2b_NL.csv')

# In[214]:


HR_inning_average = pd.DataFrame(df_home3_run['HR'], dtype=np.float)

# In[215]:


print('the average number of NL in the first inning is', HR_inning_average['HR'].mean())

# In[216]:


AL_inning = driver.find_element_by_css_selector('#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(4)')

# In[217]:


AL_inning.click()

# In[218]:


data4_div = driver.find_element_by_id('datagrid')
data4_html = data4_div.get_attribute('innerHTML')
soup4 = bs4.BeautifulSoup(data4_html, "html5lib")
head4 = [t.text.replace("▼", "") for t in soup4.thead.find_all("th")]
df_home4_run = pd.DataFrame(columns=head4)

# In[219]:


data4 = []
table4 = soup4.find('table', attrs={'class': 'stats_table data_grid'})
table_body4 = table4.find('tbody')
rows4 = table_body4.find_all('tr')
for row in rows4:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data4.append([ele for ele in cols if ele])
data4

for i in range(15):
    df_home4_run.loc[i] = data4[i]

df_home4_run.drop("", axis=1)

# In[220]:


df_home4_run.to_csv('Question_2b_AL.csv')

# In[221]:


HR_inning2_average = pd.DataFrame(df_home4_run['HR'], dtype=np.float)

# In[222]:


print('the average number of AL in the first inning is', HR_inning2_average['HR'].mean())

# In[223]:


if HR_inning_average['HR'].mean() >= HR_inning2_average['HR'].mean():
    print("the greatest average number of American league homeruns is NL:", HR_inning_average['HR'].mean())
else:
    print("the greatest average number of American league homeruns is AL:", HR_inning2_average['HR'].mean())

# ### Problem_3

# ### a)

# In[225]:


split_bar = driver.find_element_by_css_selector('#st_hitting_hitting_splits > option:nth-child(1)')

# In[226]:


split_bar.click()

# In[142]:


MLB_bar = driver.find_element_by_css_selector('#sp_hitting-1 > fieldset:nth-child(1) > label:nth-child(2)')

# In[143]:


MLB_bar.click()

# In[75]:


season_2017 = driver.find_element_by_css_selector('#sp_hitting_season > option:nth-child(2)')

# In[76]:


season_2017.click()

# In[227]:


player_bar = driver.find_element_by_id('sp_parent')

# In[228]:


player_bar.click()

# In[229]:


Team_bar = driver.find_element_by_css_selector('#sp_hitting_team_id > option:nth-child(20)')

# In[230]:


Team_bar.click()

# In[231]:


AB_bar = driver.find_element_by_css_selector('th.dg-ab > abbr:nth-child(1)')

# In[232]:


AB_bar.click()

# In[257]:


data5_div = driver.find_element_by_id('datagrid')
data5_html = data5_div.get_attribute('innerHTML')
soup5 = bs4.BeautifulSoup(data5_html, "html5lib")
head5 = [t.text.replace("▼", "") for t in soup5.thead.find_all("th")]
df_home5_run = pd.DataFrame(columns=head5)
df_home5a_run = df_home5_run.drop("", axis=1)

# In[258]:


data5 = []
table5 = soup5.find('table', attrs={'class': 'stats_table data_grid'})
table_body5 = table5.find('tbody')
rows5 = table_body5.find_all('tr')
for row in rows5:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data5.append([ele for ele in cols if ele])
data5

for i in range(33):
    df_home5a_run.loc[i] = data5[i]

df_home5a_run

# In[270]:


df_home5a_run.to_csv('Question_3a.csv')

# In[271]:


AVG = df_home5a_run.sort_values(by=['AVG'], ascending=False)
AVG

# In[340]:


Player_name = AVG.iloc[3, 1]
pos = AVG.iloc[3, 4]
print("the player name:", Player_name)
print("the position:", pos)

# ### b)

# In[273]:


RF_bar = driver.find_element_by_id('sp_hitting_position')
RF_bar_select = Select(RF_bar)
RF_bar_select.select_by_visible_text('RF')
RF_bar.click()

# In[290]:


data6_div = driver.find_element_by_id('datagrid')
data6_html = data5_div.get_attribute('innerHTML')
soup6 = bs4.BeautifulSoup(data6_html, "html5lib")
head6 = [t.text.replace("▼", "") for t in soup6.thead.find_all("th")]
df_home6_run = pd.DataFrame(columns=head6)
df_home6a_run = df_home6_run.drop("", axis=1)

# In[293]:


data6 = []
table6 = soup6.find('table', attrs={'class': 'stats_table data_grid'})
table_body6 = table6.find('tbody')
rows6 = table_body6.find_all('tr')
for row in rows6:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data6.append([ele for ele in cols if ele])
data6

for i in range(2):
    df_home6a_run.loc[i] = data6[i]

df_home6a_run

# In[294]:


df_home6a_run.to_csv('Question_3b_RF.csv')

# In[295]:


RF_bar_select.select_by_visible_text('CF')

# In[296]:


data7_div = driver.find_element_by_id('datagrid')
data7_html = data6_div.get_attribute('innerHTML')
soup7 = bs4.BeautifulSoup(data7_html, "html5lib")
head7 = [t.text.replace("▼", "") for t in soup7.thead.find_all("th")]
df_home7_run = pd.DataFrame(columns=head7)
df_home7a_run = df_home7_run.drop("", axis=1)

# In[301]:


data7 = []
table7 = soup7.find('table', attrs={'class': 'stats_table data_grid'})
table_body7 = table7.find('tbody')
rows7 = table_body7.find_all('tr')
for row in rows7:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data7.append([ele for ele in cols if ele])
data7

for i in range(2):
    df_home7a_run.loc[i] = data7[i]

df_home7a_run

# In[302]:


df_home7a_run.to_csv('Question_3b_CF.csv')

# In[303]:


RF_bar_select.select_by_visible_text('LF')

# In[304]:


data8_div = driver.find_element_by_id('datagrid')
data8_html = data8_div.get_attribute('innerHTML')
soup8 = bs4.BeautifulSoup(data8_html, "html5lib")
head8 = [t.text.replace("▼", "") for t in soup8.thead.find_all("th")]
df_home8_run = pd.DataFrame(columns=head8)
df_home8a_run = df_home8_run.drop("", axis=1)

# In[307]:


data8 = []
table8 = soup8.find('table', attrs={'class': 'stats_table data_grid'})
table_body8 = table8.find('tbody')
rows8 = table_body8.find_all('tr')
for row in rows8:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data8.append([ele for ele in cols if ele])
data8

for i in range(2):
    df_home8a_run.loc[i] = data8[i]

df_home8a_run

# In[308]:


df_home8a_run.to_csv('Question_3b_LF.csv')

# In[309]:


RF_AVG = df_home8a_run.sort_values(by=['AVG'], ascending=False)
RF_AVG

# In[339]:


RF_player = RF_AVG.iloc[0, 1]
RF_pos = RF_AVG.iloc[0, 4]
print("the player name:", RF_player)
print("the position:", RF_pos)

# In[311]:


CF_AVG = df_home7a_run.sort_values(by=['AVG'], ascending=False)
CF_AVG

# In[338]:


CF_player = CF_AVG.iloc[0, 1]
CF_pos = CF_AVG.iloc[0, 4]
print("the player name:", CF_player)
print("the position:", CF_pos)

# In[313]:


LF_AVG = df_home8a_run.sort_values(by=['AVG'], ascending=False)
LF_AVG

# In[333]:


LF_player = LF_AVG.iloc[0, 1]
LF_pos = LF_AVG.iloc[0, 4]
print("the player name:", LF_player)
print("the position:", LF_pos)

# In[341]:


max_player = RF_AVG.iloc[0, 1]
max_pos = RF_AVG.iloc[0, 5]
print("the best overall batting average player:", RF_player)
print("the best overall batting average player's position:", RF_pos)

# # Problem_4

# In[316]:


AL_header_bar = driver.find_element_by_css_selector('#sp_hitting-1 > fieldset:nth-child(1) > label:nth-child(4)')

# In[317]:


AL_header_bar.click()

# In[318]:


All_team = driver.find_element_by_css_selector('#sp_hitting_team_id > option:nth-child(1)')

# In[319]:


All_team.click()

# In[320]:


All_position = driver.find_element_by_css_selector('#sp_hitting_position > option:nth-child(1)')

# In[321]:


All_position.click()

# In[322]:


season_2015 = driver.find_element_by_css_selector('#sp_hitting_season > option:nth-child(4)')

# In[323]:


season_2015.click()

# In[325]:


data9_div = driver.find_element_by_id('datagrid')
data9_html = data9_div.get_attribute('innerHTML')
soup9 = bs4.BeautifulSoup(data9_html, "html5lib")
head9 = [t.text.replace("▼", "") for t in soup9.thead.find_all("th")]
df_home9_run = pd.DataFrame(columns=head9)
df_home9a_run = df_home9_run.drop("", axis=1)

# In[326]:


data9 = []
table9 = soup9.find('table', attrs={'class': 'stats_table data_grid'})
table_body9 = table9.find('tbody')
rows9 = table_body9.find_all('tr')
for row in rows9:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data9.append([ele for ele in cols if ele])
data9

for i in range(50):
    df_home9a_run.loc[i] = data9[i]

df_home9a_run

# In[327]:


df_home9a_run.to_csv('Question_4.csv')

# In[330]:


max_AB = df_home9a_run.sort_values(by=['AB'], ascending=False)
max_AB

# In[332]:


AB_player = max_AB.iloc[0, 1]
AB_pos = max_AB.iloc[0, 4]
print("the max_AB player name:", AB_player)
print("the max_AB position:", AB_pos)
