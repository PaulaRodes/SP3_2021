import os

os.system("ffmpeg -i bbb_original.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://@127.0.0.1:1234?pkt_size=1316")
os.system("ffplay udp://127.0.0.1:1234")
