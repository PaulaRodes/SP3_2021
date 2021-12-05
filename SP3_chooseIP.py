import os

def choose(ip):
    os.system("ffmpeg -i bbb_original.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://@ip")
    os.system("ffplay udp://ip")
    
    
IP = input("Enter the desired IP: ")
choose(IP)