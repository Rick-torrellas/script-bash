#!/bin/bash

read url
resolution=720
yt-dlp -f "bestvideo[height<="$resolution"]+bestaudio/best" $url
type lss	
echo $?

