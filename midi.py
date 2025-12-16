import rtmidi
import time
import random

# Initialize MIDI output
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print("Available MIDI ports:", available_ports)

# Open IAC Driver (Mac virtual MIDI)
for i, port in enumerate(available_ports):
    if "IAC" in port or "GarageBand" in port:
        midiout.open_port(i)
        print(f"Connected to {port}")
        break
else:
    print("⚠️ No IAC Driver found — creating virtual port instead.")
    midiout.open_virtual_port("GestureStylophone")

def play_note(note, duration=0.15):
    """Play a single MIDI note"""
    velocity = random.randint(60, 120)
    midiout.send_message([0x90, note, velocity])  # Note ON
    time.sleep(duration)
    midiout.send_message([0x80, note, 0])         # Note OFF

def send_cc(cc, value):
    value = max(0, min(127, int(value)))
    midiout.send_message([0xB0, cc, value])


