import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = "event.message.text"
    if get_message=="你好":
        line_bot_api.reply_message(event.reply_token, "你好臭雞雞")
    elif get_message=="滾":
        line_bot_api.reply_message(event.reply_token, "你在哭阿")
    elif get_message=="走開":
        line_bot_api.reply_message(event.reply_token, "ㄟ我沒有欠你ㄟ")
    else:
        line_bot_api.reply_message(event.reply_token, "哩西哩工啥")

    # Send To Line
    # reply = TextSendMessage(text=f"{get_message}")
    # line_bot_api.reply_message(event.reply_token, reply)

