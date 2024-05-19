import requests 
import random
import platform 
import time
import os




try:
    token_1 = open("tokenInsta.txt","r").readline().strip()
    id_1 =open("idInsta.txt","r").readline().strip()
    print(f"\n\n\n\n\n [=] YoUr ToKen : {token_1}\n")
    print(f" [=] YoUr Id : {id_1}\n")
    print(" [!] Note : iF You WaNt to Change Id Or Token Go at The Same file u put the Tool \n\n [!] tokenInsta.txt \n\n [!] idInsta.txt ")
    time.sleep(8)
    os.system("clear")
except:
    print("         FiRsT PlEaSe EnTer You ID AND TOkEN BOT         ")
    token = input("[=] ToKeN BoT : ")
    if platform.system() == "Windows":
        open("tokenInsta.txt",'w').write(token)
    else:
        open("tokenInsta.txt",'w').write(token)

    id = input("[=] Id TeleGraM : ")
    if platform.system() == "Windows":
        open("idInsta.txt","w").write(id)
    else:
        open("idInsta.txt",'w').write(id)
    os.system("clear")

token_1 =open("tokenInsta.txt","r").readline().strip()
id_1 =open("idInsta.txt","r").readline().strip()

print('''



            [*]    WlcoMe Sir To User ChEck InSaT UseR  [*]
                    [*] DeV : MeDO  @KKKKKQ9 [*]
      

    [*] Please Choose The length of the user [*]

      1 - FoUr ==> [4]
      2 - FiVe ==> [5]
      3 - Six  ==> [6]

      4 - To See The All Good UseR [!]
      5 - Change The ID And Token [!]
    
''')
Choose = input(" [+] ChOoSe : ")
os.system("clear")
print("")

t = 0
b1 = 0
b2 = 0

if Choose == ('1'):
    print(' [!] Do You Want Numbers and signs In The UseR ? ')
    print("")
    hab = input(" [+] PleaSe ChooSe (Yes) Or (No) : ")
    if hab == "yes"or"YES":
        os.system("clear")
        while True:
            usr = ("qwertyuiopasdfghjklzxcvbnm1234567890_.")
            User1 = str(''.join((random.choice(usr) for i in range(4))))
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            headers ={'Host':'www.instagram.com',
            'content-length':'85',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'sec-ch-ua-mobile':'?0',
            'x-instagram-ajax':'81f3a3c9dfe2',
            'content-type':'application/x-www-form-urlencoded',
            'accept':'*/*',
            'x-requested-with':'XMLHttpRequest',
            'x-asbd-id':'198387',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
            'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'sec-ch-ua-platform':'"Linux"',
            'origin':'https://www.instagram.com',
            'sec-fetch-site':'same-origin',
            'sec-fetch-mode':'cors',
            'sec-fetch-dest':'empty',
            'referer':'https://www.instagram.com/accounts/emailsignup/',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-IQ,en;q=0.9',
            'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
            'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
            'cookie':'ig_nrcb=1'}
            data= (f'email=aakmnnsjskksmsnsn%40gmail.com&username={User1}&first_name=&opt_into_one_tap=false')
            respons = requests.post(url,headers=headers , data=data)
            if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in respons.text:
                b1+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            elif '"errors": {"username":' in respons.text or  '"code": "username_is_taken"' in respons.text:
                b2+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            else:
                t+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
                if platform.system() == "Windows":
                    fileopen = open("Ok_user","a").write(f"{User1}\n")
                    tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                    requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
                else:
                    open("ok_user","a").write(f"{User1}\n")
                tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")



    elif hab == 'No' or 'no':
        os.system("clear")
        while True:
            usr = ("qwertyuiopasdfghjklzxcvbnm")
            User1 = str(''.join((random.choice(usr) for i in range(4))))
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            headers ={'Host':'www.instagram.com',
            'content-length':'85',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'sec-ch-ua-mobile':'?0',
            'x-instagram-ajax':'81f3a3c9dfe2',
            'content-type':'application/x-www-form-urlencoded',
            'accept':'*/*',
            'x-requested-with':'XMLHttpRequest',
            'x-asbd-id':'198387',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
            'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'sec-ch-ua-platform':'"Linux"',
            'origin':'https://www.instagram.com',
            'sec-fetch-site':'same-origin',
            'sec-fetch-mode':'cors',
            'sec-fetch-dest':'empty',
            'referer':'https://www.instagram.com/accounts/emailsignup/',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-IQ,en;q=0.9',
            'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
            'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
            'cookie':'ig_nrcb=1'}
            data= (f'email=aakmnnsjskksmsnsn%40gmail.com&username={User1}&first_name=&opt_into_one_tap=false')
            respons = requests.post(url,headers=headers , data=data)
            if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in respons.text:
                b1+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            elif '"errors": {"username":' in respons.text or  '"code": "username_is_taken"' in respons.text:
                b2+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            else:
                t+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
                if platform.system() == "Windows":
                    fileopen = open("Ok_user","a").write(f"{User1}\n")
                    tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                    requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
                else:
                    open("ok_user","a").write(f"{User1}\n")
                tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
