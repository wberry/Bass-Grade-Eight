import random
import gradefuncs

# Grade six

# Musical knowledge

# The candidate should be able to name any note given its string and fret number

def name_note():
    string = random.choice(["E","A","D","G"])
    fret = random.choice(range(25))
    return f'Fret {fret} on the {string} string'

# The candidate should be able to name diatonic major scale intervals up to the major 9th

def name_interval():
    key = gradefuncs.major()
    print(key)
    root = key[0]
    note = random.choice(key)
    if note == key[1]:
        note += random.choice([""," (up an octave)"])
    return f'{root} to {note}'

# The candidate must explain repeat and dynamic markings

def explain_markings():
    repeat = ["D.S. (Dal Segno)", "D.C. (Da Capo)", "Al Coda", "first and second time endings"]
    dynamic = ["ppp","pp","p","mp","mf","f","ff","fff","<",">"]
    tempo = ["Accel. (accelerando)", "Rall. (rallentando)", "A tempo", "fermata (pause)"]
    marking = random.choice(random.choice([repeat, dynamic, tempo]))
    return f'Explain what is meant by "{marking}"'

# The candidate should be familiar with common chords in a key

def name_chord():
    position = random.choice(["I","II","III","IV","V","VI"])
    key = gradefuncs.get_note()
    return f'Name the chord built from position {position} in the key of {key}'

# Playing the bass guitar

def explain_vibrato():
    return 'Explain the four ways of executing vibrato'

# Knowledge of the instrument

def explain_parts():
    term = random.choice(["action", "marker dots", "the nut", "the saddle", "changing a string", "tuning the bass guitar"])
    return f'Explain the following term: "{term}"'

print(explain_parts())