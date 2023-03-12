# Silly Me
Easy
Category: Warmup

## Challenge description

Not really Cybersec, just plain old sillyness!

Flag: RUSH{ALLCAPSMESSAGE}

![Challenge Picture](Silly_Me.jpeg)

## Solving

I downloaded the picture and looked at it, but on the first view, there is nothing interesting.
So let's start with the low hanging fruits... 

- file
- EXIF info
- and so on...

### file

Runing `file` on a file, will give you the file-type and some further infos about your item of interest.
```shell
file Silly_Me.jpeg
Silly_Me.jpeg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, Exif Standard: [TIFF image data, little-endian, direntries=3, software=Picasa], baseline, precision 8, 3000x608, components 3
```

But not in this case.

### EXIF

The EXIF data of a file will tell you some even more about a file. In fotos it is often used for detailed infos about the camera used for the picture and in some cases even, where it was shot.

But not in my case :-)

```shell
exiftool Silly_Me.jpeg 
ExifTool Version Number         : 12.57
File Name                       : Silly_Me.jpeg
Directory                       : .
File Size                       : 337 kB
File Modification Date/Time     : 2023:03:11 11:22:25+01:00
File Access Date/Time           : 2023:03:11 11:22:54+01:00
File Inode Change Date/Time     : 2023:03:11 11:22:54+01:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 96
Y Resolution                    : 96
Exif Byte Order                 : Little-endian (Intel, II)
Software                        : Picasa
Exif Version                    : 0220
Exif Image Width                : 3000
Exif Image Height               : 608
Image Width                     : 3000
Image Height                    : 608
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:0 (1 2)
Image Size                      : 3000x608
Megapixels                      : 1.8
```

### Deeper than...

Then lets look, if some hidden files are in this picture and run `binwalk`.
But there is nothing either...

```shell
$ binwalk -e Silly_Me.jpeg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30            0x1E            TIFF image data, little-endian offset of first image directory: 8

$ ls
Silly_Me.jpeg  silly_me.md  silly-me.png

$ ls -la
total 368
drwxr-xr-x 2 w3ich3rt w3ich3rt   4096 Mar 11 11:22 .
drwxr-xr-x 4 w3ich3rt w3ich3rt   4096 Mar 11 11:21 ..
-rw-r--r-- 1 w3ich3rt w3ich3rt 336615 Mar 11 11:22 Silly_Me.jpeg
-rw-r--r-- 1 w3ich3rt w3ich3rt      0 Mar 11 11:22 silly_me.md
-rw-r--r-- 1 w3ich3rt w3ich3rt  26939 Mar 11 11:21 silly-me.png
```

Okay... this does not help... I needed to have a look to the *hint*... The hint is

> Saying it out loud might help :p

... but this didn't help me either. I just asked my 14 years old daughter, because sometimes it is helpful to view with a different pair of eyes.
Together we figured out, the names for the different pictures.

1. First picture is a **sheikh**
2. The second picture is **Yor** a figure from an anime
3. The third picture is a **boot** and last but not least
4. The fourth picture is a **tea**

Said out loud it sounds like "SHAKEYOURBOOTY"

Lets give a try :D

> Flag:
> RUSH{SHAKEYOURBOOTY} 