# Copyright (C) 2026 bo7dan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE file for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
import os
import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()
DATA_FILE = "notes.json"


# -------------------- MODELS --------------------

class Note:
    def __init__(self, title, text, created_at=None):
        self.title = title
        self.text = text
        self.created_at = created_at or datetime.datetime.now()

    def to_dict(self):
        return {
            "title": self.title,
            "text": self.text,
            "created_at": self.created_at.isoformat()
        }

    @staticmethod
    def from_dict(data):
        return Note(
            data["title"],
            data["text"],
            datetime.datetime.fromisoformat(data["created_at"])
        )


class Category:
    def __init__(self, name):
        self.name = name
        self.notes = []

    def to_dict(self):
        return {
            "name": self.name,
            "notes": [n.to_dict() for n in self.notes]
        }

    @staticmethod
    def from_dict(data):
        c = Category(data["name"])
        c.notes = [Note.from_dict(n) for n in data["notes"]]
        return c


class Notebook:
    def __init__(self):
        self.categories = {}
        self.load()

    def load(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            for name, cat in data.items():
                self.categories[name] = Category.from_dict(cat)

    def save(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(
                {k: v.to_dict() for k, v in self.categories.items()},
                f,
                indent=4,
                ensure_ascii=False
            )

    # ---------- NOTES API ----------

    def add_note(self, category, title, text):
        if category not in self.categories:
            self.categories[category] = Category(category)
        self.categories[category].notes.append(Note(title, text))
        self.save()

    def delete_note(self, category, title):
        if category not in self.categories:
            return False

        cat = self.categories[category]
        cat.notes = [n for n in cat.notes if n.title != title]

        if not cat.notes:
            del self.categories[category]

        self.save()
        return True


# -------------------- UI --------------------

def header():
    console.print(Panel.fit(
        "[bold cyan]Notebook[/bold cyan]\n[dim]Notes with categories[/dim]",
        border_style="cyan"
    ))


def view_notes(nb: Notebook):
    if not nb.categories:
        console.print("[dim]No notes yet[/dim]")
        return

    for cat in nb.categories.values():
        table = Table(title=f"[bold yellow]{cat.name}[/bold yellow]", show_lines=True)
        table.add_column("Title", style="bold")
        table.add_column("Created", style="dim")
        table.add_column("Text")

        for note in cat.notes:
            table.add_row(
                note.title,
                note.created_at.strftime("%Y-%m-%d %H:%M"),
                note.text
            )

        console.print(table)


def menu():
    console.print("""
[bold]1[/bold] Add note
[bold]2[/bold] View notes
[bold]3[/bold] Delete note
[bold]4[/bold] Exit
""")


def main():
    nb = Notebook()
    header()

    while True:
        menu()
        choice = Prompt.ask("Choose", choices=["1", "2", "3", "4"])

        if choice == "1":
            nb.add_note(
                Prompt.ask("Category"),
                Prompt.ask("Title"),
                Prompt.ask("Text")
            )

        elif choice == "2":
            view_notes(nb)

        elif choice == "3":
            ok = nb.delete_note(
                Prompt.ask("Category"),
                Prompt.ask("Title")
            )
            if not ok:
                console.print("[red]Note not found[/red]")

        elif choice == "4":
            console.print("[green]Bye 👋[/green]")
            break


if __name__ == "__main__":
    main()
