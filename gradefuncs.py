import random

# pseudo-random generation of a note from a specified section of the chromatic scale in either sharp or flat enharmonic naming conventions

SharpNotes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

FlatNotes = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]

def get_sharp_note(a,b):
    SN = SharpNotes[:]
    if a > b:
        del SN[b+1:a]
        return random.choice(SN)
    else:
        return random.choice(SN[a:b+1])

def get_flat_note(a,b):
    FN = FlatNotes[:]
    if a > b:
        del FN[b+1:a] 
        return random.choice(FN)
    else: 
        return random.choice(FN[a:b+1])

def get_note_in_range(a,b):
    if random.choice([True, False]):
        return get_sharp_note(a,b)
    else:
        return get_flat_note(a,b)

# returns any note of the chromatic scale    

def get_note():
    return get_note_in_range(0,11)

# returns a note from a specified section of the chromatic scale

def get_note_Gb_D():
    return get_note_in_range(6,2)

def get_note_F_D():
    return get_note_in_range(5,2)

def get_note_F_A():
    return get_note_in_range(5,9)

def get_note_A_Gb():
    return get_note_in_range(9,6)

def get_note_B_Gb():
    return get_note_in_range(11,6)

# generates arpeggio names

def get_major():
    return get_note() + " Major"

def get_minor():
    return get_note() + " Minor"

def get_major_seven():
    return get_note() + " Major 7th"

def get_minor_seven():
    return get_note() + " Minor 7th"

def get_dom_seven():
    return get_note() + " Dominant 7th"

# generates arpegiio inversion names

def get_inv(i):
    Inv = {0:", Root Position", 1:", 1st Inversion", 2:", 2nd Inversion", 3:", 3rd Inversion"}
    return Inv[int(i)]

def get_inv_arp(arp_func, i):
    return arp_func() + get_inv(i)

# generate arpeggios with altered chord tones

def get_ext(i):
    Ext = {0:"7b5", 1:"7#5", 2:"7b9", 3:"7#9", 4:"7b5b9", 5:"7b5#9", 6:"7#5b9", 7:"7#5#9"}
    return Ext[i]

def get_minor_seven_ext(i):
    return get_note_A_Gb() + "m" + get_ext(i)

def get_dom_seven_ext(i):
    return get_note_A_Gb() + get_ext(i)

# generate diatonic scales as lists

def is_sharp(i):
    return i in [2, 4, 7, 9]

def is_flat(i):
    return i in [3, 5, 8, 10]

def get_number_of_sharps(i):
    return [((7*x)%12) for x in range(12)].index(i)

def get_number_of_flats(i):
    return [((5*x)%12) for x in range(12)].index(i)

def get_sharps_scale(i):
    SharpsToAdd = get_number_of_sharps(i)
    RootIndex = (4*SharpsToAdd)%7
    NaturalNotes = ["C","D","E","F","G","A","B"]
    while SharpsToAdd > 0:
        NaturalNotes[((4*SharpsToAdd)-1)%7] += "#"
        SharpsToAdd -= 1
    return (2*NaturalNotes)[RootIndex:RootIndex+7]

def get_flats_scale(i):
    FlatsToAdd = get_number_of_flats(i)
    RootIndex = (3*FlatsToAdd)%7
    NaturalNotes = ["C","D","E","F","G","A","B"]
    while FlatsToAdd > 0:
        NaturalNotes[((3*FlatsToAdd)+3)%7] += "b"
        FlatsToAdd -= 1
    return (2*NaturalNotes)[RootIndex:RootIndex+7]

def get_major_scale(i):
    if is_sharp(i):
        return get_sharps_scale(i)
    elif is_flat(i):
        return get_flats_scale(i)
    elif random.choice([True, False]):
        return get_sharps_scale(i)
    else:
        return get_flats_scale(i)

def get_minor_scale(i):
    return (2*get_major_scale((i+3)%12))[5:12]

def major():
    return get_major_scale(random.randint(0,11))

def minor():
    return get_minor_scale(random.randint(0,11))

# format bass patterns

def f(Key):
    for i in range(len(Key)):
        while len(Key[i]) < 8:
            Key[i] += " "
    return Key

    

# generate chord sequences for bass patterns

