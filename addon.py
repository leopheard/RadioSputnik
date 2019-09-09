from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "http://feeds.soundcloud.com/users/soundcloud:users:128016508/sounds.rss" #RADIOSPUTNIK
url2 = "https://sputniknews.com/export/rss2/podcast/radio_brave_new_world/"#BRAVENEWWORLD
url3 = "https://www.spreaker.com/show/1843722/episodes/feed" #BYANYMEANSNECESSARY
url4 = "https://www.spreaker.com/show/2976255/episodes/feed" #CRITICALHOUR
url5 = "https://www.spreaker.com/show/2268375/episodes/feed" #FAULTLINES
url6 = "https://www.spreaker.com/show/1610382/episodes/feed" #LOUDANDCLEAR
url7 = "https://www.spreaker.com/show/1949270/episodes/feed" #SOUNDCLIPS
url8 = "https://www.spreaker.com/show/2795762/episodes/feed" #SPECIALS
url9 = "https://www.spreaker.com/show/1843699/episodes/feed" #SPUTNIKINTERVIEWS
url10 = "https://apps.apple.com/us/app/sputnik-trending/id1093760760" #SPUTNIKTRENDING
url11 = "https://www.spreaker.com/show/1843710/episodes/feed" #UNANIMOUSDISSENT

#COULDNTFIND:#MOTHEROFALLTALKSHOWS#DOUBLEDOWN#SHOOTFROMTHELIP
#livestreamurl = "http://icecast-ruvr.cdnvideo.ru/rian.voiceusa"
#livealt"https://nfw.ria.ru/flv/audio.aspx?ID=40881855&type=mp3"

#"http://audio1.video.ria.ru/voiceeng" English
#"http://icecast-ruvr.cdnvideo.ru/rian.voiceusa"USA

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30099), 
            'path': plugin.url_for('episodes0'),
            'thumbnail': "https://cdn2.img.sputniknews.com/i/logo-white-inverse.png",
            'is_playable': True},
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000155813306-0dx5lm-large.jpg"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/ff/c6/35/ffc635c1-07cb-e3d9-abca-9190dad61910/mza_1362507698747519806.png/600x600bb.jpg"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/79e4d878722cc516b310afab99097268.jpg"},
        {
            'label': plugin.get_string(30004), 
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/d94cdb720ae1cad0e4fd69c61fad47fb.jpg"},
        {
            'label': plugin.get_string(30005), 
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/792313e17b3d393f3dcdd0bbf7a622dd.jpg"},
        {
            'label': plugin.get_string(30006), 
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/a59b15ee9c65c3b2c6f944b30f3d12a1.jpg"},
        {
            'label': plugin.get_string(30007), 
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/3ab164980e3fb650a1b7827c429ad773.jpg"},
        {
            'label': plugin.get_string(30008), 
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/4d31331608b66351c3183d4d2fe053c4.jpg"},
        {
            'label': plugin.get_string(30009), 
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/3ab164980e3fb650a1b7827c429ad773.jpg"},
        {
            'label': plugin.get_string(30010), 
            'path': plugin.url_for('episodes10'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Purple123/v4/97/f3/45/97f3451c-a6cc-9dd6-704c-80e3a0e2c5c1/source/100x100bb.jpg"},
        {
            'label': plugin.get_string(30011), 
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/ed42474fe8c483e721e26df3657d20d6.jpg"},
    ]
    return items

@plugin.route('/episodes0/')
def episodes0():
    #soup = criminalpodcast.compile_new_to_criminal(URL)
    playable_podcast0 = mainaddon.get_playable_podcast0
    items = mainaddon.compile_playable_podcast0(playable_podcast0)
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items

@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items

@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7)
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items

@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items

@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items

@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(url10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items

@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(url11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items

if __name__ == '__main__':
    plugin.run()
