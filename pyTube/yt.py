from pytube import YouTube
from pytube import Playlist
import os
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-y', '--youtube', dest='link1', help='link single Youtube')
parser.add_option('-l', '--playlist', dest='link2', help='link playlist Youtube')
parser.add_option('-o', '--output', dest='output', help='output location')

(options, args) = parser.parse_args()
if options.output is None:
        options.output = raw_input('Where saves files:')
if options.link1:
    if options.link1 is None:
        options.link1 = raw_input('Enter link1:')
if options.link2:
    if options.link2 is None:
        options.link2 = raw_input('Enter link2:')

print options.link1
print options.link2

