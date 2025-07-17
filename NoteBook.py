class NoteBook:

    def __init__(self):
        self.notes = {}

    def add_notes(self, title, description):
        self.notes[title] = description


def