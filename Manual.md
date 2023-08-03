# KBK Line Bot 使用手冊
本文件提供了 KBK Line Bot 的操作說明，包括環境設定、程式碼運行、資料庫設定等步驟。提供對程式碼不瞭解的使用者，盡可能以文字描述，減少操作程式碼。

## 環境設定
-  安裝 Miniconda：確保你已經安裝了 Miniconda 套件管理器，它用於安裝 Python 與相關套件。

- 下載專案

- 建立虛擬環境：在專案資料夾中建立一個虛擬環境，以隔離此專案使用的 Python 套件，安裝相關套件，避免版本衝突。
    ```
    conda create --name kbk_bot_env --file requirements.txt
    conda activate kbk_bot_env
    ```

## ngrok
- 下載 ngrok：前往 ngrok 官網（https://ngrok.com/）下載並安裝 ngrok，用於開放本地端口。

##　資料庫設定
- 註冊 MongoDB 帳號：前往 MongoDB 官網（https://www.mongodb.com/cloud/atlas）註冊一個帳號。

- 建立 Cluster：在 MongoDB Cloud 中建立一個 Cluster，用於儲存 KBK Line Bot 的資料。

- 取得連線字串：在 Cluster 頁面中取得連線字串，其中包含 MongoDB 的用戶名與密碼，

- 在Database Access中，確保該使用者權限。

- 建立 token.txt 檔案：在專案資料夾中建立一個名為 token.txt 的文字檔，內容為 MongoDB 的用戶名與密碼，格式如下：
    ```
    username = "username"
    password = "password"
    ```

## 設定 Line Bot
- 建立 Line Bot：前往 LINE Developers（https://developers.line.biz/）建立一個 Line Bot。

- 執行程式啟動linebot：在 Terminal 中執行 KBKrobot.ipynb 程式碼。

- 開啟 Terminal：在專案資料夾中，開啟一個 Terminal 視窗。

- 啟動 ngrok：在 Terminal 中執行以下指令啟動 ngrok，並開放專案程式碼中指定的 port。
    ```
    ngrok http 6000 --host-header="localhost:6000" 
    ```

- 取得 ngrok 位址：在 ngrok 啟動後，取得產生的 URL，格式為 "https://xxxxxx.ngrok.io/verify"。

- 設定 Line Bot Webhook URL：回到 LINE Developers，將 Line Bot 的 Webhook URL 設定為 "https://xxxxxx.ngrok.io/verify"，並啟用 Webhook。

