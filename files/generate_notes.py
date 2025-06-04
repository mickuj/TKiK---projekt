from pydub import AudioSegment
import os

NOTE_ORDER = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def get_note_name(base_note, semitone_shift):
    base_index = NOTE_ORDER.index(base_note[:-1])
    octave = int(base_note[-1])
    new_index = base_index + semitone_shift

    while new_index < 0:
        new_index += 12
        octave -= 1
    while new_index >= 12:
        new_index -= 12
        octave += 1

    return NOTE_ORDER[new_index] + str(octave)

def shift_note(file_path, semitones):
    sound = AudioSegment.from_file(file_path)
    new_sample_rate = int(sound.frame_rate * (2.0 ** (semitones / 12.0)))
    shifted = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    return shifted.set_frame_rate(44100)

def generate_notes(base_file, base_note, range_up=12, range_down=12, out_dir="sounds"):
    os.makedirs(out_dir, exist_ok=True)
    for i in range(-range_down, range_up + 1):
        note_name = get_note_name(base_note, i)
        shifted = shift_note(base_file, i)
        shifted.export(os.path.join(out_dir, f"{note_name}.wav"), format="wav")
        print(f"✅ Zapisano: {note_name}.wav")

# Przykład użycia:
# generuje od C3 do C5 na podstawie C4.wav
generate_notes("sounds/C4.wav", "C4", range_up=24, range_down=24)