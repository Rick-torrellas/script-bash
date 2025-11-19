@echo off
rem descargar_video_youtube

if "%1" == "" (
    echo descargar_video_youtube requiere aunque sea un parametro, la url del video.
    exit /b 1
) 

echo "%~1"
:: yt-dlp -f "bestvideo[height<=720]+bestaudio" --merge-output-format mp4 %1
exit /b 0

:: $1: url del video - $2: resolucion del video - $3: extencion del archivo 
@REM doskey descargar_video_youtube=yt-dlp -f "bestvideo[height<=$2]+bestaudio" --merge-output-format $3 $1
:: $1: url video
@REM doskey descargar_video_youtube720=yt-dlp -f "bestvideo[height<=720]+bestaudio" --merge-output-format mp4 $*
:: $1: url video
@REM doskey descargar_video_youtube1080=yt-dlp -f "bestvideo[height<=1080]+bestaudio" --merge-output-format mp4 $*