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

# returns the numerical value for the octave of note
# TODO: Some programs treat the midi notes slightly differently
def get_octave(note, octave):
	return notes[note] + (octave * 12)

track = 0
time = 0

# TODO: change these to be something user defined(?)
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time,120)

# track, channel, pitch, time, duration, volume
# MyMIDI.addNote(track, channel, pitch, time, duration, volume)

def write_track(file_name):
	binfile = open(file_name + ".mid", 'wb')
	MyMIDI.writeFile(binfile)
	binfile.close()

def write_major_chord():
	root_note = scales['Cmaj'][randint(0, 6)]
	octave = randint(5, 8)
	MyMIDI.addNote(track, 0, get_octave(root_note, octave), time, 1, 100)
	# TODO: Using % won't work 100% here 
	MyMIDI.addNote(track, 0, get_octave(root_note, octave) + 2, time, 1, 100)
	MyMIDI.addNote(track, 0, get_octave(root_note, octave) + 4, time, 1, 100)

def generate_midi():
	pass

write_major_chord()
write_track("sample")
