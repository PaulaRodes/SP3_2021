import os

os.system("")

ffmpeg \
   -i bbb_720_vp8.webm \
   -i bbb_720_vp9.webm \
  -filter_complex " \
      [0:v] setpts=PTS-STARTPTS, scale=qvga [a0]; \
      [1:v] setpts=PTS-STARTPTS, scale=qvga [a1]; \
      [a0][a1]xstack=inputs=2:layout=0_0|w0_0[out] \
      " \
    -map "[out]" \
    -c:v libx264 -t '30' -f matroska comparison.mkv
