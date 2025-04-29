<<<<<<< HEAD
# Project Folder Creator 🚀

A simple Python tool to generate a project folder and file structure based on a visual tree-style `.txt` file.

## 📋 Features

- Parse tree-style text files easily
- Create nested folders and files automatically
- Supports visual tree diagrams (├──, └──, │) as input
- Cleans up output for professional use
- Very lightweight and fast

## 📂 Example

Input (`cnn_classifier_structure.txt`):

cnn-image-classifier/ ├── README.md ├── LICENSE ├── requirements.txt ├── configs/ │ └── config.yaml ├── datasets/ │ └── dataset.py ├── models/ │ └── cnn_model.py ...

vbnet
Copy
Edit

Generated project structure:

cnn-image-classifier/ ├── README.md ├── LICENSE ├── requirements.txt ├── configs/ │ └── config.yaml ├── datasets/ │ └── dataset.py ├── models/ │ └── cnn_model.py ...

yaml
Copy
Edit

## 🚀 How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/project-folder-creator.git
    cd project-folder-creator
    ```

2. Place your structure `.txt` files inside the `structures/` folder.

3. Run the script:
    ```bash
    python create_structure.py
    ```

4. Enter the path where you want the project created.

That's it!

## 🛠 Requirements

- Python 3.7+

(No additional libraries required.)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy building! 🚀**

