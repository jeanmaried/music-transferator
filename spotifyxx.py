import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import re

# Get the username from terminal
username = sys.argv[1]

# Set spotify permission scopes
scope = 'user-library-modify'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

#
#
#
#
#
#
#
#
#
# //////////////// SET UP //////////////

# # open data.json and convert it to dict
# with open('data.json') as f:
#     data = json.load(f)

# # write not found tracks to not_found_tracks.json
# not_found_data = []

# for x in data:
#     if x['isFound'] == 0:
#         not_found_data.append(x)

# with open('not_found_tracks.json', 'w') as outfile:
#     json.dump(not_found_data, outfile)

# //////////////// END SET UP //////////////
#
#
#
#
#
#
#
#
#
#

# open not_found_data.json and convert it to dict
with open('not_found_tracks.json') as f:
    not_found_tracks = json.load(f)

# track has artist in title
track_name_has_artist = []

count_has_parenthese = 0
count_but_only_one_side = 0
count_has_two_sides = 0
count_has_right_format = 0
count_other_format = 0
count_has_feat = 0
count_is_remix = 0
count_is_mix = 0
count = 0

for track in not_found_tracks:
    count += 1
    if re.search("-", track['title']):
        # split track into array to extract artist names from title
        splitTrack = track['title'].split('-')
        # if track has artist in title
        if splitTrack[0].find(track['artist']):
            track_name_has_artist.append(
                {"track": splitTrack[1], "artist": track['artist']})
    elif track['title'].find('(') > 0:
        count_has_parenthese += 1
        # if track has featuring artist
        if re.search(r"\([Ff](t|eat). .+\)", track['title']):
            count_has_feat += 1
        # if track is a remix
        elif re.search(r"\(.*([Rr]emix).*\)", track['title']):
            count_is_remix += 1
        # if is a mix
        elif re.search(r"^((?!.*\([Oo]riginal).*([ (][Mm]ix\b))|([Ss]et\b).*", track['title']):
            count_is_mix += 1
        else:
            print(track['title'], track['artist'])
    else:
        print(track['title'])

print({
    "count": count,
    "count_has_parenthese": count_has_parenthese,
    "count_has_feat": count_has_feat,
    "count_is_remix": count_is_remix,
    "count_is_mix": count_is_mix
    # "count_but_only_one_side": count_but_only_one_side,
    # "count_has_two_sides": count_has_two_sides,
    # "count_has_right_format": count_has_right_format,
    # "count_other_format": count_other_format,
})

# if track has -
# group it into new json file
# group others into their own
# check if first half contains artist name
# if yes, remove first half

# if track is found add to playlist instead of liking it


# search_results = []

# for x in not_found_data:
#     search = spotifyObject.search(
#         x['artist'], limit=10, offset=0, type='artist', market=None)
#     search_results.append(search)


# convert to iterable for python,
# if isFound === 0
# move to lost.json

# search = spotifyObject.search(
#     'Bring Back The Summer (feat. OLY)', limit=5, offset=0, type='track', market=None)

# track = search['tracks']['items'][0]['uri']

# spotifyObject.current_user_saved_tracks_add(tracks=[track])

# print(json.dumps(track, sort_keys=True, indent=4))


# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