############
if Choose == "2":
    os.system("clear")
    print('هل تريد معاه اشارات وارقام ؟ ')
    print("")
    hab1 = input("PleaSe ChooSe (Yes) Or (No) : ")
    if hab1 == "yes" or "YES":
        os.system("clear")
        while True:
            usr = ("qwertyuiopasdfghjklzxcvbnm0987654321._")
            User1 = str(''.join((random.choice(usr) for i in range(5))))
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            headers ={'Host':'www.instagram.com',
            'content-length':'85',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'sec-ch-ua-mobile':'?0',
            'x-instagram-ajax':'81f3a3c9dfe2',
            'content-type':'application/x-www-form-urlencoded',
            'accept':'*/*',
            'x-requested-with':'XMLHttpRequest',
            'x-asbd-id':'198387',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
            'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'sec-ch-ua-platform':'"Linux"',
            'origin':'https://www.instagram.com',
            'sec-fetch-site':'same-origin',
            'sec-fetch-mode':'cors',
            'sec-fetch-dest':'empty',
            'referer':'https://www.instagram.com/accounts/emailsignup/',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-IQ,en;q=0.9',
            'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
            'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
            'cookie':'ig_nrcb=1'}
            data= (f'email=aakmnnsjskksmsnsn%40gmail.com&username={User1}&first_name=&opt_into_one_tap=false')
            respons = requests.post(url,headers=headers , data=data)
            if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in respons.text:
                b1+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            elif '"errors": {"username":' in respons.text or  '"code": "username_is_taken"' in respons.text:
                b2+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            else:
                t+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
                if platform.system() == "Windows":
                    fileopen = open("Ok_user","a").write(f"{User1}\n")
                    tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                    requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
                else:
                    open("ok_user","a").write(f"{User1}\n")
                tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
    elif Choose == "no" or "NO":
        os.system("clear")
        while True:
            usr = ("qwertyuiopasdfghjklzxcvbnm")
            User1 = str(''.join((random.choice(usr) for i in range(5))))
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            headers ={'Host':'www.instagram.com',
            'content-length':'85',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'sec-ch-ua-mobile':'?0',
            'x-instagram-ajax':'81f3a3c9dfe2',
            'content-type':'application/x-www-form-urlencoded',
            'accept':'*/*',
            'x-requested-with':'XMLHttpRequest',
            'x-asbd-id':'198387',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
            'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'sec-ch-ua-platform':'"Linux"',
            'origin':'https://www.instagram.com',
            'sec-fetch-site':'same-origin',
            'sec-fetch-mode':'cors',
            'sec-fetch-dest':'empty',
            'referer':'https://www.instagram.com/accounts/emailsignup/',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-IQ,en;q=0.9',
            'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
            'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
            'cookie':'ig_nrcb=1'}
            data= (f'email=aakmnnsjskksmsnsn%40gmail.com&username={User1}&first_name=&opt_into_one_tap=false')
            respons = requests.post(url,headers=headers , data=data)
            if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in respons.text:
                b1+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            elif '"errors": {"username":' in respons.text or  '"code": "username_is_taken"' in respons.text:
                b2+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            else:
                t+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
                if platform.system() == "Windows":
                    fileopen = open("Ok_user","a").write(f"{User1}\n")
                    tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                    requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
                else:
                    open("ok_user","a").write(f"{User1}\n")
                tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
