import os

def generate_files(num_files, directory, file_prefix, content):
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(1, num_files + 1):
        filename = f"{file_prefix}_{i}.ipynb"
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'w') as file:
            file.write(content)
        
        print(f"Generated file: {filepath}")

if __name__ == "__main__":
    num_files = 12
    directory = "."
    file_prefix = "Exp"
    content = " "
    
    generate_files(num_files, directory, file_prefix, content)