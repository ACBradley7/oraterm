import random, time, os, schedule, tkinter, yaml, ot_lib, subprocess, textwrap, sys

main_options_dict = {}
prayers_options_dict = {}
timings_options_dict = {}
friard_options_dict = {}

def get_terminal_width():
    size = os.get_terminal_size()
    return size.columns

def print_divider():
    print("-" * get_terminal_width())
    print()

def load_options_dicts():
    load_main_options_dict()
    load_prayers_options_dict()
    load_timings_options_dict()
    load_friard_options_dict()

def load_main_options_dict():
    main_options_dict["info"] = None
    main_options_dict["long_prompt"] = "(M)ark as read, (P)rayers, (T)imings, (F)riard, (Q)uit."
    main_options_dict["short_prompt"] = "M, P, T, F, Q: "
    main_options_dict["options"] = {
        "M": mark_read,
        "P": prayers_menu,
        "T": timings_menu,
        "F": friard_menu,
        "Q": quit_program,
        "": quit_program
    }

def load_prayers_options_dict():
    prayers_options_dict["info"] = None
    prayers_options_dict["long_prompt"] = "(A)dd prayer, (R)emove prayer, (B)ack, (Q)uit."
    prayers_options_dict["short_prompt"] = "A, R, B, Q: "
    prayers_options_dict["options"] = {
        "A": add_prayer,
        "R": remove_prayer,
        "Q": quit_program,
        "B": previous_menu,
        "": previous_menu
    }

def load_timings_options_dict():
    timings_options_dict["info"] = None
    timings_options_dict["long_prompt"] = "(N)ew timing, (A)djust timings, (M)odify labels, (B)ack, (Q)uit"
    timings_options_dict["short_prompt"] = "N, A, M, B, Q: "
    timings_options_dict["options"] = {
        "N": new_timing,
        "A": adjust_timings,
        "M": modify_labels,
        "Q": quit_program,
        "B": previous_menu,
        "": previous_menu
    }

def load_friard_options_dict():
    friard_options_dict["info"] = "Friard is the script in the background responsible for managing the launching of notifications/prayers."
    friard_options_dict["long_prompt"] = "(R)estart friard, (D)isable friard, (B)ack, (Q)uit."
    friard_options_dict["short_prompt"] = "R, D, B, Q: "
    friard_options_dict["options"] = {
        "R": restart_fraird,
        "D": disable_fraird,
        "Q": quit_program,
        "B": previous_menu,
        "": previous_menu
    }

def prayers_menu():
    get_input(prayers_options_dict)

def timings_menu():
    get_input(timings_options_dict)

def friard_menu():
    get_input(friard_options_dict)

def mark_read():
    print("\nPrayer has been marked as read.")

def add_prayer():
    return

def remove_prayer():
    return

def new_timing():
    return

def adjust_timings():
    return

def modify_labels():
    return

def restart_fraird():
    return

def disable_fraird():
    return

def previous_menu():
    return

def quit_program():
    sys.exit()

def get_input(choice_options):
    if choice_options["info"]:
        print(f"\n{choice_options["info"]}")

    while True:
        print_divider()

        print(f"\n{choice_options["long_prompt"]}")

        choice = input(choice_options["short_prompt"])
        choice = choice.upper()

        if choice not in choice_options["options"]:
            print("\nInvalid Choice...")
        else:
            # ANY CALLBACK ARGUMENTS ARE CALLED IN CALLBACK
            choice_options["options"][choice]()

            if choice == "B" or choice == "":
                break

def which_prayer(data_file, prayers_file):
    my_data = ot_lib.get_yaml_file(data_file)
    prayers_list = ot_lib.get_yaml_file(prayers_file)
    pick_list = []
    recent_list = my_data["recent_prayers"]

    for prayer_id in prayers_list:
        if prayer_id not in recent_list:
            pick_list.append(f"{prayer_id}")
            break

    if len(pick_list) == 0:
        pick_list = list(recent_list)
        recent_list = []

    rand_prayer_id = random.choice(pick_list)

    recent_list.append(rand_prayer_id)
    my_data["recent_prayers"] = recent_list
    ot_lib.write_to_yaml_file(data_file, my_data)

    prayer_dict = prayers_list[rand_prayer_id]
    return prayer_dict

def print_prayer(prayer_dict):
    prayer_text = prayer_dict["text"]
    print("\n\n")
    print(textwrap.fill(prayer_text, get_terminal_width()))
    print("\n\n")

def main():
    load_options_dicts()

    prayers_list_file = "prayers_list.yaml"
    my_data_file = "my_data.yaml"

    prayer_dict = which_prayer(my_data_file, prayers_list_file)
    print_prayer(prayer_dict)

    # MAIN LOOP
    get_input(main_options_dict)

if __name__ == "__main__":
    main()
