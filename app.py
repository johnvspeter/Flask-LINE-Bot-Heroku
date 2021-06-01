import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage,ButtonsTemplate,PostbackAction,MessageAction,URIAction

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))



@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        try:
            line_bot_api.push_message("U727f88967428705de1e7fe322771409d", TextSendMessage(text='台科大電腦研習社'))
        except InvalidSignatureError:
            abort(400)
        return "修改push"
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
    get_message = event.message.text
    if get_message=="你好":
        reply = TextSendMessage(text=f"你好臭雞雞")
        line_bot_api.reply_message(event.reply_token,reply)
        
    elif get_message=="滾":
        reply = TextSendMessage(text=f"你在哭阿")
        line_bot_api.reply_message(event.reply_token,reply)
    elif get_message=="走開":
        reply = TextSendMessage("蛤"+event.source.user_id)
        line_bot_api.reply_message(event.reply_token,reply)
    else:
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSt_IOaY-aGjlpLBUtM1xGqn74X-UIpiHH1ig&usqp=CAU',
                title='還不快打卡',
                text='想想你的一家老小阿',
                actions=[
                    # PostbackAction(
                    #     label='postback',
                    #     display_text='postback text',
                    #     data='action=buy&itemid=1'
                    # ),
                    # MessageAction(
                    #     label='message',
                    #     text='message text'
                    # ),
                    URIAction(
                        label='打卡囉',
                        uri='http://op.honorseiki.com:8787/External/COVID19/SignIn.aspx?openExternalBrowser=1'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,buttons_template_message)
        

    # Send To Line
    # reply = TextSendMessage(text=f"{get_message}")
    # line_bot_api.reply_message(event.reply_token, reply)

