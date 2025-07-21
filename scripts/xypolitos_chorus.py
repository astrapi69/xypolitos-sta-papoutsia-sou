from midiutil import MIDIFile
from pathlib import Path

def create_midi_with_chords(output_path: Path):
    midi = MIDIFile(1)
    track = 0
    time = 0
    tempo = 70
    channel = 0
    volume = 100

    midi.addTempo(track, time, tempo)

    # Ακόρντα (Gm, Eb, Bb, F) ως τρίφωνα
    chords = [
        [55, 58, 62],   # Gm: G, Bb, D
        [51, 55, 58],   # Eb: Eb, G, Bb
        [46, 50, 53],   # Bb: Bb, D, F
        [53, 57, 60],   # F: F, A, C
    ]
    durations = [4, 4, 4, 4]

    current_time = 0
    for chord, duration in zip(chords, durations):
        for note in chord:
            midi.addNote(track, channel, note, current_time, duration, volume)
        current_time += duration

    with open(output_path, "wb") as f:
        midi.writeFile(f)

    print(f"🎼 Έτοιμο: {output_path.absolute()}")

def create_midi(output_path: Path):
    midi = MIDIFile(1)  # ένα track
    track = 0
    time = 0
    tempo = 70
    channel = 0
    volume = 100

    midi.addTempo(track, time, tempo)

    # Root notes για τα ακόρντα: Gm - Eb - Bb - F
    chord_sequence = [55, 51, 46, 53]  # MIDI notes: G3, Eb3, Bb2, F3
    durations = [4, 4, 4, 4]  # κάθε ένα διαρκεί 4 χτύπους

    current_time = 0
    for note, duration in zip(chord_sequence, durations):
        midi.addNote(track, channel, note, current_time, duration, volume)
        current_time += duration

    with open(output_path, "wb") as f:
        midi.writeFile(f)

    print(f"🎵 MIDI αρχείο δημιουργήθηκε: {output_path.absolute()}")

def main():
    create_midi(Path("../output/xypolitos_chorus.mid"))

if __name__ == "__main__":
    main()
