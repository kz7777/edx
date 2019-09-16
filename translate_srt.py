# %%
# import os
import glob
import pysrt
from googletrans import Translator

# %%
files = glob.glob("./*/*/*/*.srt",recursive=True)
print(files[1:3])
test_files = files[1:7]

# %%
# base sample
# text = pysrt.open("./Downloaded/Marketing_Analytics-_Price_and_Promotion_Analytics/05-Module_4-_Analytics_in_Action/01-BERBUSAD2016-V005000-y94V65Yt4BY.en.srt")
# text_w_n = text.text
# text_all = text_w_n.replace("\n","")
# 
# translator = Translator()
# trans_en = translator.translate(text_all,src='en', dest='ja')
# print(trans_en.text)


#%%
#デバッグ用
for i in test_files:
    text = pysrt.open(i)
    text_w_n = text.text
    text_all = text_w_n.replace("\n","")
#    text_all = text_all.encode("cp932", "ignore")
#    text_all = text_all.replace('\xa0',"")
#    text_all = text_all.encode("cp932")
    
    translator = Translator()
    trans_ja = translator.translate(text_all,src='en', dest='ja')
    try:
        with open(i+".txt", "w",encoding="utf-8" ) as f:
            f.write(trans_ja.text)
    except:
        pass
#    print(trans_ja.text)


#%%
for i in files:
    text = pysrt.open(i)
    text_w_n = text.text
    text_all = text_w_n.replace("\n","")
#    text_all = text_all.encode("cp932", "ignore")
#    text_all = text_all.replace('\xa0',"")
#    text_all = text_all.encode("cp932")
    
    translator = Translator()
    try:
        trans_ja = translator.translate(text_all,src='en', dest='ja')
        with open(i+".txt", "w",encoding="utf-8" ) as f:
            f.write(trans_ja.text)
    except:
        pass
#    print(trans_ja.text)

