import time
from datetime import datetime as dt



# hosts_path="/etc/hosts"
hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]


while True:
    #if we're in working hours
    #block the websites in website_list
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in  website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"\t"+website+"\n")
    else: #if we're not in working hours then unblock the websites in website_list
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0) #just before the first character of the file content
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() #deletes everything underneath
        print("Fun hours...")
    time.sleep(5)
