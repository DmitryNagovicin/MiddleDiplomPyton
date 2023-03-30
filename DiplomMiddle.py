import json
import os
import sys
from datetime import datetime

STORAGE_FILE_NAME = "notes.json"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def load_notes():
    notes = []
    if os.path.exists(STORAGE_FILE_NAME):
        try:
            with open(STORAGE_FILE_NAME, "r") as f:
                notes = json.load(f)
        except:
            print("Failed to load notes from file")
    return notes

def save_notes(notes):
    try:
        with open(STORAGE_FILE_NAME, "w") as f:
            json.dump(notes, f)
    except:
        print("Failed to save notes to file")

def list_notes(notes):
    if not notes:
        print("No notes found")
    else:
        print("List of notes:")
        for note in notes:
            print("{}: {} - {}".format(note["id"], note["title"], note["timestamp"]))

def add_note(notes):
    title = input("Enter note title: ").strip()
    text = input("Enter note text: ").strip()

    # Generate a unique ID for the note
    id = str(len(notes) + 1)

    note = {"id": id, "title": title, "text": text, "timestamp": datetime.now().strftime(DATE_FORMAT)}
    notes.append(note)
    print("Note added")

def edit_note_command(notes, id):
    note = find_note_by_id(notes, id)
    if not note:
        print("Note with id {} not found".format(id))
    else:
        print("Editing note {}: {}".format(note["id"], note["title"]))
        new_title = input("Enter new title (empty to keep current): ").strip()
        new_text = input("Enter new text (empty to keep current): ").strip()

        if new_title:
            note["title"] = new_title
        if new_text:
            note["text"] = new_text

        note["timestamp"] = datetime.now().strftime(DATE_FORMAT)
        print("Note updated")

def delete_note_command(notes, id):
    note = find_note_by_id(notes, id)
    if not note:
        print("Note with id {} not found".format(id))
    else:
        notes.remove(note)
        print("Note deleted")

def find_note_by_id(notes, id):
    for note in notes:
        if note["id"] == id:
            return note
    return None

def main():
    notes = load_notes()

    while True:
        command = input().strip()
        if command == "exit":
            break
        elif command == "list":
            list_notes(notes)
        elif command == "add":
            add_note(notes)
        elif command.startswith("edit "):
            edit_note_command(notes, command[5:].strip())
        elif command.startswith("delete "):
            delete_note_command(notes, command[7:].strip())
        else:
            print("Unknown command: {}".format(command))

    save_notes(notes)

if __name__ == "__main__":
    print("Print command what do you want to do:\n list - view all notes\n add - add new note\n edit ID - change existing note\n delete ID - delet selected note\n exit - end programm\n")
    main()