def get_rnb_chords():
    Chords = minor()
    for i in [0,1,3]:
        Chords[i] += "m"
    for i in range(7):
        Chords[i] = "|" + Chords[i] + "7"
    Chords = f(Chords)
    for i in range(7):
        Chords[i] = 2*Chords[i]
    return Chords

def get_rnb_sequence(a,b,c,d):
    Key = get_rnb_chords()
    return Key[a] + Key[b] + "|\n" + Key[c] + Key[d] + "|"

def get_ballad_chords():
    Chords = major()[:6]
    for i in [1,2,5]:
        Chords[i] += "m"
    for i in range(6):
        Chords[i] = "|" + Chords[i]
    Chords = f(Chords)
    for i in range(6):
        Chords[i] = 2*Chords[i]
    return Chords

def get_ballad_sequence(a,b,c,d,e,f):
    Key = get_ballad_chords()
    return Key[a] + Key[b] + "|\n" + Key[c] + Key[d] + "|\n" + Key[e] + Key[f] + "|"


# performance

def get_alt():
    return random.choice(["7b5","7#5","7b9","7#9","7b5b9","7b5#9","7#5b9","7#5#9"])

MajorExts = [["","Maj7","6","sus4","Maj9","7"],
            ["m","m6","m7","m9","sus4"],
            ["m","m7","m9","m7#5","m7b9","m7#5b9"],
            ["","6","Maj7","Maj9","7","9","13","m","m7"],
            ["","6","7","9","11","13","aug","sus4",get_alt()],
            ["m","m7","m9","m7#5"],
            ["m7b5","°","°7","m7b5b9","m7#5","m7#5b9"]]

MinorExts = [["m","m6","m7","m9","m7#5"],
             ["m7b5","°","°7","m7b5b9","m7#5","m7#5b9"],
             ["","6","Maj7","Maj9","sus4"],
             ["m","m6","m7","m9","sus4"],
             ["m","m7","m9","m7#5","m7b9","m7#5b9","7","aug","11","13",get_alt(),"sus4"],
             ["","6","Maj7","Maj9"],
             ["","6","7","9","11","13","sus4",get_alt()]]

def get_chord(Key,Exts,i):
    #Key is a list containing the notes of the tonic scale
    #Exts is either MajorExts or MinorExts depending on the key tonality
    return "|" + Key[i] + random.choice(Exts[i])

def get_major_key_chord(Key):
    return get_chord(Key,MajorExts,random.randint(0,6))

def get_minor_key_chord(Key):
    return get_chord(Key,MinorExts,random.randint(0,6))

def get_time():
    return random.choice([["3/4  ", 3],["4/4  ", 4],["5/4  ", 5],["2/2  ", 2],["6/8  ", 2],["12/8 ", 4]])

def get_bars():
    return random.choice([8, 10, 12])

# tritone substitution on the tonic chord

def tritone_substitution(RootIndex, Key):
    # RootIndex is the chromatic scale index of the tonic note
    # Key is the list of tonic scale notes
    Exts = ["7","9","11","13","aug","sus4",get_alt()]
    if "#" in "".join(Key):
        NewRoot = SharpNotes[RootIndex + 1]
    else:
        NewRoot = FlatNotes[RootIndex + 1]
    return "|" + NewRoot + random.choice(Exts)

# diminished chord one semitone above the tonic for passing between I and ii

def passing_dim(RootIndex, Key):
    # RootIndex is the chromatic scale index of the tonic note
    # Key is the list of tonic scale notes
    if "#" in "".join(Key):
        NewRoot = SharpNotes[RootIndex + 1]
    else:
        NewRoot = FlatNotes[RootIndex + 1]
    return "|" + NewRoot + random.choice(MajorExts[6])

# create a chord sequence using secondary chords on a diatonic note
# not designed for approaching the diatonic diminished chord

