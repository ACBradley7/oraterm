import ot_lib

def main():
    times = ot_lib.get_launch_times("my_data.yaml")
    labels = ot_lib.get_launch_labels("my_data.yaml")
    print(times)
    print(labels)

main()
