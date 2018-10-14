import gradefuncs

# Grade six arpeggios

# arpeggios in two positions

def get_aug_fifth():
    return gradefuncs.get_note_A_Gb() + " Augmented 5th, Two Positions"

def get_dim_seven():
    return gradefuncs.get_note_A_Gb() + " Diminished 7th, Two Positions"

def get_major_nine():
    return gradefuncs.get_note_A_Gb() + " Major 9th, Two Positions"

def get_minor_nine():
    return gradefuncs.get_note_A_Gb() + " Minor 9th, Two Positions"

def get_dom_nine():
    return gradefuncs.get_note_A_Gb() + " Dominant 9th, Two Positions"

# arpeggios and inversions

def get_major_root():
    return gradefuncs.get_inv_arp(gradefuncs.get_major, 0)

def get_major_first_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_major, 1)

def get_major_second_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_major, 2)

def get_minor_root():
    return gradefuncs.get_inv_arp(gradefuncs.get_minor, 0)

def get_minor_first_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_minor, 1)

def get_minor_second_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_minor, 2)

# Grade seven arpeggios

# arpeggios in three positions

def get_major():
    return gradefuncs.get_note_B_Gb() + " Major, Three Positions"

def get_minor():
    return gradefuncs.get_note_B_Gb() + " Minor, Three Positions"

def get_sus_four():
    return gradefuncs.get_note_B_Gb() + " Suspended 4th, Three Positions"

def get_major_six():
    return gradefuncs.get_note_B_Gb() + " Major 6th, Three Positions"

def get_minor_six():
    return gradefuncs.get_note_B_Gb() + " Minor 6th, Three Positions"

def get_major_seven():
    return gradefuncs.get_note_B_Gb() + " Major 7th, Three Positions"

def get_minor_seven():
    return gradefuncs.get_note_B_Gb() + " Minor 7th, Three Positions"

def get_dom_seven():
    return gradefuncs.get_note_B_Gb() + " Dominant 7th, Three Positions"

# arpeggios with altered chord tones

def get_minor_seven_flat_five():
    return gradefuncs.get_minor_seven_ext(0)

def get_minor_seven_sharp_five():
    return gradefuncs.get_minor_seven_ext(1)

def get_minor_seven_flat_nine():
    return gradefuncs.get_minor_seven_ext(2)

def get_minor_seven_flat_five_flat_nine():
    return gradefuncs.get_minor_seven_ext(4)

def get_minor_seven_sharp_five_flat_nine():
    return gradefuncs.get_minor_seven_ext(6)

def get_dom_seven_flat_five():
    return gradefuncs.get_dom_seven_ext(0)

def get_dom_seven_sharp_five():
    return gradefuncs.get_dom_seven_ext(1)

def get_dom_seven_flat_nine():
    return gradefuncs.get_dom_seven_ext(2)

def get_dom_seven_sharp_nine():
    return gradefuncs.get_dom_seven_ext(3)

def get_dom_seven_flat_five_flat_nine():
    return gradefuncs.get_dom_seven_ext(4)

def get_dom_seven_flat_five_sharp_nine():
    return gradefuncs.get_dom_seven_ext(5)

def get_dom_seven_sharp_five_flat_nine():
    return gradefuncs.get_dom_seven_ext(6)

def get_dom_seven_sharp_five_sharp_nine():
    return gradefuncs.get_dom_seven_ext(7)

# arpeggios over 2 octaves

def get_two_octave_major():
    return gradefuncs.get_note_Gb_D() + " Major, Two Octaves"

def get_two_octave_minor():
    return gradefuncs.get_note_Gb_D() + " Minor, Two Octaves"

# Grade eight arpeggios

# extended dominant arpeggios

def get_dom_eleven():
    return gradefuncs.get_note_Gb_D() + " Dominant 11th"

def get_dom_thirteen():
    return gradefuncs.get_note_Gb_D() + " Dominant 13th"

# seventh arpeggios and inversions

def get_major_seven_root():
    return gradefuncs.get_inv_arp(gradefuncs.get_major_seven, 0)

def get_major_seven_first_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_major_seven, 1)

def get_major_seven_second_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_major_seven, 2)

def get_major_seven_third_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_major_seven, 3)

def get_minor_seven_root():
    return gradefuncs.get_inv_arp(gradefuncs.get_minor_seven, 0)

def get_minor_seven_first_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_minor_seven, 1)

def get_minor_seven_second_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_minor_seven, 2)

def get_minor_seven_third_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_minor_seven, 3)

def get_dom_seven_root():
    return gradefuncs.get_inv_arp(gradefuncs.get_dom_seven, 0)

def get_dom_seven_first_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_dom_seven, 1)

def get_dom_seven_second_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_dom_seven, 2)

def get_dom_seven_third_inv():
    return gradefuncs.get_inv_arp(gradefuncs.get_dom_seven, 3)

# arpeggios with altered chord tones in two positions

def get_minor_seven_flat_five():
    return gradefuncs.get_minor_seven_ext(0) + ", Two Positions"

def get_minor_seven_sharp_five():
    return gradefuncs.get_minor_seven_ext(1) + ", Two Positions"

def get_minor_seven_flat_nine():
    return gradefuncs.get_minor_seven_ext(2) + ", Two Positions"

def get_minor_seven_flat_five_flat_nine():
    return gradefuncs.get_minor_seven_ext(4) + ", Two Positions"

def get_minor_seven_sharp_five_flat_nine():
    return gradefuncs.get_minor_seven_ext(6) + ", Two Positions"

def get_dom_seven_flat_five():
    return gradefuncs.get_dom_seven_ext(0) + ", Two Positions"

def get_dom_seven_sharp_five():
    return gradefuncs.get_dom_seven_ext(1) + ", Two Positions"

def get_dom_seven_flat_nine():
    return gradefuncs.get_dom_seven_ext(2) + ", Two Positions"

def get_dom_seven_sharp_nine():
    return gradefuncs.get_dom_seven_ext(3) + ", Two Positions"

def get_dom_seven_flat_five_flat_nine():
    return gradefuncs.get_dom_seven_ext(4) + ", Two Positions"

def get_dom_seven_flat_five_sharp_nine():
    return gradefuncs.get_dom_seven_ext(5) + ", Two Positions"

def get_dom_seven_sharp_five_flat_nine():
    return gradefuncs.get_dom_seven_ext(6) + ", Two Positions"

def get_dom_seven_sharp_five_sharp_nine():
    return gradefuncs.get_dom_seven_ext(7) + ", Two Positions"
