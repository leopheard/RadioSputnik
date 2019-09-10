import requests
import re
from bs4 import BeautifulSoup

url1 = "http://feeds.soundcloud.com/users/soundcloud:users:128016508/sounds.rss" #RADIOSPUTNIK
url2 = "https://sputniknews.com/export/rss2/podcast/radio_brave_new_world/"#BRAVENEWWORLD
url3 = "https://www.spreaker.com/show/1843722/episodes/feed" #BYANYMEANSNECESSARY
url4 = "https://www.spreaker.com/show/2976255/episodes/feed" #CRITICALHOUR
url5 = "https://www.spreaker.com/show/2268375/episodes/feed" #FAULTLINES
url6 = "https://www.spreaker.com/show/1610382/episodes/feed" #LOUDANDCLEAR
url7 = "https://www.spreaker.com/show/1949270/episodes/feed" #SOUNDCLIPS
url8 = "https://www.spreaker.com/show/2795762/episodes/feed" #SPECIALS
url9 = "https://www.spreaker.com/show/1843699/episodes/feed" #SPUTNIKINTERVIEWS
url11 = "https://www.spreaker.com/show/1843710/episodes/feed" #UNANIMOUSDISSENT
url12 = "https://sputniknews.com/export/rss2/podcast/radio_trendstorm/" #RADIOTRENDSTORM

def get_soup0(url0):
    page = requests.get(url0)
    soup0 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup0))
    return soup0
get_soup0("http://feeds.soundcloud.com/users/soundcloud:users:128016508/sounds.rss")

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
get_soup1("http://feeds.soundcloud.com/users/soundcloud:users:128016508/sounds.rss")

def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
get_soup2("https://sputniknews.com/export/rss2/podcast/radio_brave_new_world/s")

def get_soup3(url3):
    page = requests.get(url3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
get_soup3("https://www.spreaker.com/show/1843722/episodes/feed")

def get_soup4(url4):
    page = requests.get(url4)
    soup4 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup4))
    return soup4
get_soup4("https://www.spreaker.com/show/2976255/episodes/feed")

def get_soup5(url5):
    page = requests.get(url5)
    soup5 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup5))
    return soup5
get_soup5("https://www.spreaker.com/show/2268375/episodes/feed")

def get_soup6(url6):
    page = requests.get(url6)
    soup6 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup6))
    return soup6
get_soup6("https://www.spreaker.com/show/1610382/episodes/feed")

def get_soup7(url7):
    page = requests.get(url7)
    soup7 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup7))
    return soup7
get_soup7("https://www.spreaker.com/show/1949270/episodes/feed")

def get_soup8(url8):
    page = requests.get(url8)
    soup8 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup8))
    return soup8
get_soup8("https://www.spreaker.com/show/2795762/episodes/feed")

def get_soup9(url9):
    page = requests.get(url9)
    soup9 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup9))
    return soup9
get_soup9("https://www.spreaker.com/show/1843699/episodes/feed")

def get_soup11(url11):
    page = requests.get(url11)
    soup11 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup11))
    return soup11
get_soup11("https://www.spreaker.com/show/1843710/episodes/feed")

def get_new_to_criminal(soup):
    subjects = []
    item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail
        }
    subjects.append(item)
    return subjects
