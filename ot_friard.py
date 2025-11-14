import time, ot_lib, os, re,, ot_notification_launcher

data_filename = "my_data.yaml"
log_file = "friard_log.txt"
error_log_file = "friard_error_log.txt"

def ctime_to_sec(t):
    match = re.search(r'..:..:..', t)
    t_hh_mm_ss = match.group(0)

    t_float = time_to_sec(t_hh_mm_ss)
    return t_float

def time_to_sec(t):
    hour = t[0:2]
    min = t[3:5]

    t_float = int(hour) + (int(min) / 60)
    return t_float * 60 * 60

def launch_times_to_sec(arr):
    launch_times_arr_sec = []

    for launch_t in arr:
        launch_times_arr_sec.append(time_to_sec(launch_t))

    return launch_times_arr_sec

def time_diff_to_next_launch(ct, launch_times):
    next_launch_time = None

    for launch_t in reversed(launch_times):
        if ct <= launch_t:
            next_launch_time = launch_t

    if not next_launch_time:
        next_launch_time = launch_times[0]

    if ct == next_launch_time:
        time_diff_to_next_launch = 0
    elif ct < next_launch_time:
        time_diff_to_next_launch = next_launch_time - ct
    else:
        time_diff_to_next_launch = 24 * 60 * 60 - ct + next_launch_time

    return time_diff_to_next_launch

def get_time_to_sleep(time_to_launch):
    offset = 2 * 60

    sleep_amount = time_to_launch - offset

    if sleep_amount <= 0:
        sleep_amount = 0

    return sleep_amount

def handle_sleeping(awake, time_diff_to_next_launch, sleep_amount):
    if awake and time_diff_to_next_launch == 0:
        return
    elif awake:
        time.sleep(60)
    else:
        time.sleep(sleep_amount)

def launch_notification(time_diff_to_next_launch):
    if time_diff_to_next_launch == 0:
        ot_lib.write_to_file(log_file, "Main Launched...")
        ot_notification_launcher.main()

        # DO NOT REMOVE. PREVENTS INFINITE LOOPS.
        time.sleep(60)

        return False
    else:
        return True

def run_program():
    awake = False
    pid = os.getpid()
    ot_lib.write_to_file(log_file, f"Friard Initialized. PID: {pid}.")

    while True:
        try:
            data = ot_lib.get_yaml_file(data_filename)
        except Exception as e:
            with open(error_log_file, "a") as err_f:
                err_f.write(f"{time.ctime()} - Exception reading YAML: {e}\n")

        curr_time_str = time.ctime()
        curr_time_sec = ctime_to_sec(curr_time_str)
        launch_times = ot_lib.get_launch_times(data_filename)
        launch_times = launch_times_to_sec(launch_times)
        next_launch_time_diff = time_diff_to_next_launch(curr_time_sec, launch_times)
        sleep_amount = get_time_to_sleep(next_launch_time_diff)

        ot_lib.write_to_file(log_file, f"Curr Time: {curr_time_str}. Time to launch: {next_launch_time_diff}.")

        handle_sleeping(awake, next_launch_time_diff, sleep_amount)
        awake = launch_notification(next_launch_time_diff)

if __name__ == "__main__":
    run_program()
