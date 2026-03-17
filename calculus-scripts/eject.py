import os

for root, dirs, files in os.walk("."):
    for dir_name in dirs:
        if dir_name == "__pycache__":
            cache_path = os.path.join(root, dir_name)
            print(f"Removing: {cache_path}")
            os.rmdir(cache_path)
