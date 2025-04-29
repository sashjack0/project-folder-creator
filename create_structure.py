import os
import re

def clean_line_symbols(line):
    """Remove tree drawing symbols like ├──, └──, │, ── etc."""
    return re.sub(r'[├└│─]+', '', line)

def read_structure_file(file_path):
    """Smart parser that uses non-alphanumeric leading characters to detect levels and builds full paths with root tracking."""
    structure = []
    folder_stack = []
    root_folder = None  # NEW: Track the root folder

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Normalize line endings and clean symbols
            line = line.rstrip('\n').rstrip('\r')
            if not line.strip():
                continue

            cleaned_line = clean_line_symbols(line).strip()

            # Remove inline comments like '# (something)'
            if '#' in cleaned_line:
                cleaned_line = cleaned_line.split('#')[0].strip()

            if not cleaned_line:
                continue

            # Count number of leading non-alphanumeric characters
            leading_nonalpha = len(re.match(r'[^a-zA-Z0-9]*', line).group())
            indent_level = leading_nonalpha // 4

            # Adjust stack based on indent level
            folder_stack = folder_stack[:indent_level]

            if cleaned_line.endswith('/'):
                # It's a folder
                folder_stack.append(cleaned_line.rstrip('/'))

                # Track the first folder as root
                if root_folder is None:
                    root_folder = folder_stack[0]

                full_path = '/'.join(folder_stack) + '/'
                structure.append(full_path)
            else:
                # It's a file
                full_path = '/'.join(folder_stack + [cleaned_line])
                structure.append(full_path)

    # After building structure, ensure all paths are nested under root_folder
    if root_folder:
        final_structure = []
        for path in structure:
            if not path.startswith(root_folder):
                final_structure.append(f"{root_folder}/{path}".replace('//', '/'))
            else:
                final_structure.append(path)
        return final_structure
    else:
        return structure

def create_structure(base_dir, structure_lines):
    """Create folders and files based on smart parsed structure lines."""
    for path in structure_lines:
        full_path = os.path.normpath(os.path.join(base_dir, path))

        if path.endswith('/'):
            os.makedirs(full_path, exist_ok=True)
        else:
            folder = os.path.dirname(full_path)
            os.makedirs(folder, exist_ok=True)
            if not os.path.exists(full_path):
                open(full_path, 'a').close()

    print(f"\n✅ Project structure created successfully at: {base_dir}")


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
