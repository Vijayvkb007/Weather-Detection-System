import shutil
import os

# recursive list of files in a directory
def recursive_list(path: str, fp: list) -> None:
    for folder in os.listdir(path):
        folder = os.path.join(path, str(folder))
        if os.path.isdir(folder):
            recursive_list(folder, fp)
        else:
            if folder.endswith(".jpg") and folder.split("/")[2] == "Dataset2":
                fp.append(folder)

# check if a string is a prefix of another string
def is_prefix(prefix, path) -> bool:
    return path.startswith(prefix)

# create folders directly to datasets
nloc = ["./datasets/cloudy/", "./datasets/rain/", "./datasets/shine/", "./datasets/sunrise/"]

for dirs in nloc:
    os.makedirs(dirs, exist_ok=True)
    
# move files with prefix to new location
fp = list()
recursive_list("./datasets", fp)
for file in fp:
    if is_prefix("cloudy", file.split("/")[-1]):
        shutil.move(file,(nloc[0] + file.split("/")[-1]))
    elif is_prefix("rain", file.split("/")[-1]):
        shutil.move(file,(nloc[1] + file.split("/")[-1]))
    elif is_prefix("shine", file.split("/")[-1]):
        shutil.move(file,(nloc[2] + file.split("/")[-1]))
    elif is_prefix("sunrise", file.split("/")[-1]):
        shutil.move(file,(nloc[3] + file.split("/")[-1]))

# move files from Dataset1 to datasets
for files in os.listdir("./datasets/Dataset1"):
    files = os.path.join("./datasets/Dataset1", str(files))
    shutil.move(files, "./datasets/")

os.system("ls ./datasets/Dataset1 >> ./was_empty.txt && ls ./datasets/Dataset2 >> ./was_empty.txt")
# remove empty folders
os.rmdir("./datasets/Dataset1")
os.rmdir("./datasets/Dataset2")
