# coding: utf-8
## Hao Cheng(10426048)

# In[1]:

from selenium import webdriver
from selenium.webdriver.support.select import Select

# In[2]:

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# In[3]:

import requests
import bs4

# In[71]:

driver = webdriver.Firefox(executable_path=r'geckodriver')

# In[72]:

driver.get('http://www.mlb.com')

# In[6]:

stats_header_bar = driver.find_element_by_css_selector('.megamenu-navbar-overflow__menu-item-link--stats')

# In[7]:

stats_header_bar.click()

# In[8]:

stats_header_bar.click()

# ### Problem_1

# In[9]:

team_bar = driver.find_element_by_css_selector('li.right_border:nth-child(5)')

# In[10]:

team_bar.click()

# In[11]:

season_2015_bar = driver.find_element_by_css_selector('#st_hitting_season > option:nth-child(4)')

# In[12]:

season_2015_bar.click()

# In[13]:

regular_bar = driver.find_element_by_css_selector('#st_hitting_game_type > option:nth-child(1)')

# In[14]:

regular_bar.click()

# In[15]:

HR_bar = driver.find_element_by_css_selector('th.dg-hr > abbr:nth-child(1)')

# In[16]:

HR_bar.click()

# In[17]:

import pandas as pd

# In[18]:

data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df_home_run = pd.DataFrame(columns=head)

# In[19]:

context_table_q1 = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q1.append(a.text)
context_table_q1

# In[20]:

context_table_q1_prettify = []
for i in range(int(len(context_table_q1) / len(head))):
    s = context_table_q1[i * len(head):(i + 1) * len(head)]
    context_table_q1_prettify.append(s)

# In[21]:

context_table_q1_prettify
for i in range(30):
    df_home_run.loc[i] = context_table_q1_prettify[i]

df_home_run.drop("", axis=1)

# In[22]:

df_home_run.to_csv('Question_1.csv')

# In[24]:

Most_HR_Team = driver.find_element_by_css_selector(
    '#_386451520446224440 > tbody:nth-child(34) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)').text
Most_HR_Team

# ### Problem_2

# #### a）

# In[25]:

AL_bar = driver.find_element_by_css_selector('#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(4)')

# In[26]:

AL_bar.click()

# In[27]:

Regular_bar = driver.find_element_by_css_selector('#st_hitting_game_type > option:nth-child(1)')

# In[28]:

Regular_bar.click()

# In[29]:

data1_div = driver.find_element_by_id('datagrid')
data1_html = data1_div.get_attribute('innerHTML')
soup1 = bs4.BeautifulSoup(data1_html, "html5lib")
head1 = [t.text.replace("▼", "") for t in soup1.thead.find_all("th")]
df_home1_run = pd.DataFrame(columns=head1)

# In[30]:

context_table_q2 = []
for t in soup1.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q2.append(a.text)
context_table_q2

# In[31]:

context_table_q2_prettify = []
for i in range(int(len(context_table_q2) / len(head))):
    s = context_table_q2[i * len(head):(i + 1) * len(head)]
    context_table_q2_prettify.append(s)

# In[32]:

context_table_q2_prettify
for i in range(15):
    df_home1_run.loc[i] = context_table_q2_prettify[i]

df_home1_run.drop("", axis=1)

# In[33]:

df_home1_run.to_csv('Question_2a_AL.csv')

# In[34]:

import numpy as np

# In[35]:

HR_average_AL = pd.DataFrame(df_home1_run['HR'], dtype=np.float)

# In[36]:

print('the average number of AL is', HR_average_AL['HR'].mean())

# In[37]:

NL_bar = driver.find_element_by_css_selector('#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(6)')

# In[38]:

NL_bar.click()

# In[39]:

Reg_bar = driver.find_element_by_css_selector('#st_hitting_game_type > option:nth-child(1)')

# In[40]:

Reg_bar.click()

# In[41]:

data2_div = driver.find_element_by_id('datagrid')
data2_html = data1_div.get_attribute('innerHTML')
soup2 = bs4.BeautifulSoup(data2_html, "html5lib")
head2 = [t.text.replace("▼", "") for t in soup2.thead.find_all("th")]
df_home2_run = pd.DataFrame(columns=head2)

# In[42]:

