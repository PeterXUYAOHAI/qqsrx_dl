#-*- coding: utf-8 -*-

import pafy
import os
import subprocess
import itchat
import datetime

itchat.auto_login(hotReload=True, enableCmdQR=2)
#need to change to all video in channel
plurl = "https://www.youtube.com/playlist?list=PLUdOxqM_oDhuPNq-Ake09j4xPDQP6kyCT"
playlist = pafy.get_playlist(plurl)

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d %H:%M")
itchat.send(date + ' start to update newfeed', toUserName='filehelper')

exist_audios = os.listdir("./qqsrx_audio")
print exist_audios[0]
type(exist_audios[0])
for item in playlist['items']:
        try:
                title = item['pafy'].title
                published = item['pafy'].published
                title_with_ext = published+title+".m4a"
                title_with_ext = title_with_ext.replace(" ","").replace(":","")
                print type(title_with_ext)
                #this check not work, because utf-8 problem
                if title_with_ext not in exist_audios:
                        audio = item['pafy'].m4astreams[0]
                        audio.download(filepath="./qqsrx_audio/"+title_with_ext)
        except:
                continue

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d %H:%M")
itchat.send(date + ' start to sync newfeed with baidu', toUserName='filehelper')

subprocess.call("bypy -vd syncup ./qqsrx_audio /qqsrx_audio", shell=True)

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d %H:%M")
itchat.send(date + ' update finished', toUserName='filehelper')
