from pyparsing import (alphanums, alphas, CharsNotIn, Forward,
Group, hexnums, OneOrMore, Optional, ParseException, Combine,nums,
ParseSyntaxException, Suppress, Word, ZeroOrMore, restOfLine, LineEnd)

songs = []

def add_song(tokens):
    print 'add_song==>', tokens
    songs.append(
        (tokens.title, tokens.filename, tokens.seconds) 
    )

title = restOfLine("title")
filename = restOfLine("filename")
# seconds = Combine(Optional("-") + Word(nums)).setParseAction(
#     lambda tokens: int(tokens[0]))("seconds")
seconds = Combine(Optional("-") + Word(nums))('seconds')
seconds.setParseAction(lambda tokens: int(tokens[0]))("seconds")


info = Suppress("#EXTINF:") + seconds + Suppress(",") + title
entry = info + LineEnd() + filename + LineEnd()
entry.setParseAction(add_song)
parser = Suppress("#EXTM3U") + OneOrMore(entry)

parser.parseFile('songsm3u')
for song in songs:
    print song
