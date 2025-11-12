import subprocess, time, ot_lib, yaml, signal, os
from plyer import notification

launcher_timein_sec = 5
notification_timeout_sec = 5

def send_notification():
    subprocess.run([
    "notify-send",
    "Oraterm",
    f"Launching in {launcher_timein_sec} seconds...",
    f"--expire-time={notification_timeout_sec * 1000}"
])

def launch_window():
    time.sleep(launcher_timein_sec)
    terminal_cmd_arr = ot_lib.get_yaml_file("my_data.yaml")["terminal_cmd_arr"]
    process = subprocess.Popen(terminal_cmd_arr, stdout=subprocess.PIPE, text=True)
    pid = process.pid

    time.sleep(5)

    print(process.stdout)

    for line in process.stdout:
        print(f"Parent received: {line.strip()}")

    # time.sleep(5)

    # try:
    #     os.kill(pid, signal.SIGTERM)
    # finally:
    #     pass

if __name__ == "__main__":
    send_notification()
    launch_window()
