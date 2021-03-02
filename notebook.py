'''In this module was implemented a
simple NoteBook'''

import datetime


UNIQUE_NUM = 0
class Note:
    '''Class for creating notes for a NoteBook.'''
    def __init__(self, data, tag=''):
        '''creates a note class object. Also set the note's
        creation date and gives to it a unique id.
        >>> Note('Hello','Dear Friend').tags
        'Dear Friend'
        >>> Note('Hello','Dear Friend').memo
        'Hello'
        '''
        self.memo = data
        self.tags = tag
        self.creation_date = datetime.date.today()
        global UNIQUE_NUM
        UNIQUE_NUM += 1
        self.id_num = UNIQUE_NUM


    def match(self, key):
        '''Checks if the note contains the key
        text, it can be a tag or simply the text of the note.
        >>> Note('Exercise','Homework').match('Homework')
        True
        '''
        return key in self.memo or key in self.tags


class Notebook:
    '''NoteBook class, makes operations with notes'''
    def __init__(self):
        '''Creates a notebook class object with an empty list.
        >>> Notebook().notes
        []
        '''
        self.notes = []


    def new_note(self, info, key_word=''):
        '''Create a new note and add it to the Notebook memory.
        Kye_word it's simply a tag.
        >>> data = Notebook()
        >>> data.new_note('Wrote a topic','')
        >>> len(data.notes)
        1
        '''
        self.notes.append(Note(info, key_word))


    def modify_memo(self, note_id, note_text):
        '''Modifies note text, by replacing it
        with the given value.
        >>> my_notebook = Notebook()
        >>> my_notebook.new_note('Data')
        >>> note_num = my_notebook.notes[0].id_num
        >>> my_notebook.modify_memo(note_num,'Work')
        >>> my_notebook.notes[0].memo
        'Work'
        '''
        check = 0
        for note in self.notes:
            if note.id_num == int(note_id):
                note.memo = note_text
                check = 1
                break
        if not check:
            print('Something wrong with id!')


    def modify_tags(self, note_num, value):
        '''Modifies note tag, by replacing it
        with the given value.
        >>> my_notebook = Notebook()
        >>> my_notebook.new_note('Info')
        >>> note_num = my_notebook.notes[0].id_num
        >>> my_notebook.modify_tags(note_num,'#1')
        >>> my_notebook.notes[0].tags
        '#1'
        '''
        check = 0
        for note in self.notes:
            if note.id_num == int(note_num):
                note.tags = value
                check = 1
                break
        if not check:
            print('Something wrong with id!')
        
        


    def search(self, note_filter):
        '''Find all notes that contain note_filter(string).
        >>> my_notebook = Notebook()
        >>> my_notebook.new_note('Info','second')
        >>> my_notebook.search('Info')[0].memo
        'Info'
        '''
        return [note for note in self.notes if
        note.match(note_filter)]