context_table_q3 = []
for t in soup2.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q3.append(a.text)
context_table_q3

# In[43]:

context_table_q3_prettify = []
for i in range(int(len(context_table_q3) / len(head))):
    s = context_table_q3[i * len(head):(i + 1) * len(head)]
    context_table_q3_prettify.append(s)

# In[44]:

context_table_q3_prettify
for i in range(15):
    df_home2_run.loc[i] = context_table_q3_prettify[i]

df_home2_run.drop("", axis=1)

# In[45]:

df_home2_run.to_csv('Question_2a_NL.csv')

# In[46]:

HR_average_NL = pd.DataFrame(df_home2_run['HR'], dtype=np.float)

# In[47]:

print('the average number of NL is', HR_average_NL['HR'].mean())

# In[48]:

if HR_average_AL['HR'].mean() >= HR_average_NL['HR'].mean():
    print("the greatest average number of American league homeruns is AL:", HR_average_AL['HR'].mean())
else:
    print("the greatest average number of American league homeruns is NL:", HR_average_NL['HR'].mean())

# #### b)

# In[49]:

first_inning = driver.find_element_by_id("st_hitting_hitting_splits")
first_inning_select = Select(first_inning)
first_inning_select.select_by_visible_text('First Inning')

# In[50]:

first_inning.click()

# In[51]:

data3_div = driver.find_element_by_id('datagrid')
data3_html = data3_div.get_attribute('innerHTML')
soup3 = bs4.BeautifulSoup(data3_html, "html5lib")
head3 = [t.text.replace("▼", "") for t in soup3.thead.find_all("th")]
df_home3_run = pd.DataFrame(columns=head3)

# In[52]:

context_table_q4 = []
for t in soup3.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q4.append(a.text)
context_table_q4

# In[53]:

context_table_q4_prettify = []
for i in range(int(len(context_table_q4) / len(head))):
    s = context_table_q4[i * len(head):(i + 1) * len(head)]
    context_table_q4_prettify.append(s)

# In[54]:

context_table_q4_prettify
for i in range(15):
    df_home3_run.loc[i] = context_table_q4_prettify[i]

df_home3_run.drop("", axis=1)

# In[55]:

df_home3_run.to_csv('Question_2b_NL.csv')

# In[56]:

HR_inning_average = pd.DataFrame(df_home3_run['HR'], dtype=np.float)

# In[57]:

print('the average number of NL in the first inning is', HR_inning_average['HR'].mean())

# In[58]:

AL_inning = driver.find_element_by_css_selector('#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(4)')

# In[59]:

AL_inning.click()

# In[60]:

data4_div = driver.find_element_by_id('datagrid')
data4_html = data4_div.get_attribute('innerHTML')
soup4 = bs4.BeautifulSoup(data4_html, "html5lib")
head4 = [t.text.replace("▼", "") for t in soup4.thead.find_all("th")]
df_home4_run = pd.DataFrame(columns=head4)

# In[61]:

context_table_q5 = []
for t in soup4.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q5.append(a.text)
context_table_q5

# In[62]:

context_table_q5_prettify = []
for i in range(int(len(context_table_q5) / len(head))):
    s = context_table_q5[i * len(head):(i + 1) * len(head)]
    context_table_q5_prettify.append(s)

# In[63]:

context_table_q5_prettify
for i in range(15):
    df_home4_run.loc[i] = context_table_q5_prettify[i]

df_home4_run.drop("", axis=1)

# In[64]:

df_home4_run.to_csv('Question_2b_AL.csv')

# In[65]:

HR_inning2_average = pd.DataFrame(df_home4_run['HR'], dtype=np.float)

# In[66]:

print('the average number of AL in the first inning is', HR_inning2_average['HR'].mean())

# In[67]:

if HR_inning_average['HR'].mean() >= HR_inning2_average['HR'].mean():
    print("the greatest average number of American league homeruns is NL:", HR_inning_average['HR'].mean())
else:
    print("the greatest average number of American league homeruns is AL:", HR_inning2_average['HR'].mean())

# ### Problem_3

# ### a)

# In[68]:

splits_bar = driver.find_element_by_id('st_hitting_hitting_splits')
splits_bar_select = Select(splits_bar)
splits_bar_select.select_by_visible_text('Select Split')

# In[73]:

