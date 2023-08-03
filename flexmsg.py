from linebot.models import FlexSendMessage, TextSendMessage,ImageSendMessage,ConfirmTemplate,TemplateSendMessage
from collections import Counter
import pandas as pd
#選擇大分類
flex_message = FlexSendMessage(
    alt_text='RECEIPT',
    contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://images.deliveryhero.io/image/fd-tw/LH/ml5z-hero.jpg?width=1600&height=400&quality=45",
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
        "text": "可不可熟成紅茶",
        "weight": "bold",
        "size": "xl",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "紅茶系列",
            "weight": "bold",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "紅茶",
              "text": "紅茶系列",
              "data": "紅茶"
            },
            "color": "#905C44",
            "style": "primary"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "綠茶+冬瓜茶系列",
            "weight": "bold",
            "flex": 0,
            "margin": "sm",
            "contents": []
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "綠茶 冬瓜茶",
              "text": "綠茶冬瓜茶",
              "data": "綠茶冬瓜茶"
            },
            "color": "#36E229FF",
            "style": "primary"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "歐蕾系列",
            "weight": "bold",
            "contents": []
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "歐蕾",
              "text": "歐蕾系列",
              "data": "歐蕾"
            },
            "color": "#F9CB6AFF",
            "style": "primary"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "期間限定",
            "weight": "bold",
            "contents": []
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "期間限定",
              "text": "期間限定",
              "data": "期間限定"
            },
            "color": "#EB8A12FF",
            "style": "primary"
          }
        ]
      }
    ]
  }
})


#冰塊
ice_flex_message = FlexSendMessage(
    alt_text="冰塊",
    contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "borderColor": "#C7BC07FF",
    "contents": [
      {
        "type": "text",
        "text": "選擇冰塊",
        "weight": "bold",
        "size": "lg",
        "color": "#E34E4EFF",
        "align": "center",
        "contents": []
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://cdn0-manfashion.techbang.com/system/images/71757/medium/9a21683b0b08ffad4c5cce83db0eb22c.jpg?1522734722",
    "align": "center",
    "size": "5xl",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit"
  },
  "body": {
    "type": "box",
    "layout": "baseline",
    "contents": [
      {
        "type": "text",
        "text": "Ice level",
        "weight": "bold",
        "size": "lg",
        "color": "#C5B83CFF",
        "align": "center",
        "contents": []
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
          "label": "熱",
          "text": "熱",
          "data": "熱 冰"
        },
        "color": "#D77777FF",
        "margin": "md"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "去冰",
          "text": "去冰",
          "data": "去冰"
        },
        "color": "#E9E162FF",
        "margin": "md"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "微冰",
          "text": "微冰",
          "data": "微冰"
        },
        "color": "#C0D543FF",
        "margin": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "少冰",
          "text": "少冰",
          "data": "少冰"
        },
        "color": "#66D3B2FF",
        "margin": "md"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "正常冰",
          "text": "正常冰",
          "data": "正常冰"
        },
        "color": "#7ECFF7FF",
        "margin": "md"
      }
    ]
  }
}
)


#甜度
sugar_flex_message = FlexSendMessage(
    alt_text="甜度",
    contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "選擇甜度",
        "weight": "bold",
        "size": "lg",
        "color": "#E34E4EFF",
        "align": "center",
        "margin": "sm",
        "contents": []
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://cdn0-manfashion.techbang.com/system/images/71757/medium/9a21683b0b08ffad4c5cce83db0eb22c.jpg?1522734722",
    "size": "5xl",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Sweetness level",
        "weight": "bold",
        "size": "lg",
        "color": "#C5B83CFF",
        "align": "center",
        "contents": []
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "無糖",
          "text": "無糖",
          "data": "無糖"
        },
        "color": "#51CCF3FF"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "微糖",
          "text": "微糖",
          "data": "微糖"
        },
        "color": "#D1D529FF"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "半糖",
          "text": "半糖",
          "data": "半糖"
        },
        "color": "#F7A8A8FF"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "全糖",
          "text": "全糖",
          "data": "全糖"
        },
        "color": "#B6ECB6FF"
      }
    ]
  }
}
)


#確認
def confirm_template_generator(x): # x<-lista
  confirm_template_message = TemplateSendMessage(
      alt_text='Confirm template',
      template=ConfirmTemplate(
          text=x[0]+"\n飲料:"+x[2]+"\n"+"冰塊:"+x[3]+"\n"+"甜度:"+x[4],
          actions=[
              {
          "type": "postback",
          "label": "是",
          "text": "是",
          "data": "確認點餐"
        },
        {
          "type": "postback",
          "label": "否",
          "text": "否，重新點餐\n(再次點餐請輸入'點餐')",
          "data": "重新點餐"
        }
          ]
      )
  )
  return confirm_template_message


#結單統計 (最終輸出格式)
def orderall(all,connector):
    global alldf
    alldf = pd.DataFrame(all)
    alldf = alldf.T
    alldf = alldf.sort_values([2],ascending=1)

    t=""
    total_price=0

    for i in range(alldf.shape[1]) :
        for j in range(alldf.shape[0]):
            if alldf[i][j] == "0":
                alldf[i][j] = np.NaN

    new_df = alldf.dropna()
    
    mongo_df = new_df.to_dict("records")
    for i in mongo_df :#每一筆資料
        # 處理key名稱
        i.update({"costumer":i.pop(0),"tea":i.pop(2),"ice_level":i.pop(3),"sugar_level":i.pop(4)})
        i.update({"price":i["tea"][i["tea"].find("$")+1:]})
        i.pop(1)
        i.pop(5)
        #進入mongodb
        connector.insert_data(i)
    
    for i in new_df[:][2]:
        #print(i)
        total_price+=int(i[i.find("$")+1:])

    for k in range(new_df.shape[0]):
        t1 = new_df[0][k]+" "+new_df[2][k]+" "+new_df[3][k]+" "+new_df[4][k]+"\n" 
        t += t1

    t+= ("總共 "+ str(new_df.shape[0])+"杯 "+ str(total_price)+"元")
    t+=("\n"+"*"*30)
    
    t2=""
    #list(new_df[:][2]+new_df[:][3]+new_df[:][4]) 
    result_count = Counter(list(new_df[:][2]+new_df[:][3]+new_df[:][4]))
    for c in result_count:
        t2 = "\n"+c+" "+str(result_count[c])
        t += t2
    
    return t



