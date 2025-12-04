import os

# Node directories
nodes = ["node1", "node2", "node3"]

# Ensure storage.txt exists in each node
for node in nodes:
    os.makedirs(node, exist_ok=True)
    storage_file = os.path.join(node, "storage.txt")
    if not os.path.exists(storage_file):
        with open(storage_file, "w") as f:
            pass  # create empty file if it doesn't exist

# Function to upload a file
def upload_file():
    title = input("Enter Title name to upload: ")
    content = input("Enter file content: ")
    node_choice = input("Enter node to store file (1, 2, 3): ")

    try:
        node_index = int(node_choice) - 1
        if node_index not in [0, 1, 2]:
            print("Invalid node number!")
            return
    except ValueError:
        print("Invalid input!")
        return

    file_path = os.path.join(nodes[node_index], "storage.txt")
    with open(file_path, "a") as f:
        f.write(f"{title}: {content}\n")
    print(f"File stored in {nodes[node_index]} successfully!")

# Function to view files in nodes
def view_files():
    for node in nodes:
        print(f"\nFiles in {node}:")
        file_path = os.path.join(node, "storage.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data = f.read()
                if data:
                    print(data.strip())
                else:
                    print("No files yet.")
        else:
            print("Storage file missing!")

# Main menu
def main():
    while True:
        print("\n1. Upload File")
        print("2. View Files in Nodes")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            upload_file()
        elif choice == "2":
            view_files()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()