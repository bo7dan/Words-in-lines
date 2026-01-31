[![License: GPL v3](https://img.shields.io)](https://www.gnu.org)

# 📝 Console Notes Application

A simple but well-structured **console-based notes application** written in Python.  
Designed as a **notes app**, not a todo list.

Notes are grouped into categories automatically and stored persistently in a JSON file.

---

## ✨ Features

- 📌 Add notes with:
  - title
  - text
  - category (created automatically if it doesn’t exist)
- 📂 View notes grouped by categories
- 🗑 Delete individual notes
- 🧹 Empty categories are removed automatically
- 💾 Persistent storage using `notes.json`
- 🎨 Clean and readable console UI using **rich**
- 📜 Licensed under **GNU GPL v3**

---

## 🧭 Menu

1. Add note

2. View notes

3. Delete note

4. Exit

   
The menu is intentionally minimal and action-oriented:
- Categories are **not managed manually**
- The focus is on writing and reading notes

---

## 🛠 Requirements

- Python **3.8+**
- `rich` library

Install dependencies:

```bash
pip install rich
```

  ## ⚖️ License

This project is licensed under the **GNU General Public License v3.0**.

- You are free to copy, modify, and distribute this software.
- Any modifications or derivative works **must also be licensed under GPLv3**.
- For more details, see the [LICENSE](LICENSE) file in this repository.

---
*This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.*


