import os

# Node folders
nodes = ["node1", "node2", "node3"]

def upload_file():
    file_name = input("Enter file name to upload: ")
    content = input("Enter file content: ")
    node = input("Enter node to store file (1, 2, 3): ")
    node_folder = nodes[int(node)-1]
    file_path = os.path.join(node_folder, "storage.txt")
    with open(file_path, "a") as f:
        f.write(f"{file_name}: {content}\n")
    print(f"File '{file_name}' uploaded to {node_folder} successfully!\n")

def view_files():
    for idx, node_folder in enumerate(nodes):
        print(f"Files in {node_folder}:")
        file_path = os.path.join(node_folder, "storage.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data = f.read()
                if data:
                    print(data)
                else:
                    print("No files yet.")
        print("-"*20)

def main():
    while True:
        print("1. Upload File")
        print("2. View Files in Nodes")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            upload_file()
        elif choice == "2":
            view_files()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()