def major_secondary(RootIndex, NewRootDegree, Key, *NewKeyDegrees):
    #RootIndex is the chromatic scale index of the original tonic note
    #NewRootDegree the scale degree we are approaching (eg. 5 for ii/V)
    #ApproachDegree is the degree we approach from relative to the NewRootDegree (eg. 2 for ii/V)
    #Key is the list of notes in the tonic scale

    if NewRootDegree in [1,4,5]:
        ScaleFunc = get_major_scale
        IsMajor = True
    else:
        ScaleFunc = get_minor_scale
        IsMajor = False
        
    ChromaticDistance = [0,2,4,5,7,9,11][NewRootDegree - 1]
    NewRootIndex = (RootIndex + ChromaticDistance) % 12
    
    NewKey = ScaleFunc(NewRootIndex)
    
    if IsMajor and NewRootIndex in [1,6,11]:
        if "#" in "".join(Key):
            NewKey = get_sharps_scale(NewRootIndex)
        else:
            NewKey = get_flats_scale(NewRootIndex)

    if (not IsMajor) and NewRootIndex in [3, 8, 10]:
        if "#" in "".join(Key):
            NewKey = (2*get_sharps_scale((NewRootIndex+3)%12))[5:12]
        else:
            NewKey = (2*get_flats_scale((NewRootIndex+3)%12))[5:12]
    L = []
    for x in NewKeyDegrees:
        L.append("|" + NewKey[x - 1] + random.choice(MajorExts[x - 1]))
    return "".join(L)

def minor_secondary(RootIndex, NewRootDegree, Key, *NewKeyDegrees):
    #RootIndex is the chromatic scale index of the original tonic note
    #NewRootDegree the scale degree we are approaching (eg. 5 for ii/V)
    #NewKeyDegrees give the chord sequence erlative to the new key eg for vi/V | ii/V | V/V | V -> 6,2,5,1
    #Key is the list of notes in the original tonic scale

    if NewRootDegree in [1,4,5]:
        ScaleFunc = get_minor_scale
        IsMinor = True
    else:
        ScaleFunc = get_major_scale
        IsMinor = False
        
    ChromaticDistance = [0,2,3,5,7,8,10][NewRootDegree - 1]
    NewRootIndex = (RootIndex + ChromaticDistance) % 12
    
    NewKey = ScaleFunc(NewRootIndex)
    
    if IsMinor and NewRootIndex in [3,8,10]:
        if "#" in "".join(Key):
            NewKey = (2*get_sharps_scale((NewRootIndex+3)%12))[5:12]
        else:
            NewKey = (2*get_flats_scale((NewRootIndex+3)%12))[5:12]
    
    if (not IsMinor) and NewRootIndex in [1, 6, 11]:
        if "#" in "".join(Key):
            NewKey = get_sharps_scale(NewRootIndex)
        else:
            NewKey = get_flats_scale(NewRootIndex)
    
    L = []
    for x in NewKeyDegrees:
        L.append("|" + NewKey[x - 1] + random.choice(MinorExts[x - 1]))
    return "".join(L)

def major_secondary_dominant(RootIndex, Key):
    return major_secondary(RootIndex, random.randint(1,6), Key, 5, 1)

def minor_secondary_dominant(RootIndex, Key):
    return minor_secondary(RootIndex, random.choice([2,7]), Key, 5, 1)

def major_minor_four(Key):
    majorfour = "|" + Key[3] + random.choice(MajorExts[3])
    minorfour = "|" + Key[3] + random.choice(MinorExts[3])
    return majorfour + minorfour

def major_two_bar(RootIndex, Key):
    return random.choice([major_secondary_dominant(RootIndex, Key), major_minor_four(Key)])


  

def major_four_bar(RootIndex, Key):
    a = get_chord(Key, MajorExts, 2) + major_secondary(RootIndex, 2, Key, 5, 1)
    b = get_chord(Key, MajorExts, 0) + passing_dim(RootIndex, Key) + get_chord(Key, MajorExts, 1)
    c = get_chord(Key, MajorExts, 0) + major_secondary(RootIndex, 5, Key, 2, 5)
    d = major_secondary(RootIndex, 1, Key, 1, 6, 2)
    e = get_chord(Key, MajorExts, 4)
    f = tritone_substitution(RootIndex, Key)
    return random.choice([a,b,c,d]) + random.choice([e,f])

def minor_four_bar(Key):
    a = ""
    Exts = MinorExts[:]
    Exts[4], Exts[5] = Exts[6], Exts[6]
    for i in [5,4,5,6]: a += get_chord(Key, Exts, i)
    return a

# format performance

def split_list(Performance):
    L = Performance.split("|")[:-1]
    for i in range(1,len(L)):
        while len(L[i]) < 8:
            L[i] += " "
    x = int(len(L)/2) + 1
    L.insert(x,"\n     ")
    L = "|".join(L) + "|"
    return L