"""
Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

Each object will have a "title" property (string), and a "plays" property (integer).

"""


def favorite_songs(playlist):
    sorted_playlist = sorted(playlist, key=lambda x: x['plays'], reverse=True)
    playlist = [sorted_playlist[0]['title'], sorted_playlist[1]['title']]

    return playlist


