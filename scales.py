import gradefuncs

# Grade six scale functions

def get_harmonic_minor():
    return gradefuncs.get_note() + " Harmonic Minor"

def get_dorian():
    return gradefuncs.get_note() + " Dorian"

def get_mixolydian():
    return gradefuncs.get_note() + " Myxolydian"

def get_chromatic():
    return gradefuncs.get_note() + " Chromatic"

def get_two_octave_major():
    return gradefuncs.get_note_Gb_D() + " Major, Two Octaves"

def get_two_octave_minor():
    return gradefuncs.get_note_Gb_D() + " Minor, Two Octaves"

def get_major_eighths():
    return gradefuncs.get_note_F_D() + " Major in 8ths"

# Grade seven scale functions

def get_lydian():
    return gradefuncs.get_note() + " Lydian"

def get_whole_tone():
    return gradefuncs.get_note() + " Whole Tone"

def get_major_tenths():
    return gradefuncs.get_note_F_A() + " Major in 10ths"

# Grade eight scale functions

def get_blues():
    return gradefuncs.get_note_Gb_D() + " Blues, Two Octaves"

def get_pent_major():
    return gradefuncs.get_note_Gb_D() + " Pentatonic Major, Two Octaves"

def get_pent_minor():
    return gradefuncs.get_note_Gb_D() + " Pentatonic Minor, Two Octaves"

def get_minor_eighths():
    return gradefuncs.get_note_F_D() + " Minor in 8ths"