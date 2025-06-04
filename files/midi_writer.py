from mido import Message, MidiFile, MidiTrack

note_map = {
    "C2": 36, "D2": 38, "E2": 40, "F2": 41,
    "G2": 43, "A2": 45, "B2": 47,
    "C3": 48, "D3": 50, "E3": 52, "F3": 53,
    "G3": 55, "A3": 57, "B3": 59,
    "C4": 60, "D4": 62, "E4": 64, "F4": 65,
    "G4": 67, "A4": 69, "B4": 71, "C5": 72
}

def save_melody_to_midi(note_names, background_notes=None, filename="melody_out.mid", velocity=64):
    mid = MidiFile()

    # Track dla tła
    if background_notes:
        track_bg = MidiTrack()
        mid.tracks.append(track_bg)
        for item in background_notes:
            if isinstance(item[0], list):
                notes, dur = item
                for note_tuple in notes:
                    note = note_tuple[0] if isinstance(note_tuple, tuple) else note_tuple
                    pitch = note_map.get(note)
                    if pitch:
                        track_bg.append(Message("note_on", note=pitch, velocity=50, time=0))
                for note_tuple in notes:
                    note = note_tuple[0] if isinstance(note_tuple, tuple) else note_tuple
                    pitch = note_map.get(note)
                    if pitch:
                        track_bg.append(Message("note_off", note=pitch, velocity=50, time=dur))
            else:
                if isinstance(item, (tuple, list)) and len(item) == 2:
                    note, dur = item
                    pitch = note_map.get(note)
                    if pitch:
                        track_bg.append(Message("note_on", note=pitch, velocity=50, time=0))
                        track_bg.append(Message("note_off", note=pitch, velocity=50, time=dur))
                else:
                    print(f"Błędny format nuty tła: {item}")
    # Track główny
    track = MidiTrack()
    mid.tracks.append(track)
    for note, dur in note_names:
        if note == "REST":
            track.append(Message("note_on", note=0, velocity=0, time=dur))
        else:
            pitch = note_map.get(note)
            if pitch:
                track.append(Message("note_on", note=pitch, velocity=velocity, time=0))
                track.append(Message("note_off", note=pitch, velocity=velocity, time=dur))

    mid.save(filename)
    print(f"Zapisano plik MIDI: {filename}")
