from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage

# Create your views here.
line_bot_api = LineBotApi('FahJPPqUxtoq/yLuc+En5xIHdTK/NCewWMYkQ/hBF760e77vT9QZkQIDignIUE1R9VExkX57K+uoMhrr0Q2SGQymGXrbltmE9phrI8gX5ZHdljjvffKHj62Wp12kmpMcHRwzIlL7od/Fe2Tz0L28OQdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('a490f46fc8269f37c7e73911561a635e')

@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=event.message.text)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()