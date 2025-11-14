import random, time, os, schedule, tkinter, yaml, ot_lib, subprocess, textwrap, sys, datetime


prayers_list_filename = "prayers_list.yaml"
my_data_filename = "my_data.yaml"
main_options_dict = {}
prayers_options_dict = {}
add_prayer_name_dict = {}
add_prayer_label_dict = {}
add_prayer_text_dict = {}
timings_options_dict = {}
friard_options_dict = {}
strings_dict = {}

def get_terminal_width():
    size = os.get_terminal_size()
    return size.columns

def print_divider():
    print("-" * get_terminal_width())
    print()

def load_global_dicts():
    load_strings_dict()
    load_main_menu_dicts()
    load_prayers_subdicts()

def load_strings_dict():

    # Prayer Read
    strings_dict["prayer_read"] = "Marking as read..."
    strings_dict["prayer_inc_streak"] = "Prayer has been read. Streak increased."
    strings_dict["prayer_no_inc_streak"] = "Prayer has already been read. Cannot increase streak."
 
    # Prayers menu
    strings_dict["prayers_menu"] = "Entering prayers menu..."
    strings_dict["add_prayer"] = "Adding prayer..."
    strings_dict["edit_prayer"] = "Editing prayer..."
    strings_dict["remove_prayer"] = "Removing prayer..."
    strings_dict["list_prayers_contents"] = "Listing prayers' contents..."

    # Add prayer
    strings_dict["new_prayer_name"] = "New prayer name"
    strings_dict["prayer_name_added"] = "Prayer name added."
    strings_dict["new_prayer_label"] = "New prayer label"
    strings_dict["prayer_label_added"] = "Prayer label added."
    strings_dict["new_prayer_text"] = "New prayer text"
    strings_dict["prayer_text_added"] = "Prayer text added."

    # Timings menu
    strings_dict["timings_menu"] = "Entering timings menu..."
    strings_dict["new_timing"] = "Adding new timing..."
    strings_dict["adjust_timings"] = "Adjusting timings..."
    strings_dict["modify_labels"] = "Modifying labels..."

    # Friard menu
    strings_dict["friard_menu"] = "Entering friard menu..."
    strings_dict["friard_restart"] = "Restarting the friar..."
    strings_dict["friard_disable"] = "Disabling the friar..."

    # General
    strings_dict["back"] = "Going back..."
    strings_dict["quit"] = "Quitting..."
    strings_dict["invalid"] = "Invalid choice..."

def load_main_menu_dicts():
    load_main_options_dict()
    load_prayers_options_dict()
    load_timings_options_dict()
    load_friard_options_dict()

def load_prayers_subdicts():
    load_add_prayer_name_dict()
    load_add_prayer_label_dict()
    load_add_prayer_text_dict()

def load_main_options_dict():
    main_options_dict["info"] = None
    main_options_dict["long_prompt"] = "(M)ark as read, (P)rayers, (T)imings, (F)riard, (Q)uit."
    main_options_dict["short_prompt"] = "M, P, T, F, Q: "
    main_options_dict["options"] = {
        "M": {
            "callback": mark_read,
            "response": strings_dict["prayer_read"]
        },
        "P": {
            "callback": prayers_menu,
            "response": strings_dict["prayers_menu"]
        },
        "T": {
            "callback": timings_menu,
            "response": strings_dict["timings_menu"]
        },
        "F": {
            "callback": friard_menu,
            "response": strings_dict["friard_menu"]
        },
        "Q": {
            "callback": quit_program,
            "response": strings_dict["quit"]
        },
        "": {
            "callback": quit_program,
            "response": strings_dict["quit"]
        }
    }

def load_prayers_options_dict():
    prayers_options_dict["info"] = None
    prayers_options_dict["long_prompt"] = "(A)dd prayer, (E)dit prayer, (R)emove prayer, (L)ist prayers' contents, (B)ack, (Q)uit."
    prayers_options_dict["short_prompt"] = "A, E, R, L, B, Q: "
    prayers_options_dict["options"] = {
        "A": {
            "callback": add_prayer,
            "response": strings_dict["add_prayer"]
        },
        "E": {
            "callback": edit_prayer,
            "response": strings_dict["edit_prayer"]
        },
        "R": {
            "callback": remove_prayer,
            "response": strings_dict["remove_prayer"]
        },
        "L": {
            "callback": list_prayers_contents,
            "response": strings_dict["list_prayers_contents"]
        },
        "Q": {
            "callback": quit_program,
            "response": strings_dict["quit"]
        },
        "B": {
            "callback": previous_menu,
            "response": strings_dict["back"]
        },
        "": {
            "callback": previous_menu,
            "response": strings_dict["back"]
        }
    }

def load_timings_options_dict():
    timings_options_dict["info"] = None
    timings_options_dict["long_prompt"] = "(N)ew timing, (A)djust timings, (M)odify labels, (B)ack, (Q)uit"
    timings_options_dict["short_prompt"] = "N, A, M, B, Q: "
    timings_options_dict["options"] = {
        "N": {
            "callback": new_timing,
            "response": strings_dict["new_timing"]
        },
        "A": {
            "callback": adjust_timings,
            "response": strings_dict["adjust_timings"]
        },
        "M": {
            "callback": modify_labels,
            "response": strings_dict["modify_labels"]
        },
        "Q": {
            "callback": quit_program,
            "response": strings_dict["quit"]
        },
        "B": {
            "callback": previous_menu,
            "response": strings_dict["back"]
        },
        "": {
            "callback": previous_menu,
            "response": strings_dict["back"]
        }
    }

