#!/bin/bash
# Donne un rendu « vraie vidéo iPhone » à une vidéo IA trop propre :
# image un peu adoucie, grain temporel, légère respiration d'exposition, recompression façon réseaux sociaux,
# micro-tremblement optionnel, et son de téléphone dans une pièce (petite réverbération + bruit de fond).
# Usage : filtre-iphone.sh entree.mp4 sortie.mp4 [tremblement 0|1] [son-piece 0|1]
set -e
IN=$1; OUT=$2; SHAKE=${3:-0}; ROOM=${4:-1}
TMP=$(mktemp -d -p "$(dirname "$OUT")")
if [ "$SHAKE" = 1 ]; then
  CROP="crop=w=iw*0.95:h=ih*0.95:x='(iw-ow)/2+(iw-ow)/2*0.55*sin(t*1.9)*cos(t*0.73)':y='(ih-oh)/2+(ih-oh)/2*0.45*sin(t*1.3+1)*cos(t*0.51)',"
else CROP=""; fi
VF="${CROP}scale=576:1024:flags=area,gblur=sigma=0.45,eq=contrast=0.96:saturation=1.04:gamma=1.02:brightness='0.012*sin(2*PI*t/3.9)':eval=frame,noise=c0s=9:c0f=t+u:c1s=4:c1f=t:c2s=4:c2f=t"
if [ "$ROOM" = 1 ]; then
  AF="highpass=f=110,lowpass=f=11000,aecho=0.85:0.5:18|33:0.10|0.06,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120"
  ffmpeg -v error -y -i "$IN" -f lavfi -i "anoisesrc=color=brown:amplitude=0.0035:sample_rate=48000" \
    -filter_complex "[0:a]aresample=48000,$AF[v];[1:a]lowpass=f=900[n];[v][n]amix=inputs=2:duration=first:weights=1 1,loudnorm=I=-16:TP=-1.5:LRA=11[a]" \
    -map 0:v -map "[a]" -vf "$VF" -c:v libx264 -preset veryfast -b:v 1600k -maxrate 1900k -bufsize 2200k -pix_fmt yuv420p -c:a aac -b:a 128k "$TMP/mid.mp4"
else
  ffmpeg -v error -y -i "$IN" -vf "$VF" -af "loudnorm=I=-16:TP=-1.5:LRA=11" -c:v libx264 -preset veryfast -b:v 1600k -maxrate 1900k -bufsize 2200k -pix_fmt yuv420p -c:a aac -b:a 128k "$TMP/mid.mp4"
fi
ffmpeg -v error -y -i "$TMP/mid.mp4" -vf "scale=1080:1920:flags=bicubic" -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a copy -movflags +faststart "$OUT"
rm -rf "$TMP"
echo "ok $OUT"
