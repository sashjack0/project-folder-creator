# 🗂️ Project Folder Creator

![Python](https://img.shields.io/badge/built%20with-Python-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/status-Production--Ready-brightgreen)

> Instantly create folder and file structures from tree-style `.txt` templates — clean, fast, and dependency-free.

---

## 📌 Features

- 📂 Parse visual tree-style text files (├──, └──, │ symbols supported)
- 🏗️ Automatically create nested folders and files
- ⚡ Lightweight and fast — no external libraries required
- 🛠️ Perfect for scaffolding new projects instantly

---

## 📁 Project Structure

```bash
project-folder-creator/
├── assets/                  # (Optional screenshots if needed)
│
├── structures/               # Structure templates
│   └── cnn_classifier_structure.txt
│
├── .gitignore
├── LICENSE
├── README.md
├── create_structure.py
├── requirements.txt          # (Optional - empty if no libraries needed)
🚀 How to Use
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/sashjack0/project-folder-creator.git
cd project-folder-creator
2. Add Your Structure .txt File
Place your custom tree-style .txt files inside the structures/ folder.

Example (cnn_classifier_structure.txt):

bash
Copy
Edit
cnn-image-classifier/
├── README.md
├── LICENSE
├── requirements.txt
├── configs/
│   └── config.yaml
├── datasets/
│   └── dataset.py
├── models/
│   └── cnn_model.py
...
3. Run the Script
bash
Copy
Edit
python create_structure.py
Follow the prompts:

Select the structure file

Enter the destination path

Watch your project structure generate instantly 🎯

🛠 Requirements
Python 3.7+

No external packages needed

🔐 Security
Local folder/file creation only — no network access

No user data stored or transmitted

Safe for offline use

🙌 Contributing
Pull requests are welcome!
If you have ideas for new features or improvements, feel free to open an issue.

👨‍💻 Author
Sachin Bhandary
Prompt Engineer & AI Tool Developer
GitHub: @sashjack0

📄 License
Licensed under the MIT License.

