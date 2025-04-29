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
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/sashjack0/project-folder-creator.git
cd project-folder-creator
```

### 2. Prepare Your Structure File

Place your custom tree-style `.txt` files inside the `structures/` folder.

Example (`cnn_classifier_structure.txt`):

```bash
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
├── training/
│   ├── train.py
│   ├── validate.py
│   └── test.py
├── utils/
│   ├── metrics.py
│   ├── logger.py
│   └── helpers.py
├── tests/
│   ├── test_dataset.py
│   └── test_model.py
└── notebooks/
    └── exploration.ipynb
```

### 3. Run the Script

```bash
python create_structure.py
```

Follow the prompts:
- Select the structure `.txt` file
- Enter the destination path
- Project structure will be created automatically 🎯

---

## 🛠 Requirements

- Python 3.7 or higher
- No external packages needed

---

## 🔐 Security

- Local file and folder creation only — **no network access**
- No sensitive data stored
- Fully offline and secure

---

## 🙌 Contributing

Pull requests are welcome!  
Feel free to open issues to suggest new features, improvements, or report bugs.

---

## 👨‍💻 Author

**Sachin Bhandary**  
*AI Engineer*  
GitHub: [@sashjack0](https://github.com/sashjack0)

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---
