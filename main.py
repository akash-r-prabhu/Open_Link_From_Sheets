import webbrowser
import time
c_time=time.time()
i=0
while(1==1):
    if(int(time.time())==int(c_time+10)):
        c_time=c_time+10
        f=open("links.txt","r")
        s=f.readlines()
        if i<len(s):
            c=s[i].strip()
            if(c is not None):
                webbrowser.open(c)    
            i+=1
