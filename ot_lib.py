import yaml
from pathlib import Path

def write_to_file(filename, string):
    with open(filename, "a") as f:
        f.write(f"\n{string}")

def get_yaml_file(filename):
    path = Path(f"~/Files/_Coding/oraterm/{filename}").expanduser()

    with open(path, "r") as f:
        return yaml.safe_load(f)

def write_to_yaml_file(filename, contents):
    path = Path(f"~/Files/_Coding/oraterm/{filename}").expanduser()

    with open(path, "w") as f:
        yaml.dump(contents, f)

def get_launch_times(filename):
    my_data = get_yaml_file(filename)
    launch_times = my_data["launch_times"]
    arr = []

    for label in launch_times:
        arr.append(launch_times[label])

    return arr

def get_launch_labels(filename):
    my_data = get_yaml_file(filename)
    launch_times = my_data["launch_times"]
    arr = []

    for label in launch_times:
        arr.append(label)

    return arr
