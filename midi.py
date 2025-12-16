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

# Play random notes for a few seconds
print("🎹 Sending test notes...")

try:
    notes = [58, 56, 54, 51, 54, 56 ,58]  # C major scale
    for note in notes:
            velocity = random.randint(60, 120)
            midiout.send_message([0x90, note, velocity])  # Note ON
            print(f"Note ON: {note}")
            time.sleep(1.3)
            midiout.send_message([0x80, note, 0])  # Note OFF
            time.sleep(1.3)
except KeyboardInterrupt:
    print("Stopped.")
