"""
Spotify Playlists - SOLUTION

You work for Spotify and are creating a feature for users to alphabetize their playlists by song title. Below is a list of titles from a sample playlist. Alphabetize these songs and print the result. Then do the reverse.
"""

playlist_titles = ['Tiny Dancer', 'At Last', 'Fortunate Son', 
'Hey Jude', 'Isn\'t She Lovely', 'Just the Way You Are', 'I\'m Yours',
'Vienna', 'Roxanne', 'Dancing in the Moonlight']

playlist_titles = ['Tiny Dancer', 'At Last', 'Fortunate Son', 
'Hey Jude', 'Isn\'t She Lovely', 'Just the Way You Are', 'I\'m Yours',
'Vienna', 'Roxanne', 'Dancing in the Moonlight']

# Alphabetized
print(sorted(playlist_titles))
"""['At Last', 'Dancing in the Moonlight', 'Fortunate Son', 'Hey Jude', "I'm Yours", "Isn't She Lovely", 'Just the Way You Are', 'Roxanne', 'Tiny Dancer', 'Vienna']"""


# Reversed
print(sorted(playlist_titles, reverse=True))
"""['Vienna', 'Tiny Dancer', 'Roxanne', 'Just the Way You Are', "Isn't She Lovely", "I'm Yours", 'Hey Jude', 'Fortunate Son', 'Dancing in the Moonlight', 'At Last']"""
