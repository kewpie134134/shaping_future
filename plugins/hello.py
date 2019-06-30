# coding: utf-8

import json
from slackbot.bot import respond_to


@respond_to('こんにちは')
def reply_hello(message):
    message.reply('こんにちは！')

# @respond_to('(.*)')
# def reply_echo(message, arg):
#     message.reply(arg)


@respond_to('スマイル')
def reply_slime(message):
    message.react('smile')


@respond_to('集合場所')
def reply_scadule(message):
    attachments = [
        {
            "color": "3104B4",
            "fields": [
                {
                    "title": "場所",
                    "value": "東京駅",
                },
                {
                    "title": "時間",
                    "value": "09:00",
                }
            ],
            "footer": "usagi-san",
            "footer_icon": "https://pics.prcm.jp/db36726f85742/67433428/jpeg/67433428.jpeg"
        }
    ]
    message.send_webapi('集合場所', json.dumps(attachments))
