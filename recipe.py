#讀取excel
import pandas as pd
import copy

#產生各類別菜單 drink_flex_message_generate
flex_format ={ #格式
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://images.chinatimes.com/newsphoto/2021-07-08/1024/20210708002855.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": "熟成紅茶",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "中杯$30",
                "weight": "bold",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "180kcl",
                "size": "sm",
                "color": "#AAAAAA",
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "大杯$35",
                "weight": "bold",
                "flex": 0,
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "200kcl",
                "size": "sm",
                "color": "#AAAAAA",
                "align": "end",
                "contents": []
              }
            ]
          }
        ]
      },
      {
        "type": "text",
        "text": "解炸物/燒烤肉類油膩，茶味濃郁帶果香",
        "size": "xxs",
        "color": "#AAAAAA",
        "wrap": True,
        "contents": []
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "中杯$30",
          "text": "熟成紅茶中杯30",
          "data": "tea熟成紅茶中杯30"
        },
        "color": "#F9CB6AFF",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "大杯$35",
          "text": "熟成紅茶大杯35",
          "data": "tea熟成紅茶大杯35"
        },
        "color": "#905C44",
        "style": "primary"
      }

    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "確認",
          "text": "確認",
          "data": "確認"
        },
        "color": "#CDF482E8",
        "style": "secondary"
      }
    ]
  }
}

flex_format1 ={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://images.chinatimes.com/newsphoto/2021-07-08/1024/20210708002855.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": "熟成紅茶",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "中杯$30",
                "weight": "bold",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "180kcl",
                "size": "sm",
                "color": "#AAAAAA",
                "align": "end",
                "contents": []
              }
            ]
          }
        ]
      },
      {
        "type": "text",
        "text": "解炸物/燒烤肉類油膩，茶味濃郁帶果香",
        "size": "xxs",
        "color": "#AAAAAA",
        "wrap": True,
        "contents": []
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "中杯$30",
          "text": "熟成紅茶中杯30",
          "data": "tea熟成紅茶中杯30"
        },
        "color": "#F9CB6AFF",
        "style": "primary"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "確認",
          "text": "確認",
          "data": "確認"
        },
        "color": "#CDF482E8",
        "style": "secondary"
      }
    ]
  }
}





df = pd.read_excel("可不可爬蟲飲料菜單final.xlsx", sheet_name="菜單all")



#紅茶品項輪播清單
flex_carousel_blacktea = {
  "type": "carousel",
  "contents": []}
