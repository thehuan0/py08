import sys
import os
import site


def check_the_construct() -> None:
    """
    Analyzes the environment to determine if the user is inside a venv.
    Uses sys.prefix comparison to detect environment isolation.
    """
    try:
        is_venv: bool = sys.prefix != sys.base_prefix

        if is_venv:
            print("\nMATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}")
            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting global system\n")
            print("Package installation path:")
            for path in site.getsitepackages():
                print(f" {path}")
        else:
            print("\nMATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")
            print("\nWARNING: You're in the global environment!")
            print("To enter the construct, run:")
            print("python3 -m venv matrix_env")
            print("source matrix_env/bin/activate # Unix")
            print("matrix_env\\Scripts\\activate # Windows")

    except Exception as e:
        print(f"Error accessing the mainframe: {e}")


if __name__ == "__main__":
    check_the_construct()
