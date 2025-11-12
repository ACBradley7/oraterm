import os, sys
from pathlib import Path

def make_systemd_unit_file():
    unit_file_path = Path("~/.config/systemd/user/oraterm.service").expanduser()
    scripts_path = Path("~/Files/_Coding/oraterm/ot_friard.py").expanduser()
    working_dir = scripts_path.parent
    python_interp_path = sys.executable

    with open(unit_file_path, "w") as file:
        file.write("[Unit]\n")
        file.write("Description=Oraterm Service\n\n")
        file.write("[Service]\n")
        file.write("Environment=PYTHONUNBUFFERED=1\n")
        file.write(f"WorkingDirectory={working_dir}\n")
        file.write(f"ExecStart={python_interp_path} {scripts_path}\n")
        file.write("Restart=on-failure\n\n")
        file.write("[Install]\n")
        file.write("WantedBy=default.target\n\n")

def launch_service():
    os.system("systemctl --user enable --now oraterm.service")

def linux_install():
    make_systemd_unit_file()
    launch_service()

def main():
    linux_install()

main()
