import random
import gradefuncs

def get_major_performance():
    RootIndex = random.randint(0,11)
    Key = gradefuncs.get_major_scale(RootIndex)
    Time = gradefuncs.get_time()
    #NumberOfBeats = Time[1]
    NumberOfBars = gradefuncs.get_bars()
    Performance = Time[0]
    while NumberOfBars > 0:
        if (NumberOfBars%8 == 0 or NumberOfBars%10 == 0 or NumberOfBars%12 == 0) and(random.randint(0,9) > 0):
            Performance += gradefuncs.get_chord(Key,gradefuncs.MajorExts,0)
            NumberOfBars -= 1
            continue
        if NumberOfBars%2==0 and random.randint(0,3)==0:
            Performance += gradefuncs.major_two_bar(RootIndex, Key)
            NumberOfBars -= 2
            continue
        if NumberOfBars%4==0 and random.randint(0,3)==0:
            Performance += gradefuncs.major_four_bar(RootIndex, Key)
            NumberOfBars -= 4
            continue
        Performance += gradefuncs.get_major_key_chord(Key)
        NumberOfBars -= 1
    Performance += "|"
    return gradefuncs.split_list(Performance)

def get_minor_performance():
    RootIndex = random.randint(0,11)
    Key = gradefuncs.get_minor_scale(RootIndex)
    Time = gradefuncs.get_time()
    #NumberOfBeats = Time[1]
    NumberOfBars = gradefuncs.get_bars()
    Performance = Time[0]
    while NumberOfBars > 0:
        if (NumberOfBars%8 == 0 or NumberOfBars%10 == 0 or NumberOfBars%12 == 0) and(random.randint(0,9) > 0):
            Performance += gradefuncs.get_chord(Key,gradefuncs.MinorExts,0)
            NumberOfBars -= 1
            continue
        if NumberOfBars%2==0 and random.randint(0,3)==0:
            Performance += gradefuncs.minor_secondary_dominant(RootIndex, Key)
            NumberOfBars -= 2
            continue
        if NumberOfBars%4==0 and random.randint(0,3)==0:
            Performance += gradefuncs.minor_four_bar(Key)
            NumberOfBars -= 4
            continue
        Performance += gradefuncs.get_minor_key_chord(Key)
        NumberOfBars -= 1
    Performance += "|"
    return gradefuncs.split_list(Performance)

print(get_minor_performance())