elif Choose == "3":
    print('هل تريد معاه اشارات وارقام ؟ ')
    print("")
    hab2 = input("PleaSe ChooSe (Yes) Or (No) : ")
    if hab2 == "yes" or "YES":
        while True:
            usr = ("qwertyuiopasdfghjklzxcvbnm1234567890_.")
            User1 = str(''.join((random.choice(usr) for i in range(6))))
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            headers ={'Host':'www.instagram.com',
            'content-length':'85',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'sec-ch-ua-mobile':'?0',
            'x-instagram-ajax':'81f3a3c9dfe2',
            'content-type':'application/x-www-form-urlencoded',
            'accept':'*/*',
            'x-requested-with':'XMLHttpRequest',
            'x-asbd-id':'198387',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
            'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'sec-ch-ua-platform':'"Linux"',
            'origin':'https://www.instagram.com',
            'sec-fetch-site':'same-origin',
            'sec-fetch-mode':'cors',
            'sec-fetch-dest':'empty',
            'referer':'https://www.instagram.com/accounts/emailsignup/',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-IQ,en;q=0.9',
            'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
            'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
            'cookie':'ig_nrcb=1'}
            data= (f'email=aakmnnsjskksmsnsn%40gmail.com&username={User1}&first_name=&opt_into_one_tap=false')
            respons = requests.post(url,headers=headers , data=data)
            if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in respons.text:
                b1+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            elif '"errors": {"username":' in respons.text or  '"code": "username_is_taken"' in respons.text:
                b2+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            else:
                t+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
                if platform.system() == "Windows":
                    fileopen = open("Ok_user","a").write(f"{User1}\n")
                    tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                    requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
                else:
                    open("ok_user","a").write(f"{User1}\n")
                tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
    elif hab2 == "no" or "No":
        while True:
            usr = ("qwertyuiopasdfghjklzxcvbnm")
            User1 = str(''.join((random.choice(usr) for i in range(6))))
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            headers ={'Host':'www.instagram.com',
            'content-length':'85',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'sec-ch-ua-mobile':'?0',
            'x-instagram-ajax':'81f3a3c9dfe2',
            'content-type':'application/x-www-form-urlencoded',
            'accept':'*/*',
            'x-requested-with':'XMLHttpRequest',
            'x-asbd-id':'198387',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
            'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'sec-ch-ua-platform':'"Linux"',
            'origin':'https://www.instagram.com',
            'sec-fetch-site':'same-origin',
            'sec-fetch-mode':'cors',
            'sec-fetch-dest':'empty',
            'referer':'https://www.instagram.com/accounts/emailsignup/',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-IQ,en;q=0.9',
            'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
            'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
            'cookie':'ig_nrcb=1'}
            data= (f'email=aakmnnsjskksmsnsn%40gmail.com&username={User1}&first_name=&opt_into_one_tap=false')
            respons = requests.post(url,headers=headers , data=data)
            if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in respons.text:
                b1+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            elif '"errors": {"username":' in respons.text or  '"code": "username_is_taken"' in respons.text:
                b2+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
            else:
                t+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'''

    [+] GooD UsEr : {t}

    [+] Bad User : {b1+b2}

    [=] User Check : {User1}

''')
                if platform.system() == "Windows":
                    fileopen = open("Ok_user","a").write(f"{User1}\n")
                    tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                    requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")
                else:
                    open("ok_user","a").write(f"{User1}\n")
                tlg=(f'''
                    [!] NeW GooD UseR   [!]

                        [=] {User1} [=]

                        [!] @KKKKKQ9  [!]
                     
                     ''')
                requests.post(f"https://api.telegram.org/bot{token_1}/sendMessage?chat_id={id_1}&text={tlg}")

                
if Choose == "5":
    print(" [!]Input What You Want To ChanGe Sir ")
    changer = input("Choose (id) Or (token) : ")
    if changer == "ID" or "id":
        id = input("[=] Id TeleGraM : ")
        if platform.system() == "Windows":
            open("idInsta.txt","w").write(id)
        else:
            open("idInsta.txt",'w').write(id)
        os.system("clear")
        exit()
    elif changer == "TOKEN" or "token":
        print('InPut Your New Id and Token ')
        token = input("[=] ToKeN BoT : ")
        if platform.system() == "Windows":
            open("tokenInsta.txt",'w').write(token)
        else:
            open("tokenInsta.txt",'w').write(token)
        os.system("clear")
        exit()

if Choose == "4":
    try:
        usercoo= open("ok_user","r").readlines()
        for i in range(len(usercoo)):
            print(f"{i} - {usercoo[i]}")
    except FileNotFoundError:
        print("\n\n [!] THere's no file for good user Yet\n\n")
        
else:
    os.system("clear")
    print(" \n\nSorry Try Agin wrong input [!] \n\n")
    exit()
