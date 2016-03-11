from midiutil.MidiFile import MIDIFile
from random import randint

MyMIDI = MIDIFile(1)

notes = {\
'C' : 0, 'C#' : 1, \
'D' : 2, 'D#' : 3, \
'E' : 4, \
'F' : 5, 'F#' : 6, \
'G' : 7, 'G#' : 8, \
'A' : 9, 'A#' : 10, 
'B' : 11 }

scales = {\
'Cmaj' : ['C', 'D', 'E', 'F', 'G', 'A', 'B']\
}

# TODO: Need this to be able to be set by the user
global_key = 'Cmaj'

# returns the numerical value for the octave of note
# TODO: Some programs treat the midi notes slightly differently
def get_octave(note, octave):
	return notes[note] + (octave * 12)

track = 0
time = 0

# TODO: change these to be something user defined(?)
MyMIDI.addTrackName(track, time, "Midi Track")
MyMIDI.addTempo(track, time, 78)

# track, channel, pitch, time, duration, volume
# MyMIDI.addNote(track, channel, pitch, time, duration, volume)

def write_midi_file(file_name):
	binfile = open(file_name + ".mid", 'wb')
	MyMIDI.writeFile(binfile)
	binfile.close()

def generate_chord():
	chord = []
	# TODO: Give list of midi numbers instead of strings for the pitches

	note_index = randint(0, 6)

	# TODO: Generate chords with variable octaves
	# Root Note:
	chord.append(get_octave(scales[global_key][note_index], randint(4, 5)))

	# Currently only generates 2 other notes for the chord
	chord.append(get_octave(scales[global_key][(note_index+2)%6], randint(4, 5)))
	chord.append(get_octave(scales[global_key][(note_index+4)%6], randint(4, 5)))

	return chord

def generate_chord_progression():
	chord_progression = []

	# Randomly pick a 2 -> 4 chord progression
	num_chords = randint(2, 4)

	# Add chords to the chord progression (2 -> 4 chords)
	# TODO: Make it so that two of the same/similar chords can't follow right after the other
	for i in xrange(num_chords):
		chord_progression.append(generate_chord())

	track = 0
	channel = 0
	time = 0

	# TODO: Need a simpler function to generate chords no matter the number of chords (if possible)

	if (num_chords == 2):
		for chord in chord_progression:
			for note in chord:
				MyMIDI.addNote(track, channel, note, time, 2, 100)
			time += 2
	elif (num_chords == 3):
		for chord in chord_progression:
			for note in chord:
				MyMIDI.addNote(track, channel, note, time, 1, 100)
			time += 1

	elif (num_chords == 4):
		for chord in chord_progression:
			for note in chord:
				MyMIDI.addNote(track, channel, note, time, 1, 100)
			time += 1

	return chord_progression

print generate_chord_progression()
write_midi_file("sample")
