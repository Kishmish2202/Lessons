with open ('lyrics.txt', encoding = "utf8") as f:
    lyrics = f.read()
    
#print(lyrics)
#print(type(lyrics))

lyrics_list = []
banned = [' ','.',',','!']
lyrics_world = ''
for w in lyrics:
    w = w.lower()
    if w == '\n':
        if lyrics_world:
            lyrics_list.append(lyrics_world)
            lyrics_world = ''
    elif w not in banned:
        lyrics_world += w
    else:
        if lyrics_world:
            lyrics_list.append(lyrics_world)
        lyrics_world = ''
if lyrics_world:
    lyrics_list.append(lyrics_world)
    lyrics_world = ''
        
            
print(lyrics_list)