MLB_bar = driver.find_element_by_css_selector('#sp_hitting-1 > fieldset:nth-child(1) > label:nth-child(2)')

# In[74]:

MLB_bar.click()

# In[75]:

season_2017 = driver.find_element_by_css_selector('#sp_hitting_season > option:nth-child(2)')

# In[76]:

season_2017.click()

# In[77]:

player_bar = driver.find_element_by_id('sp_parent')

# In[78]:

player_bar.click()

# In[79]:

Team_bar = driver.find_element_by_css_selector('#sp_hitting_team_id > option:nth-child(20)')

# In[80]:

Team_bar.click()

# In[81]:

AB_bar = driver.find_element_by_css_selector('th.dg-ab > abbr:nth-child(1)')

# In[82]:

AB_bar.click()

# In[89]:

data5_div = driver.find_element_by_id('datagrid')
data5_html = data5_div.get_attribute('innerHTML')
soup5 = bs4.BeautifulSoup(data5_html, "html5lib")
head5 = [t.text.replace("▼", "") for t in soup5.thead.find_all("th")]
df_home5_run = pd.DataFrame(columns=head5)
df_home5_run

# In[84]:

context_table_q6 = []
for t in soup5.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q6.append(a.text)
context_table_q6

# In[91]:

context_table_q6_prettify = []
for i in range(int(len(context_table_q6) / len(head5))):
    s = context_table_q6[i * len(head5):(i + 1) * len(head5)]
    context_table_q6_prettify.append(s)
len(context_table_q6_prettify)

# In[92]:

context_table_q6_prettify
for i in range(33):
    df_home5_run.loc[i] = context_table_q6_prettify[i]

df_home5_run.drop("", axis=1)

# In[96]:

df_home5_run.to_csv('Question_3a.csv')

# In[95]:

AVG = df_home5_run.sort_values(by=['AVG'], ascending=False)
AVG

# In[99]:

Player_name = AVG.iloc[3, 1]
pos = AVG.iloc[3, 5]
print("the player name:", Player_name)
print("the position:", pos)

# ### b)

# In[135]:

RF_bar = driver.find_element_by_id('sp_hitting_position')
RF_bar_select = Select(RF_bar)
RF_bar_select.select_by_visible_text('RF')
RF_bar.click()

# In[136]:

data6_div = driver.find_element_by_id('datagrid')
data6_html = data5_div.get_attribute('innerHTML')
soup6 = bs4.BeautifulSoup(data6_html, "html5lib")
head6 = [t.text.replace("▼", "") for t in soup6.thead.find_all("th")]
df_home6_run = pd.DataFrame(columns=head6)
df_home6_run

# In[137]:

context_table_q7 = []
for t in soup6.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q7.append(a.text)
context_table_q7

# In[141]:

context_table_q7_prettify = []
for i in range(int(len(context_table_q7) / len(head6))):
    s = context_table_q7[i * len(head6):(i + 1) * len(head6)]
    context_table_q7_prettify.append(s)
context_table_q7_prettify

# In[142]:

context_table_q7_prettify
for i in range(2):
    df_home6_run.loc[i] = context_table_q7_prettify[i]

df_home6_run.drop("", axis=1)

# In[143]:

df_home6_run.to_csv('Question_3b_RF.csv')

# In[144]:

RF_bar_select.select_by_visible_text('CF')

# In[145]:

data7_div = driver.find_element_by_id('datagrid')
data7_html = data6_div.get_attribute('innerHTML')
soup7 = bs4.BeautifulSoup(data7_html, "html5lib")
head7 = [t.text.replace("▼", "") for t in soup7.thead.find_all("th")]
df_home7_run = pd.DataFrame(columns=head7)
df_home7_run

# In[146]:

context_table_q8 = []
for t in soup7.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q8.append(a.text)
context_table_q8

# In[147]:

context_table_q8_prettify = []
for i in range(int(len(context_table_q8) / len(head7))):
    s = context_table_q8[i * len(head7):(i + 1) * len(head7)]
    context_table_q8_prettify.append(s)
len(context_table_q8_prettify)

# In[148]:

context_table_q8_prettify
for i in range(3):
    df_home7_run.loc[i] = context_table_q8_prettify[i]

df_home7_run.drop("", axis=1)

# In[149]:

df_home7_run.to_csv('Question_3b_CF.csv')

