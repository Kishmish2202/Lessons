with open ('lyrics.txt', encoding = "utf8") as f:
    lyrics = f.read()
    
#print(lyrics)
#print(type(lyrics))

lyrics_list = []
banned = [' ','.',',','!',"'"]
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

check_dupes = {}

for w in lyrics_list:
    w = w.lower()
    if w not in check_dupes:
        check_dupes[w] = 1
    else:
        check_dupes[w] += 1

most_freq_world = max(check_dupes.values())

for k in check_dupes.keys():
    if check_dupes[k] == most_freq_world:
        most_freq_world = k, check_dupes[k]
        break
print(f'Часто употребляли слово: {most_freq_world[0]} - {most_freq_world[1]}')

def most_common_worlds(freq):
    values = freq.values()
    best = max(values)
    worlds = []
    for k in freq:
        if freq[k] == best:
            worlds.append(k)
    return worlds, best
#print(most_common_worlds(check_dupes))

def worlds_often (freq,times):
    result = []
    done = False
    while not done:
        temp = most_common_worlds(freq)
        if temp[1] >= times:
            result.append(temp)
            for w in temp[0]:
                del(freq[w])
        else:
            done = True 
    return result

lyrics_2000 = worlds_often(check_dupes, 2)
print(lyrics_2000)