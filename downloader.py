import colored as cl
from bs4 import BeautifulSoup
import requests as req
import sys


def extract_video_link_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    val = soup.find("source").get("src")
    return val


def download_video(vidoza_link, path):
    resp = req.get(vidoza_link)
    video_link = extract_video_link_from_html(resp.text)
    with open(path, 'wb') as f:
        f.write(req.get(str(video_link)).text)


if __name__ == "__main__":
    print(cl.fg("cyan"))
    print("""  _   ___    __              ___  __ 
 | | / (_)__/ /__  ___ ___ _/ _ \/ / 
 | |/ / / _  / _ \/_ // _ `/ // / /__
 |___/_/\_,_/\___//__/\_,_/____/____/
                                     """)
    print(cl.fg("white"))

    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: *.py <video_link>             (<file_path> + format)")
        print("       *.py https://vidoza.co/...    video.mp4")
        print("")
        print("Or import this file to your script.")
        print("")
        exit()

    if len(sys.argv) == 2:
        print("[*] Downloading '" + sys.argv[1] + "' to file 'output.mp4'")
        download_video(sys.argv[1], "output.mp4")
        print("[*] Done!")
        exit()

    if len(sys.argv) == 3:
        print("[*] Downloading '" + sys.argv[1] + "' to file '" + sys.argv[2] + "'")
        download_video(sys.argv[1], sys.argv[2])
        print("[*] Done!")
        exit()