# In[150]:

RF_bar_select.select_by_visible_text('LF')

# In[151]:

data8_div = driver.find_element_by_id('datagrid')
data8_html = data8_div.get_attribute('innerHTML')
soup8 = bs4.BeautifulSoup(data8_html, "html5lib")
head8 = [t.text.replace("▼", "") for t in soup8.thead.find_all("th")]
df_home8_run = pd.DataFrame(columns=head8)
df_home8_run

# In[152]:

context_table_q9 = []
for t in soup8.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q9.append(a.text)
context_table_q9

# In[153]:

context_table_q9_prettify = []
for i in range(int(len(context_table_q9) / len(head8))):
    s = context_table_q9[i * len(head8):(i + 1) * len(head8)]
    context_table_q9_prettify.append(s)
len(context_table_q9_prettify)

# In[154]:

context_table_q9_prettify
for i in range(2):
    df_home8_run.loc[i] = context_table_q9_prettify[i]

df_home8_run.drop("", axis=1)

# In[155]:

df_home8_run.to_csv('Question_3b_LF.csv')

# In[156]:

RF_AVG = df_home6_run.sort_values(by=['AVG'], ascending=False)
RF_AVG

# In[161]:

RF_player = RF_AVG.iloc[0, 1]
RF_pos = RF_AVG.iloc[0, 5]
print("the player name:", RF_player)
print("the position:", RF_pos)

# In[162]:

CF_AVG = df_home7_run.sort_values(by=['AVG'], ascending=False)
CF_AVG

# In[163]:

CF_player = CF_AVG.iloc[0, 1]
CF_pos = CF_AVG.iloc[0, 5]
print("the player name:", CF_player)
print("the position:", CF_pos)

# In[164]:

LF_AVG = df_home8_run.sort_values(by=['AVG'], ascending=False)
LF_AVG

# In[165]:

LF_player = LF_AVG.iloc[0, 1]
LF_pos = LF_AVG.iloc[0, 5]
print("the player name:", LF_player)
print("the position:", LF_pos)

# In[169]:

max_player = RF_AVG.iloc[0, 1]
max_pos = RF_AVG.iloc[0, 5]
print("the best overall batting average player:", RF_player)
print("the best overall batting average player's position:", RF_pos)

# # Problem_4

# In[170]:

AL_header_bar = driver.find_element_by_css_selector('#sp_hitting-1 > fieldset:nth-child(1) > label:nth-child(4)')

# In[171]:

AL_header_bar.click()

# In[172]:

All_team = driver.find_element_by_css_selector('#sp_hitting_team_id > option:nth-child(1)')

# In[173]:

All_team.click()

# In[174]:

All_position = driver.find_element_by_css_selector('#sp_hitting_position > option:nth-child(1)')

# In[175]:

All_position.click()

# In[176]:

season_2015 = driver.find_element_by_css_selector('#sp_hitting_season > option:nth-child(4)')

# In[177]:

season_2015.click()

# In[178]:

data9_div = driver.find_element_by_id('datagrid')
data9_html = data9_div.get_attribute('innerHTML')
soup9 = bs4.BeautifulSoup(data9_html, "html5lib")
head9 = [t.text.replace("▼", "") for t in soup9.thead.find_all("th")]
df_home9_run = pd.DataFrame(columns=head9)
df_home9_run

# In[179]:

context_table_q10 = []
for t in soup9.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q10.append(a.text)
context_table_q10

# In[180]:

context_table_q10_prettify = []
for i in range(int(len(context_table_q10) / len(head9))):
    s = context_table_q10[i * len(head9):(i + 1) * len(head9)]
    context_table_q10_prettify.append(s)
len(context_table_q10_prettify)

# In[181]:

context_table_q10_prettify
for i in range(50):
    df_home9_run.loc[i] = context_table_q10_prettify[i]

df_home9_run.drop("", axis=1)

# In[182]:

df_home9_run.to_csv('Question_4.csv')

# In[183]:

max_AB = df_home9_run.sort_values(by=['AB'], ascending=False)
max_AB

# In[184]:

AB_player = max_AB.iloc[0, 1]
AB_pos = max_AB.iloc[0, 5]
print("the max_AB player name:", AB_player)
print("the max_AB position:", AB_pos)