def compile_new_to_criminal(compile_ntc):
    items = [{
		    'label': 'Sputnik livestream - USA',
        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
        	    'path': 'http://icecast-ruvr.cdnvideo.ru/rian.voiceusa',
        	    'is_playable': True},
           	    {'label': 'Sputnik livestream - English',
        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
        	    'path': 'http://audio1.video.ria.ru/voiceeng',
        	    'is_playable': True},
		    {'label': 'Sputnik livestream - French',
        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
        	    'path': 'https://nfw.ria.ru/flv/audio.aspx?ID=40881855&type=mp3',
        	    'is_playable': True},
		    {'label': 'Sputnik livestream - Spanish',
        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
        	    'path': 'http://icecast-ruvr.cdnvideo.ru/rian.voicespa',
        	    'is_playable': True},
		    {'label': 'Sputnik livestream - Russian',
        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
        	    'path': 'http://icecast-ruvr.cdnvideo.ru/rian.voicerus',
        	    'is_playable': True},
		    {'label': 'Sputnik livestream - Chinese',
        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
        	    'path': 'http://icecast-ruvr.cdnvideo.ru/rian.voicechi',
        	    'is_playable': True},
		    {'label': 'Sputnik livestream - German',
        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
        	    'path': 'http://icecast-ruvr.cdnvideo.ru/rian.voiceger',
        	    'is_playable': True},
		    {'label': 'Sputnik livestream - Portugese',
        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
        	    'path': 'http://icecast-ruvr.cdnvideo.ru/rian.voicepor',
        	    'is_playable': True},
]
    return items

#def get_playable_podcast0:
#    subjects = []
#    item = {
#                'url': link,
#                'title': title,
#                'desc': desc,
#                'thumbnail': thumbnail,
#        }
#    subjects.append(item)
#    return subjects
#def compile_playable_podcast0(soup0):
#    items = [{
#		    'label': 'Sputnik - USA',
#        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
#        	    'path': 'http://icecast-ruvr.cdnvideo.ru/rian.voiceusa',
#        	    'is_playable': True},
#           	    {'label': 'Sputnik - English',
#        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
#        	    'path': 'http://audio1.video.ria.ru/voiceeng',
#        	    'is_playable': True},
#		    {'label': 'Sputnik - French',
#        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
#        	    'path': 'https://nfw.ria.ru/flv/audio.aspx?ID=40881855&type=mp3',
#        	    'is_playable': True},
#		    {'label': 'Sputnik - German',
#        	    'thumbnail': 'https://cdn2.img.sputniknews.com/i/logo-white-inverse.png',
#        	    'path': 'http://audio1.video.ria.ru/voiceeng',
#        	    'is_playable': True},
#]
#    return items

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://i1.sndcdn.com/avatars-000155813306-0dx5lm-large.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/ff/c6/35/ffc635c1-07cb-e3d9-abca-9190dad61910/mza_1362507698747519806.png/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/79e4d878722cc516b310afab99097268.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast4(soup4):
    subjects = []
    for content in soup4.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/d94cdb720ae1cad0e4fd69c61fad47fb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast4(playable_podcast4):
    items = []
    for podcast in playable_podcast4:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast5(soup5):
    subjects = []
    for content in soup5.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/792313e17b3d393f3dcdd0bbf7a622dd.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast5(playable_podcast5):
    items = []
    for podcast in playable_podcast5:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast6(soup6):
    subjects = []
    for content in soup6.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/a59b15ee9c65c3b2c6f944b30f3d12a1.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast6(playable_podcast6):
    items = []
    for podcast in playable_podcast6:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast7(soup7):
    subjects = []
    for content in soup7.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/3ab164980e3fb650a1b7827c429ad773.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast7(playable_podcast7):
    items = []
    for podcast in playable_podcast7:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast8(soup8):
    subjects = []
    for content in soup8.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/4d31331608b66351c3183d4d2fe053c4.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast8(playable_podcast8):
    items = []
    for podcast in playable_podcast8:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast9(soup9):
    subjects = []
    for content in soup9.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/3ab164980e3fb650a1b7827c429ad773.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast9(playable_podcast9):
    items = []
    for podcast in playable_podcast9:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast11(soup11):
    subjects = []
    for content in soup11.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/ed42474fe8c483e721e26df3657d20d6.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast11(playable_podcast11):
    items = []
    for podcast in playable_podcast11:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast11(soup12):
    subjects = []
    for content in soup12.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://cdn3.img.sputniknews.com/images/105617/96/1056179634.png",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast12(playable_podcast12):
    items = []
    for podcast in playable_podcast12:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
