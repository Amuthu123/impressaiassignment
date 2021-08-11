from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render

from .models import CallInfo

import telebot
import ast
import time
from telebot import types

import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
API_KEY = env("API_KEY")

#API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)


def makeKeyboard():
    stringList = ['Stupid', 'Fat', 'Dumb']
    markup = types.InlineKeyboardMarkup()
    for btn in stringList:
        markup.add(types.InlineKeyboardButton(text=btn,callback_data="['btn', '" + btn + "']"))

    return markup

@bot.message_handler(commands=['show'])
def handle_command_adminwindow(message):
    bot.send_message(chat_id=message.chat.id,
                     text="Button Values :",
                     reply_markup=makeKeyboard(),
                     parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):

    if (call.data.startswith("['btn'")):
        #valueFromCallBack = ast.literal_eval(call.data)[1]
        n_c = 0
        if ast.literal_eval(call.data)[1] == "Stupid":
            valueFromCallBack = "What washes up on really small beaches? ...Micro-waves"

            btn_name = ast.literal_eval(call.data)[1]
            c_cnt = CallInfo.objects.filter(Button_name ='Stupid').count()
            if c_cnt > 0 :
                c_chk = CallInfo.objects.filter(Button_name ='Stupid')
                for i in c_chk:
                    n_c = i.No_Calls
                    n_c = n_c + 1

                CallInfo.objects.filter(Button_name ='Stupid').update(No_Calls = n_c)

            else :
                p = CallInfo(user_id ='1234', Button_name='Stupid', No_Calls= 1)
                p.save()
        elif ast.literal_eval(call.data)[1] == "Fat" :
            n_c = 0
            valueFromCallBack = "You are not fat, you have fat!!!!"

            btn_name = ast.literal_eval(call.data)[1]
            c_cnt = CallInfo.objects.filter(Button_name ='Fat').count()
            if c_cnt > 0 :
                c_chk = CallInfo.objects.filter(Button_name ='Fat')
                for i in c_chk:
                    n_c = i.No_Calls
                    n_c = n_c + 1

                CallInfo.objects.filter(Button_name ='Fat').update(No_Calls = n_c)

            else :
                p = CallInfo(user_id ='1234', Button_name='Fat', No_Calls= 1)
                p.save()

        elif ast.literal_eval(call.data)[1] == "Dumb" : 
            n_c = 0           
            valueFromCallBack = "What’s brown and sticky? ...A Stick"

            btn_name = ast.literal_eval(call.data)[1]
            c_cnt = CallInfo.objects.filter(Button_name ='Dumb').count()
            if c_cnt > 0 :
                c_chk = CallInfo.objects.filter(Button_name ='Dumb')
                for i in c_chk:
                    n_c = i.No_Calls
                    n_c = n_c + 1

                CallInfo.objects.filter(Button_name ='Dumb').update(No_Calls = n_c)

            else :
                p = CallInfo(user_id ='1234', Button_name='Dumb', No_Calls= 1)
                p.save()

        else:
            valueFromCallBack = "No Joke"
        bot.answer_callback_query(callback_query_id=call.id,
                              show_alert=True,
                              text= valueFromCallBack )

while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)

def callinfo(request):
	info_disp = ""
	callinfo_query = CallInfo.objects.all()
	for cinfo in callinfo_query:
		info_disp = "<tr><td>" + str(cinfo.user_id) + "</td><td>" + str(cinfo.Button_name) + "</td><td>"  + str(cinfo.No_Calls) + "</td></tr>"
	return render(request, 'chatbot_tutorial/callinfo.html',{'info_disp': info_disp})        