def load_friard_options_dict():
    friard_options_dict["info"] = "Friard is the script in the background responsible for managing the launching of notifications/prayers."
    friard_options_dict["long_prompt"] = "(R)estart friard, (D)isable friard, (B)ack, (Q)uit."
    friard_options_dict["short_prompt"] = "R, D, B, Q: "
    friard_options_dict["options"] = {
        "R": {
            "callback": restart_fraird,
            "response": strings_dict["friard_restart"]
        },
        "D": {
            "callback": disable_fraird,
            "response": strings_dict["friard_disable"]
        },
        "Q": {
            "callback": quit_program,
            "response": strings_dict["quit"]
        },
        "B": {
            "callback": previous_menu,
            "response": strings_dict["back"]
        },
        "": {
            "callback": previous_menu,
            "response": strings_dict["back"]
        }
    }

def load_add_prayer_name_dict():
    add_prayer_name_dict["info"] = None
    add_prayer_name_dict["prompt"] = strings_dict["new_prayer_name"]
    add_prayer_name_dict["response"] = strings_dict["prayer_name_added"]

def load_add_prayer_text_dict():
    add_prayer_text_dict["info"] = None
    add_prayer_text_dict["prompt"] = strings_dict["new_prayer_text"]
    add_prayer_text_dict["response"] = strings_dict["prayer_text_added"]

def load_add_prayer_label_dict():
    prayer_labels = ot_lib.get_prayer_labels(my_data_filename)

    add_prayer_label_dict["info"] = None
    add_prayer_label_dict["long_prompt"] = strings["new_prayer_label"]

    return

def prayers_menu(args):
    get_input_from_choices(prayers_options_dict, *args)

def timings_menu(args):
    get_input_from_choices(timings_options_dict)

def friard_menu(args):
    get_input_from_choices(friard_options_dict)

def mark_read(args):
    my_data_filename = args[0]
    data = ot_lib.get_yaml_file(my_data_filename)
    date_today = str(datetime.date.today().month) + "-" + str(datetime.date.today().day) + "-" + str(datetime.date.today().year)

    if data["streak_date"] != date_today:
        data["streak"] += 1
        data["streak_date"] = date_today
        print(f"\n{strings_dict["prayer_inc_streak"]}")
        ot_lib.write_to_yaml_file(my_data_filename, data)
    else:
        print(f"\n{strings_dict["prayer_no_inc_streak"]}")

def add_prayer(args):
    prayers_list_filename = args[1]
    prayers_list_dict = ot_lib.get_yaml_file(prayers_list_filename)
    new_prayer_text = input(f"\n{strings_dict["new_prayer_text"]}: ")
    new_prayer_name = input(f"{strings_dict["new_prayer_name"]}: ")
    new_prayer_label = input(f"{strings_dict["new_prayer_label"]}: ")

    new_prayer_dict = {
        "name": new_prayer_name,
        "label": new_prayer_label,
        "text": new_prayer_text
    }

    for prayer_id in prayers_list_dict:
        new_id = int(prayer_id[-1])
    new_id += 1
    new_id_str = f"id_{new_id}"

    prayers_list_dict[new_id_str] = new_prayer_dict
    ot_lib.write_to_yaml_file(prayers_list_filename, prayers_list_dict)

def edit_prayer(args):
    prayers_filename = args[1]
    list_prayers_handler(prayers_filename, False)

def list_prayers_contents(args):
    prayers_filename = args[1]
    list_prayers_handler(prayers_filename, True)

def remove_prayer(args):
    return

def new_timing(args):
    return

def adjust_timings(args):
    return

def modify_labels(args):
    return

def restart_fraird(args):
    return

def disable_fraird(args):
    return

def previous_menu(args):
    return

def quit_program(args):
    sys.exit()

def list_prayers_handler(prayers_list_filename, show_contents):
    prayers_list_dict = ot_lib.get_yaml_file(prayers_list_filename)

    print_divider()
    print("\nList of current prayers\n")
    for prayer_id in prayers_list_dict:
        print(f"\nID: {prayer_id[-1]}")
        print(f"Name: {prayers_list_dict[prayer_id]["name"]}")
        print(f"Label: {prayers_list_dict[prayer_id]["label"]}")

        if show_contents:
            prayer_text = prayers_list_dict[prayer_id]["text"]
            print()
            print(textwrap.fill(prayer_text, get_terminal_width()))

def list_prayers_labels_handler():
    labels = ot_lib.get_launch_labels(my_data_filename)
    cnt = 0

    print()
    for label in labels:
        cnt += 1
        print(f"{cnt}: {label}")

def get_input_from_choices(choice_options, *callback_args):
    if choice_options["info"]:
        print(f"\n{choice_options["info"]}")

    while True:
        print_divider()

        print(f"\n{choice_options["long_prompt"]}")

        choice = input(choice_options["short_prompt"])
        choice = choice.upper()

        if choice not in choice_options["options"]:
            print(strings_dict["invalid"])
        else:
            print(f"\n{choice_options["options"][choice]["response"]}")
            choice_options["options"][choice]["callback"](callback_args)

            if choice == "Q" or choice == "B" or choice == "":
                break

def get_string_input(choice_options):
    if choice_options["info"]:
        print(f"\n{choice_options["info"]}")

    while True:
        choice = input(choice_options["prompt"])
        print(f"\n{choice_options["options"]["response"]}")

        if choice == "q" or choice == "Q" or choice == "b" or choice == "B" or choice == "":
            print(strings_dict["back"])
            return None
        else:
            return choice

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
    load_global_dicts()

    prayer_dict = which_prayer(my_data_filename, prayers_list_filename)
    print_prayer(prayer_dict)

    # MAIN LOOP
    get_input_from_choices(main_options_dict, my_data_filename, prayers_list_filename)

if __name__ == "__main__":
    main()
