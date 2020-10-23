from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.simplecast.com/62B8minO"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://image.simplecastcdn.com/images/64af662e-1592-4f56-95e3-fb640c2a3a03/697e3847-2690-4f50-b24e-2b2b40bfffb5/3000x3000/1550591259-artwork.jpg?aid=rss_feed"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://image.simplecastcdn.com/images/64af662e-1592-4f56-95e3-fb640c2a3a03/697e3847-2690-4f50-b24e-2b2b40bfffb5/3000x3000/1550591259-artwork.jpg?aid=rss_feed"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
