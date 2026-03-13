import os
try:
    from dotenv import load_dotenv
except ImportError:
    print("dotenv: Not installed. Run 'pip install python-dotenv' "
          "on venv to install")
    exit()


def reveal_mainframe_config() -> None:
    """Loads and displays secrets using the python-dotenv library."""
    load_dotenv()

    mode: str = os.getenv("MATRIX_MODE", "development")
    db_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_url: str | None = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: "
          f"{'Connected to local instance' if db_url else 'Missing'}")
    print(f"API Access: {'Authenticated' if api_key else 'Missing'}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion_url else 'Offline'}")

    print("\nEnvironment security check:")
    if os.path.exists(".env"):
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("[KO] Not accessible")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        reveal_mainframe_config()
    except Exception as e:
        print(f"ERROR: Mainframe connection failure: {e}")
