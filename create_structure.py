import os
import re

def clean_line_symbols(line):
    """Remove tree drawing symbols like ├──, └──, │, ── etc."""
    return re.sub(r'[├└│─]+', '', line)

def read_structure_file(file_path):
    """Smart parser that uses non-alphanumeric leading characters to detect levels and builds full paths with root tracking."""
    structure = []
    current_path = []
    root_folder = None

    # Read all lines first to avoid file pointer issues
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        # Skip empty lines
        line = line.rstrip('\n').rstrip('\r')
        if not line.strip():
            continue

        # Count the indentation level
        raw_line = line
        indent_count = 0
        for char in raw_line:
            if char in '│ ├└─':
                indent_count += 1
            else:
                break
        indent_level = indent_count // 4

        # Clean the line of tree symbols and whitespace
        cleaned_line = clean_line_symbols(line).strip()

        # Remove inline comments
        if '#' in cleaned_line:
            cleaned_line = cleaned_line.split('#')[0].strip()

        if not cleaned_line:
            continue

        print(f"Processing line: '{raw_line}' -> cleaned: '{cleaned_line}' (indent: {indent_level})")  # Debug

        # Handle root folder specially
        if root_folder is None:
            root_folder = cleaned_line.rstrip('/')
            current_path = [root_folder]
            structure.append('/'.join(current_path) + '/')
            continue

        # Reset path to appropriate level based on indentation
        if indent_level == 1:
            current_path = [root_folder]  # Reset to root for level 1
        else:
            # Keep only the path elements up to the current indent level
            current_path = current_path[:indent_level]

        # Check if it's a directory
        is_directory = False
        if cleaned_line.endswith('/'):
            is_directory = True
        elif '.' not in cleaned_line:  # No file extension
            # Check if next line has greater indentation
            if i + 1 < len(lines):
                next_line = lines[i + 1].rstrip('\n').rstrip('\r')
                next_indent = len(next_line) - len(next_line.lstrip('│ ├└─'))
                is_directory = next_indent > indent_count

        # Add the current item to the path
        item_name = cleaned_line.rstrip('/')
        if is_directory:
            current_path.append(item_name)
            full_path = '/'.join(current_path) + '/'
            print(f"Adding directory: {full_path}")  # Debug
            structure.append(full_path)
        else:
            # It's a file
            full_path = '/'.join(current_path + [cleaned_line])
            print(f"Adding file: {full_path}")  # Debug
            structure.append(full_path)

    print("\nFinal structure:")  # Debug
    for path in structure:
        print(f"  {path}")  # Debug
    return structure

def create_structure(base_dir, structure_lines):
    """Create folders and files based on smart parsed structure lines."""
    if not structure_lines:
        return

    # First create all directories
    for path in structure_lines:
        if path.endswith('/'):
            full_path = os.path.normpath(os.path.join(base_dir, path))
            print(f"Creating directory: {full_path}")  # Debug
            os.makedirs(full_path, exist_ok=True)

    # Then create all files
    for path in structure_lines:
        if not path.endswith('/'):
            full_path = os.path.normpath(os.path.join(base_dir, path))
            print(f"Creating file: {full_path}")  # Debug
            folder = os.path.dirname(full_path)
            os.makedirs(folder, exist_ok=True)  # Ensure parent directory exists
            if not os.path.exists(full_path):
                open(full_path, 'a').close()

    root_folder = structure_lines[0].split('/')[0]
    root_path = os.path.join(base_dir, root_folder)
    print(f"\n✅ Project structure created successfully at: {root_path}")

def main():
    structures_dir = 'structures'
    structure_files = [f for f in os.listdir(structures_dir) if f.endswith('.txt')]

    if not structure_files:
        print(f"❌ No structure files found in '{structures_dir}' directory.")
        return

    selected_file = structure_files[0]
    file_path = os.path.join(structures_dir, selected_file)

    base_dir = input("\n📂 Enter the full path where you want to create the project structure: ").strip()

    if not os.path.isdir(base_dir):
        print(f"❌ The path '{base_dir}' does not exist. Please create it first or provide a valid path.")
        return

    structure_lines = read_structure_file(file_path)
    create_structure(base_dir, structure_lines)

if __name__ == "__main__":
    main()
