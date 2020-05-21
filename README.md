# Download videos of Microsoft-Ch9
**Get video download links from 'sitemap.xml(html)' for Microsoft Channel 9**

To download 

1. Get Sitemap.xml (or html) file from https://www.xml-sitemaps.com/
2. Use `sitemap_process.py` to get download links of videos and subtitles
3. Video links will send to clipboard automatically, IDM will catch all clipboard links and popup to make batch download
4. All subtitles(vtt) files will convert to srt files and renamed according to video titles, then downloaded inside this program
5. Use `video_rename.py` to rename .mp4 files by subtitles files, thus video player can load subtitles of videos automatically.
