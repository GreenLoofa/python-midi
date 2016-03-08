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
MyMIDI.addTrackName(track,time,"Midi Track")
MyMIDI.addTempo(track,time,120)

# track, channel, pitch, time, duration, volume
# MyMIDI.addNote(track, channel, pitch, time, duration, volume)

def write_midi_file(file_name):
	binfile = open(file_name + ".mid", 'wb')
	MyMIDI.writeFile(binfile)
	binfile.close()

def generate_chord():
	chord = []

	note_index = randint(0, 6)

	# Root Note:
	chord[0] = scales[global_key][note_index]

	# Currently only generates 2 other notes for the chord
	chord[1] = chord[(note_index+2)%6]
	chord[2] = chord[(note_index+4)%6]

	return chord

def generate_midi():
	pass

write_midi_file("sample")
