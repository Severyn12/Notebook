'''This module interacts with the user'''
import notebook


NOTE_LIST = notebook.Notebook()

class Menu:
    '''A menu module for Notebook'''
    def __init__(self):
        '''
        Creates a new class Menu object.
        >>> Menu().notebook.notes
        []
        '''
        global NOTE_LIST
        self.notebook = NOTE_LIST
        self.options = {
        "1": self.change_note,
        "2": self.create_note,
        "3": self.find_notes,
        "4": self.show_notes
        }

    def display(self):
        '''
        Prints on the screen notebook's menu.
        Returns nothing.
        >>> len(Menu().display())
        185
        '''
        menu = """Here you can see a Notebook Menu:
        1. Change an old Note
        2. Create a new Note
        3. Search Notes
        4. See all Notes
To continue working enter an option number!"""
        return menu


    def start(self):
        '''Display the menu and calls a method based on the info
        received from a user.'''
        print(self.display())
        choice = input("Enter an option: ")
        while True:
            if (not choice.isdigit()) or not 0 < int(choice) < 5:
                print('Something went wront! Try again!')
                choice = input('Enter here: ')
                continue
            break
        print()
        self.options[choice]()


    def show_notes(self,notes = None):
        '''
        Show notes to a user
        >>> data = Menu()
        >>> data.notebook.new_note('Data','#1')
        >>> data.show_notes()
        Here you can see your notes!
        Note id: 1
        Note tag: #1
        Note data: Data
        '''
        if notes:
            data = notes
        else:
            data = self.notebook.notes
        print('Here you can see your notes!')
        for note in data:
            print(f"Note id: {note.id_num}\nNote tag: {note.tags}\
\nNote data: {note.memo}")


    def find_notes(self):
        '''Finds a note for user.'''
        key = input("Enter a search parameter: ")
        notes = self.notebook.search(key)
        self.show_notes(notes)


    def create_note(self):
        '''Creates a new note'''
        topic = input("Enter a note data and its tag (Data;tag): ")
        while True:
            if not ';' in topic:
                print('Something went wront! Try again!')
                topic = input('Enter here: ')
                continue
            break
        info = topic.split(';')
        self.notebook.new_note(info[0].strip(),info[1].strip())
        print("Note was successfully created.")


    def change_note(self):
        '''Changes a note'''
        id_num = input("Enter a note id you want to change: ")
        memo = input("Enter a memo (can skip): ")
        tags = input("Enter tags (can skip): ")
        if memo:
            self.notebook.modify_memo(id_num, memo)
        if tags:
            self.notebook.modify_tags(id_num, tags)



if __name__ == "__main__":
    print("Nice to see you here again! Let's start!")
    while True:
        Menu().start()
        print('\nDo you want to continue?')
        verbose = input('Enter here(Yes/No): ')
        while True:
            if verbose not in ('Yes','No'):
                print('Something went wront! Try again!')
                verbose = input('Enter here: ')
                continue
            break
        if verbose == 'Yes':
            print("Let's do it again!")
            continue
        break
