## Table of contents
* [arayuzlu_klasor_uzantisi_belirsiz_dosya_listeleyici](#arayuzlu_klasor_uzantisi_belirsiz_dosya_listeleyici)
* [Kullanılan paketler](#kullanılan-paketler)
* [Kurulum](#kurulum)

## arayuzlu_klasor_uzantisi_belirsiz_dosya_listeleyici
Python'un Tkinter modülüyle arayüzü yazılmış ve Linux, Windows ve Mac OX ile uyumlu, verilen klasördeki uzantısı belli olmayan dosyaların uzantısını anlayıp listeleyen, pasta grafiğini dahi oluşturan program.
	
## Kullanılan paketler
* Python version: 3.7.8
* matplotlib version: 3.3.3
* filetype version: 1.0.7
	
## Kurulum
Uzantısı bilinmeyen dosyanın uzantısını bulan modül için:
```
pip install filetype
```

Arayüzdeki pasta grafiği için:
```
pip3 install matplotlib
```

## Kullanım
Terminale aşağıdaki yazılır. (python3 yerine python da olabilir ortam değişkeninize göre lakin python 2 de denemedim programı.)
python3 dosya_tiplerini_listele.py "path"

arayüzlü için:
python3 dosya_tiplerini_listele_arayuzlu.py

## Anlaşılabilen Uzantılar
Bu kod dosyanın sonundaki .uzantı kısmına hiç bakmaz. Anlayabildiği uzantılar:
```
Image
jpg - image/jpeg
jpx - image/jpx
png - image/png
gif - image/gif
webp - image/webp
cr2 - image/x-canon-cr2
tif - image/tiff
bmp - image/bmp
jxr - image/vnd.ms-photo
psd - image/vnd.adobe.photoshop
ico - image/x-icon
heic - image/heic
Video
mp4 - video/mp4
m4v - video/x-m4v
mkv - video/x-matroska
webm - video/webm
mov - video/quicktime
avi - video/x-msvideo
wmv - video/x-ms-wmv
mpg - video/mpeg
flv - video/x-flv
Audio
mid - audio/midi
mp3 - audio/mpeg
m4a - audio/m4a
ogg - audio/ogg
flac - audio/x-flac
wav - audio/x-wav
amr - audio/amr
Archive
epub - application/epub+zip
zip - application/zip
tar - application/x-tar
rar - application/x-rar-compressed
gz - application/gzip
bz2 - application/x-bzip2
7z - application/x-7z-compressed
xz - application/x-xz
pdf - application/pdf
exe - application/x-msdownload
swf - application/x-shockwave-flash
rtf - application/rtf
eot - application/octet-stream
ps - application/postscript
sqlite - application/x-sqlite3
nes - application/x-nintendo-nes-rom
crx - application/x-google-chrome-extension
cab - application/vnd.ms-cab-compressed
deb - application/x-deb
ar - application/x-unix-archive
Z - application/x-compress
lz - application/x-lzip
Font
woff - application/font-woff
woff2 - application/font-woff
ttf - application/font-sfnt
otf - application/font-sfnt
```
