# Project Folder Creator 🚀

A simple Python tool to generate a project folder and file structure based on a visual tree-style `.txt` file.

---

## 📋 Features

- Parse tree-style text files with indentation or visual tree symbols
- Automatically create deeply nested folders and files
- Supports diagrams with `├──`, `└──`, `│` or indented plain text
- Minimal, dependency-free implementation
- Great for scaffolding new projects, fast!

---

## 📂 Example

### Input (`structure.txt`):

## 📁 Project Structure

project-folder-creator/ ├── assets/ # (Optional screenshots if you want) │ ├── structures/ # Structure templates │ └── cnn_classifier_structure.txt │ ├── .gitignore ├── LICENSE ├── README.md ├── create_structure.py ├── requirements.txt # (Optional - empty if no libraries needed)

yaml
Copy
Edit

### 🛠 Generated Folder Structure:

Same as above — automatically created under the specified path.

---

## 🚀 How to Use

1. **Clone the repository:**

```bash
git clone https://github.com/sashjack0/project-folder-creator.git
cd project-folder-creator
Add a structure definition file (like cnn_classifier_structure.txt) inside the structures/ directory.

Run the script:

bash
Copy
Edit
python create_structure.py
Enter the path where you want the project created.

That's it! ✅

📦 Requirements
Python 3.7+

No external libraries required

📄 License
This project is licensed under the MIT License.
See the LICENSE file for full details.

Happy building! 🛠️🚀