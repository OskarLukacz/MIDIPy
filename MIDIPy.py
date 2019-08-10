import mido
import time
import rtmidi
import rtmidi.midiutil

rtmidi.midiutil.list_output_ports(api=rtmidi.API_UNSPECIFIED)

midiout = rtmidi.MidiOut()
midiout.open_port(1)

note_on = [0x90, 60, 120] # channel 1, middle C, velocity 112
note_off = [0x80, 60, 0]
midiout.send_message(note_on)
time.sleep(.5)
midiout.send_message(note_off)
time.sleep(.5)
midiout.send_message(note_on)
time.sleep(.5)
midiout.send_message(note_off)

lines = []
raw_genome = ''

with open('fulldata.txt', 'rt') as data:
    for line in data:
        words = line.split()
        lines.append(words)

for l in lines:
    l.pop(0)
    ul = ''
    for w in l:
        ul += w
    raw_genome += ul

translate = {
        'a': 60,
        't': 63,
        'g': 65,
        'c': 67
}

to_notes = {
        60: 'C',
        63: 'D#',
        65: 'F',
        67: 'G'
}

while True:
    try:
        c = raw_genome[0]
        note = translate.get(c, 60)
        print("Base: ", c, "Playing: ", to_notes.get(note, 'C'))
        note_on = [0x90, note, 120]
        note_off = [0x80, note, 0]
        midiout.send_message(note_on)
        time.sleep(.2)
        midiout.send_message(note_off)
        raw_genome = raw_genome[1:]
    except IndexError:
        del midiout