for i in range(6) : #前六筆為紅茶
    
    if str(df.at[i,"價格2"]) !="nan":
        flex_format["hero"]["url"] = df.at[i,"圖片連結"] #圖片網址
        flex_format["body"]["contents"][0]["text"] = df.at[i,"品名"]   #品名
        #print(df.at[i,"品名"])
        flex_format["body"]["contents"][1]["contents"][0]["contents"][0]["text"] =  df.at[i,"價格1"]  #價格1(中杯)text
        flex_format["body"]["contents"][1]["contents"][0]["contents"][1]["text"] =  df.at[i,"熱量1"]  #熱量1(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][0]["text"] =  df.at[i,"價格2"]  #價格2(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][1]["text"] =  df.at[i,"熱量2"]  #熱量2(中杯)text  
        flex_format["body"]["contents"][2]["text"] = df.at[i,"介紹"]   #介紹
        flex_format["body"]["contents"][3]["action"]["label"] =  df.at[i,"價格1"]  #價格1(中杯)按鈕 
        flex_format["body"]["contents"][3]["action"]["text"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳text
        flex_format["body"]["contents"][3]["action"]["data"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳data
        flex_format["body"]["contents"][4]["action"]["label"] =  df.at[i,"價格2"]  #價格2(大杯)按鈕
        flex_format["body"]["contents"][4]["action"]["text"] =  str(df.at[i,"品名"])+str(df.at[i,"價格2"])   #價格2(大杯)回傳text
        flex_format["body"]["contents"][4]["action"]["data"] =  str(df.at[i,"品名"])+str(df.at[i,"價格2"])  #價格2(大杯)回傳data
        #print(flex_format["body"]["contents"][0]["text"])
        flex_formatcopy = copy.deepcopy(flex_format)
        flex_carousel_blacktea["contents"].append(flex_formatcopy)    

    else :   

        flex_format1["hero"]["url"] = df.at[i,"圖片連結"] #圖片網址
        flex_format1["body"]["contents"][0]["text"] = df.at[i,"品名"]   #品名
        flex_format1["body"]["contents"][1]["contents"][0]["contents"][0]["text"] =  df.at[i,"價格1"]  #價格1(中杯)text
        flex_format1["body"]["contents"][1]["contents"][0]["contents"][1]["text"] =  df.at[i,"熱量1"]  #熱量1(中杯)text
        flex_format1["body"]["contents"][2]["text"] = df.at[i,"介紹"]   #介紹
        flex_format1["body"]["contents"][3]["action"]["label"] =  df.at[i,"價格1"]  #價格1(中杯)按鈕 
        flex_format1["body"]["contents"][3]["action"]["text"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳text
        flex_format1["body"]["contents"][3]["action"]["data"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳data  #價格1(中杯)回傳data
        flex_formatcopy = copy.deepcopy(flex_format1)
        flex_carousel_blacktea["contents"].append(flex_formatcopy)
    
#冬瓜茶+綠茶品項輪播清單
flex_carousel_greentea = {
  "type": "carousel",
  "contents": []}
for i in range(6,12) : #綠茶+冬瓜茶
        flex_format["hero"]["url"] = df.at[i,"圖片連結"] #圖片網址
        flex_format["body"]["contents"][0]["text"] = df.at[i,"品名"]   #品名
        #print(df.at[i,"品名"])
        flex_format["body"]["contents"][1]["contents"][0]["contents"][0]["text"] =  df.at[i,"價格1"]  #價格1(中杯)text
        flex_format["body"]["contents"][1]["contents"][0]["contents"][1]["text"] =  df.at[i,"熱量1"]  #熱量1(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][0]["text"] =  df.at[i,"價格2"]  #價格2(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][1]["text"] =  df.at[i,"熱量2"]  #熱量2(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][0]["text"] =  " "
        flex_format["body"]["contents"][1]["contents"][1]["contents"][1]["text"] =  " "    
        flex_format["body"]["contents"][2]["text"] = df.at[i,"介紹"]   #介紹
        flex_format["body"]["contents"][3]["action"]["label"] =  df.at[i,"價格1"]  #價格1(中杯)按鈕 
        flex_format["body"]["contents"][3]["action"]["text"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳text
        flex_format["body"]["contents"][3]["action"]["data"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳data
        flex_format["body"]["contents"][4]["action"]["label"] =  df.at[i,"價格2"]  #價格2(大杯)按鈕
        flex_format["body"]["contents"][4]["action"]["text"] =  str(df.at[i,"品名"])+str(df.at[i,"價格2"])   #價格2(大杯)回傳text
        flex_format["body"]["contents"][4]["action"]["data"] =  str(df.at[i,"品名"])+str(df.at[i,"價格2"])  #價格2(大杯)回傳data

        flex_formatcopy = copy.deepcopy(flex_format)
        flex_carousel_greentea["contents"].append(flex_formatcopy)    

#歐蕾品項輪播清單
flex_carousel_ole = {
  "type": "carousel",
  "contents": []}
for i in range(12,15) : #歐蕾
    
    if df.at[i,"價格2"] != "nan" :
        flex_format["hero"]["url"] = df.at[i,"圖片連結"] #圖片網址
        flex_format["body"]["contents"][0]["text"] = df.at[i,"品名"]   #品名
        #print(df.at[i,"品名"])
        flex_format["body"]["contents"][1]["contents"][0]["contents"][0]["text"] =  df.at[i,"價格1"]  #價格1(中杯)text
        flex_format["body"]["contents"][1]["contents"][0]["contents"][1]["text"] =  df.at[i,"熱量1"]  #熱量1(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][0]["text"] =  df.at[i,"價格2"]  #價格2(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][1]["text"] =  df.at[i,"熱量2"]  #熱量2(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][0]["text"] =  " "
        flex_format["body"]["contents"][1]["contents"][1]["contents"][1]["text"] =  " "    
        flex_format["body"]["contents"][2]["text"] = df.at[i,"介紹"]   #介紹
        flex_format["body"]["contents"][3]["action"]["label"] =  df.at[i,"價格1"]  #價格1(中杯)按鈕 
        flex_format["body"]["contents"][3]["action"]["text"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳text
        flex_format["body"]["contents"][3]["action"]["data"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳data
        flex_format["body"]["contents"][4]["action"]["label"] =  df.at[i,"價格2"]  #價格2(大杯)按鈕
        flex_format["body"]["contents"][4]["action"]["text"] =  str(df.at[i,"品名"])+str(df.at[i,"價格2"])   #價格2(大杯)回傳text
        flex_format["body"]["contents"][4]["action"]["data"] =  str(df.at[i,"品名"])+str(df.at[i,"價格2"])  #價格2(大杯)回傳data

        flex_formatcopy = copy.deepcopy(flex_format)
        flex_carousel_ole["contents"].append(flex_formatcopy)   

#限定品項輪播清單
flex_carousel_seasonal = {
  "type": "carousel",
  "contents": []}
for i in range(15,20) : #限定
    
    if df.at[i,"價格2"] != "nan" :
        flex_format["hero"]["url"] = df.at[i,"圖片連結"] #圖片網址
        flex_format["body"]["contents"][0]["text"] = df.at[i,"品名"]   #品名
        #print(df.at[i,"品名"])
        flex_format["body"]["contents"][1]["contents"][0]["contents"][0]["text"] =  df.at[i,"價格1"]  #價格1(中杯)text
        flex_format["body"]["contents"][1]["contents"][0]["contents"][1]["text"] =  df.at[i,"熱量1"]  #熱量1(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][0]["text"] =  df.at[i,"價格2"]  #價格2(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][1]["text"] =  df.at[i,"熱量2"]  #熱量2(中杯)text
        flex_format["body"]["contents"][1]["contents"][1]["contents"][0]["text"] =  " "
        flex_format["body"]["contents"][1]["contents"][1]["contents"][1]["text"] =  " "    
        flex_format["body"]["contents"][2]["text"] = df.at[i,"介紹"]   #介紹
        flex_format["body"]["contents"][3]["action"]["label"] =  df.at[i,"價格1"]  #價格1(中杯)按鈕 
        flex_format["body"]["contents"][3]["action"]["text"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳text
        flex_format["body"]["contents"][3]["action"]["data"] =  str(df.at[i,"品名"])+str(df.at[i,"價格1"])   #價格1(中杯)回傳data
        flex_format["body"]["contents"][4]["action"]["label"] =  df.at[i,"價格2"]  #價格2(大杯)按鈕
        flex_format["body"]["contents"][4]["action"]["text"] =  str(df.at[i,"品名"])+str(df.at[i,"價格2"])   #價格2(大杯)回傳text
        flex_format["body"]["contents"][4]["action"]["data"] =  str(df.at[i,"品名"])+str(df.at[i,"價格2"])  #價格2(大杯)回傳data
        
        flex_formatcopy = copy.deepcopy(flex_format)
        flex_carousel_seasonal["contents"].append(flex_formatcopy)    
