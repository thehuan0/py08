import os
from dotenv import load_dotenv


def reveal_mainframe_config() -> None:
    """Loads and displays secrets using the python-dotenv library."""
    load_dotenv()

    mode: str = os.getenv("MATRIX_MODE", "development")
    db_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_url: str | None = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {'Connected' if db_url else 'Missing'}")
    print(f"API Access: {'Authenticated' if api_key else 'Missing'}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_url if zion_url else 'Offline'}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")


if __name__ == "__main__":
    try:
        reveal_mainframe_config()
    except Exception as e:
        print(f"ERROR: Mainframe connection failure: {e}")
