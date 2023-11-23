#!/bin/env python
#Это телеграмм настройка

import requests  # для работы запросов 
def TOKEN():                  #токен делаем функцией чтобы иметь возможность экспорта 
  TOKEN = "ваш токен"
  return TOKEN
chat_id = "ваш айди чата"

############################################
import json  # переваривать json запросы из заббикс
from datetime import datetime   # это для первода времени и получение сегоднешнего
today = datetime.now().timestamp()  # сегоднешнее время  для последуещего вычесления времени недоступности

# авторизация в заббикс получаем токен 
ZABBIX_API_URL = "http://127.0.0.1:8080/api_jsonrpc.php"  #адрес заббикса

def AUTHTOKEN():            #делаем функцией чтобы иметь возможности вылониваться и залогиниваться по вызову а не открытию скрипта
  
  UNAME = "admin"      # пользователь заббикса дожен быть доступ к запрашиваемым узлам, тестировалось на юзер правах с доступом на чтение
  PWORD = "admin"    # пароль пользователя
  # autorization in zabbix
  r = requests.post(ZABBIX_API_URL,
                  json={"jsonrpc": "2.0",
                        "method": "user.login",
                        "params": {"user": UNAME,
                                   "password": PWORD},
                        "id": 1})

  AUTHTOKEN = r.json()["result"]
  return AUTHTOKEN

############################################
def logout():  #делаем функцией чтобы иметь возможности вылониваться и залогиниваться по вызову а не открытию скрипта
  requests.post(ZABBIX_API_URL,
                  json={"jsonrpc": "2.0",
                        "method": "user.logout",
                        "params": {},
                        "id": 2,
                        "auth": AUTHTOKEN()})






############################################

######## получаем список узлов в группе по id группы, которую вручную подставляем перед новой группой задаём spisok_id и передаём в функцию
def spisok_id_host(group):
    spid = requests.post(ZABBIX_API_URL,
json={"jsonrpc": "2.0",
      "method": "host.get",
      "params": { "output": ["hostid", "host"],
                  "selectInterfaces": ["ip"],
                  "groupids": [group]},

      "id": 1,
      "auth": AUTHTOKEN()})
    return spid
#### получаем по ip id хоста где ip это hostname, а rip это список айди хостов которая из функции spisok_id_host получается 
def getid(ip,rip):
  length = len(rip.json()['result'])  # количество узлов в группе вычесляет, потом подставляем в range
  for i in range(0,length): 
    a = str(rip.json()['result'][i]['interfaces'][0]['ip'])   # если не найдёт ip функция ничего не вернёт
    if a != ip:
      i += 1
    elif a == ip :      
      hostid = rip.json()['result'][i]['hostid']     
      break  
#  logout()  
  return hostid 



### функция из id хоста возвращает время длительности      

def timeproblem(hid): 
  
  r = requests.post(ZABBIX_API_URL,
        json={"jsonrpc": "2.0",
               "method": "problem.get",
               "params": {"hostids":hid,          # передаём айди хоста
                          "output":   ["name", "clock"],
                          "acknowledged":0,},           # отображать только не подтвержденные                          
               "id": 2,
               "auth": AUTHTOKEN()})

  l = r.json()['result']                        # это ловитель ошибок, если время вдруг в запросе нет он 2 минуты подставляет, в текущей версии такого быть не должно. 
  if l==[]:
    timeprob =(today - 120)   
  else:
    timeprob = int(r.json()['result'][0]['clock'])  # get the time
  #теперь время которое недоступно вычисляем 
  sec = (today - timeprob)       # отнимаем из сегодняшнего времени время падения камеры в timestamps
  day = sec //86400 # вычесляем дни
  hour = (sec  % 86400) // 3600  # вычесляем часы
  min = ((sec  % 86400) % 3600) // 60  # вычесляем минуты
#  logout()
  if hour == 0:                                 #в этом условие обрезаем часы и минуты если их нет 
     return "%02dм" % (min)
  elif day == 0:
    return "%02dч %02dм" % (hour, min)  
  else :
    return "%02dд %02dч %02dм" % (day, hour, min)


#######проверяем если проблема по айди узла, если её нет пропускает, если есть идёт дальше искать время итд
def problem(hid):
  r = requests.post(ZABBIX_API_URL,
        json={
                      "jsonrpc": "2.0",
                      "method": "problem.get",
                      "params": {
                          "output": ["name", "clock"],
                          "hostids":hid,   # передаём айди хоста
                          "acknowledged":0,},
                      "id": 2,
                      "auth": AUTHTOKEN()})
#  logout()                           
  if r.json()['result']==[] :                              # провряем есть ли проблемы на узле, нет значит пропуск 
    return 'noproblem'
  elif r.json()['result'][0]["name"] == 'ping':              # проверяем чтобы тригер назывался 'ping'
    return 'problem!!!'

############################################################################################
def uzly_svyazi():
  message = "❗❗❗Недоступны❗❗❗\n"  # шапка сообщения
#Название группы
  group12 = "========================\nУЗЛЫ СВЯЗИ\n========================\n"           
  message12 = group12            # сообщения имеют индекс, тк ранее они одним сообщением отпрвлялись, можно и просто "message1", но так можно легко одним сообщением сделать
  spisok_id = spisok_id_host("ваш фйли группы")  #в зависимости от группы( id берем из заббикса) получаем список id и ip



 
  hostname = "ваш айпи узла"
  hostid = getid(hostname,spisok_id)
  if problem(hostid) == 'problem!!!':
    duration_of_the_problem = timeproblem(hostid)
    message12= message12 + "Ытык-Кюэль контейнер\n"+  'Длительность ' +  duration_of_the_problem + '\n' + '‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n'

#если в группе нет падений название не выводится
  if not message12 == group12:
    message = message + message12    # если есть то добавляется название группы / так же сделано для возможности одним сообщением отправлять 
  else:
    message = group12 + " Все камеры доступны"



  if not message == "❗❗❗Недоступны❗❗❗\n":    # если есть какие то проблемы, проверяется добавления в общее тело 
    return message          
  


#если в группе нет падений название не выводится
  if not message13 == group13:
    message = message + message13
  else:
    message = group13 + " Все камеры доступны"

  if not message == "❗❗❗Недоступны❗❗❗\n":
    return message 