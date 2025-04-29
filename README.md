# Project Folder Creator 🚀

A simple Python tool to generate a complete project folder and file structure based on a visual tree-style `.txt` file.

---

## 📋 Features

- Parse tree-style text files easily (supports ├──, └──, │ formats)
- Automatically create nested folders and files
- Lightweight, no external dependencies
- Helps quickly scaffold new projects
- Beginner-friendly, production-quality code

---

## 📁 Project Structure

```bash
project-folder-creator/
├── assets/                  # (Optional screenshots if you want)
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
Clone the repository:

bash
Copy
Edit
git clone https://github.com/sashjack0/project-folder-creator.git
cd project-folder-creator
Prepare your structure file:

Create a .txt file representing your desired project structure using tree symbols.

Example: See structures/cnn_classifier_structure.txt provided.

Run the tool:

bash
Copy
Edit
python create_structure.py
Follow prompts:

Select the structure file

Enter the path where you want the project created

Done! 🎉

📂 Example Input and Output
Example cnn_classifier_structure.txt:
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
✅ The script will automatically create the entire project structure exactly as shown.

🛠 Requirements
Python 3.7 or higher

No additional libraries needed (pure standard Python)

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

🙌 Contributing
Pull requests are welcome!
Feel free to open issues to suggest new features, improvements, or fixes.

🌟 Acknowledgements
Inspired by the simplicity of tree-based project initialization.

Built with ❤️ for making project setup faster.

Happy building! 🚀