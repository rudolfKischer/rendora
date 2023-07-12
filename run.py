#!/usr/bin/env python3

import os

# Get the interpreter from the virtual enviroment
script_dir = os.path.dirname(os.path.abspath(__file__))
venv_activate = os.path.join(script_dir, "env", "bin", "activate")
activate_cmd = f"source {venv_activate}"
if os.name == "nt":  # For Windows
    activate_cmd = f"call {venv_activate}"
os.system(activate_cmd)

from src import main

def run():
    main.main()

if __name__ == "__main__":
    run()