from midiutil.MidiFile import MIDIFile
from random import randint

MyMIDI = MIDIFile(1)

# Every possible note
notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

# s -> sharp
(C,Cs,D,Ds,E,F,Fs,G,Gs,A,As,B) = 0,1,2,3,4,5,6,7,8,9,10,11

scales = {\
	'Cmaj' : [C, D, E, F, G, A, B]
}

(I,ii,iii,IV,V,vi,viio) = 0,1,2,3,4,5,6

global_chords_in_scale = {\
'Cmaj' : [['Cmaj', 'Cmaj7'], ['Dmin', 'Dmin7'], ['Emin', 'Emin7'],\
		  ['Fmaj', 'Fmaj7'], ['Gmaj', 'Gdom7'], ['Amin', 'Amin7'],\
		  ['Bdim', 'Bmin7b5']]
}

global_chords = {\
	'Amaj'    : [],\
	'Amaj7'   : [],\
	'Amin'    : [A, C, E],\
	'Amin7'   : [A, C, E, G],\
	'Bmaj'    : [],\
	'Bmaj7'   : [],\
	'Bmin'    : [],\
	'Bmin7'   : [],\
	'Bdim'    : [B, D, F],\
	'Bmin7b5' : [B, D, F, A],\
	'Cmaj'    : [C, E, G],\
	'Cmaj7'   : [C, E, G, B],\
	'Cmin'    : [],\
	'Cmin7'   : [],\
	'Dmaj'    : [],\
	'Dmaj7'   : [],\
	'Dmin'    : [D, F, A],\
	'Dmin7'   : [D, F, A, C],\
	'Emaj'    : [],\
	'Emaj7'   : [],\
	'Emin'    : [E, G, B],\
	'Emin7'   : [E, G, B, D],\
	'Fmaj'    : [F, A, C],\
	'Fmaj7'   : [F, A, C, E],\
	'Fmin'    : [],\
	'Fmin7'   : [],\
	'Gmaj'    : [G, B, D],\
	'Gmaj7'   : [G, B, D, F],\
	'Gmin'    : [],\
	'Gmin7'   : [],\
	'Gdom7'   : [G, B, D, F]
}

# TODO: Need this to be able to be set by the user
global_key = 'Cmaj'

# returns the numerical value for the octave of note
# TODO: Some programs treat the midi notes slightly differently
def get_octave(note, octave):
	return note + (octave * 12)

(track, time, channel, volume) = 0, 0, 0, 100

# TODO: change these to be something user defined(?)
MyMIDI.addTrackName(track, time, "Midi Track")
MyMIDI.addTempo(track, time, 78)

# track, channel, pitch, time, duration, volume
# MyMIDI.addNote(track, channel, pitch, time, duration, volume)

def write_midi_file(file_name):
	binfile = open(file_name + ".mid", 'wb')
	MyMIDI.writeFile(binfile)
	binfile.close()

def generate_chord_progression():
	chords = []

	# Number of chords 
	num_chords = randint(2, 4)

	# This should be moved over to a markov chain
	for i in xrange(num_chords):
		chords.append(randint(I, viio))

	chord_progression = []

	for chord in chords:
		append_chord = global_chords_in_scale[global_key][chord][randint(0,1)]
		chord_progression.append(global_chords[append_chord])

	return chord_progression

def write_chord_progression():
	chords = generate_chord_progression()

	duration = 4 / len(chords)
	time = 0

	for chord in chords:
		print chord
		for note in chord:
			MyMIDI.addNote(track, channel, get_octave(note, randint(4,5)), time, duration, volume)
		time += duration

	write_midi_file("sample")

write_chord_progression()
