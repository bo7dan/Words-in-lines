import datetime
from rich.console import Console

console = Console()

ASCII_ART = r"""
[yellow]
    _    _                           _                  __           
  F L  J J     ____     _ ___    ___FJ     ____        LJ   _ ___   
 J J .. L L   F __ J   J '__ ", F __  L   F ___J           J '__ J  
 | |/  \| |  | |--| |  | |__|-J| |--| |  | '----_      FJ  | |__| | 
 F   /\   J  F L__J J  F L  `-'F L__J J  )-____  L    J  L F L  J J 
J___//\\___LJ\______/FJ__L    J\____,__LJ\______/F    J__LJ__L  J__L
|___/  \___|_J______F |__L     J____,__F J______F     |__||__L  J__|
  FJ       LJ   _ ___      ____      ____                           
 J |           J '__ J    F __ J    F ___J                          
 | |       FJ  | |__| |  | _____J  | '----_                         
 F L_____ J  L F L  J J  F L___--. )-____  L                        
J________LJ__LJ__L  J__LJ\______/FJ\______/F                        
|________||__||__L  J__| J______F  J______F                         
[/yellow]
"""

console.print(ASCII_ART)
class Note:
    def __init__(self, title, text, category):
        self.title = title
        self.text = text
        self.category = category
        self.creation_date = datetime.datetime.now()

    def __str__(self):
        return f"Title: {self.title}\nСategory: {self.category}\nDate of creation: {self.creation_date}\nText:\n{self.text}\n"



class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, text, category):
        new_note = Note(title, text, category)
        self.notes.append(new_note)

    def view_notes(self):
        if not self.notes:
            print("No notes.")
        else:
            for note in self.notes:
                print(note)
                print("-" * 40)

    def edit_note(self, title, new_text):
        for note in self.notes:
            if note.title == title:
                note.text = new_text
                print("Note edited.")
                return
        print("Note with this title not found.")

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print("Note deleted.")
                return
        print("Note with this title not found.")



def display_menu():
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. Exit")



def main():
    notebook = Notebook()

    while True:
        display_menu()
        choice = input("Оберіть опцію: ")

        if choice == "1":
            title = input("Введіть заголовок нотатки: ")
            text = input("Введіть текст нотатки: ")
            category = input("Введіть категорію нотатки: ")
            notebook.add_note(title, text, category)
            print("Нотатку додано.\n")

        elif choice == "2":
            notebook.view_notes()

        elif choice == "3":
            title = input("Введіть заголовок нотатки для редагування: ")
            new_text = input("Введіть новий текст нотатки: ")
            notebook.edit_note(title, new_text)

        elif choice == "4":
            title = input("Введіть заголовок нотатки для видалення: ")
            notebook.delete_note(title)

        elif choice == "5":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.\n")


if __name__ == "__main__":
    main()
