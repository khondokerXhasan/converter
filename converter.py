import requests,json,base64,marshal
from bs4 import BeautifulSoup as bs
class fb_link_to_uid():
	def __init__(self):
		self.session=requests.Session()
		try:req=self.session.get(marshal.loads(base64.b64decode(b'+kZodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20va2hvbmRva2VyWGhhc2FuL2Jpbi9tYWluL2Nvb2tpZS5qc29u'))).json();self.cookie={'cookie' : req['cookie']['facebook']};self.get_uid_name()
		except requests.exceptions.ConnectionError:print('\n\t\x1b[1;93m[\x1b[1;91m!\x1b[1;93m]\x1b[1;91m Network Connection Error ')
	def logo(self):
		logo='''\x1b[38;5;125m
  ____   ___   _   _ __     __ _____  ____   _____  _____  ____  
 / ___| / _ \ | \ | |\ \   / /| ____||  _ \ |_   _|| ____||  _ \ 
| |    | | | ||  \| | \ \ / / |  _|  | |_) |  | |  |  _|  | |_) |
| |___ | |_| || |\  |  \ V /  | |___ |  _ <   | |  | |___ |  _ < 
 \____| \___/ |_| \_|   \_/   |_____||_| \_\  |_|  |_____||_| \_\
 
         
        \x1b[38;5;140m ( \x1b[1;93mFind FB UID from Profile Link \x1b[38;5;140m)
          
        \x1b[38;5;172m[Developed by\x1b[38;5;161m Khondoker \x1b[1;92mX \x1b[38;5;161mHasan\x1b[38;5;172m ]
        \x1b[38;5;172m[github]: \x1b[38;5;129mgithub.com/khondoker\x1b[38;5;118mX\x1b[38;5;129mhasan
        
        
		'''
		return logo
	def get_uid_name(self):
		print(self.logo())
		fbd=input('\t\x1b[1;93m[\x1b[1;92m*\x1b[1;93m] Profile link : \x1b[1;92m')
		if 'www.facebook' in str(fbd):fbid=str(fbd).replace('www.facebook','mbasic.facebook')
		elif 'm.facebook' in str(fbd):fbid=str(fbd).replace('m.facebook','mbasic.facebook')
		else:pass
		try:
			req2=bs(self.session.get(fbid,cookies=self.cookie).text,'html.parser');name=str(str(req2.title).split('>')[1]).split('<')[0]
			for link in req2.find_all('a',href=True):
				if 'privacy/touch/block/confirm/?' in str(link):uid=str(link.get('href').split('&')[0]).split('=')[1]
				else:pass
			print('\n\t\x1b[1;93m[\x1b[1;92m>\x1b[1;93m] Name : \x1b[1;92m'+name)
			print('\t\x1b[1;93m[\x1b[1;92m>\x1b[1;93m] UID : \x1b[1;92m'+str(uid))
		except requests.exceptions.ConnectionError:print('\n\t\x1b[1;93m[\x1b[1;91m!\x1b[1;93m]\x1b[1;91m Network Connection Error ')
		except:print('\n\t\x1b[1;93m[\x1b[1;91m!\x1b[1;93m]\x1b[1;91m Account Not Found ')
fb_link_to_uid()