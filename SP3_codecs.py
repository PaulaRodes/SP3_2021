import os


class SP3():
    
    def vp8():
        os.system("ffmpeg -i bbb_720p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis bbb_720_vp8.webm")
        os.system("ffmpeg -i bbb_480p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis bbb_480_vp8.webm")
        os.system("ffmpeg -i bbb_360x240.mp4 -c:v libvpx -b:v 1M -c:a libvorbis bbb_360_vp8.webm")
        os.system("ffmpeg -i bbb_160x120.mp4 -c:v libvpx -b:v 1M -c:a libvorbis bbb_160_vp8.webm")

    def vp9():
        os.system("ffmpeg -i bbb_720p.mp4 -c:v libvpx-vp9 -b:v 2M bbb_720_vp9.webm")
        os.system("ffmpeg -i bbb_480p.mp4 -c:v libvpx-vp9 -b:v 2M bbb_480_vp9.webm")
        os.system("ffmpeg -i bbb_360x240.mp4 -c:v libvpx-vp9 -b:v 2M bbb_360_vp9.webm")
        os.system("ffmpeg -i bbb_160x120.mp4 -c:v libvpx-vp9 -b:v 2M bbb_160_vp9.webm")
        
        
    def h265():
        os.system("ffmpeg -i bbb_720p.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k bbb_720_h265.mp4")
        os.system("ffmpeg -i bbb_480p.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k bbb_480_h265.mp4")
        os.system("ffmpeg -i bbb_360x240.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k bbb_360_h265.mp4")
        os.system("ffmpeg -i bbb_160x120.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k bbb_160_h265.mp4")
        
    def av1():
        os.system("ffmpeg -i bbb_720p.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental bbb_720_AV1.mkv")
        
        
        
SP3.vp8()
SP3.vp9()
SP3.h265()
SP3.av1()