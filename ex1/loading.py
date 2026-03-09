import importlib
# import sys


def check_dependencies() -> bool:
    """
    Verifies existence of mandatory packages and explains management tools.
    """
    packages: list[str] = ['pandas', 'requests', 'matplotlib', 'numpy']
    all_found: bool = True

    print("\nLOADING STATUS: Loading programs...")
    print("\n--- Package Manager Info ---")
    print("pip: Uses requirements.txt for flat list dependencies.")
    print("Poetry: Uses pyproject.toml for deterministic builds and locking\n")

    for lib in packages:
        try:
            module = importlib.import_module(lib)
            version: str = getattr(module, '__version__', 'unknown')
            print(f"[OK] {lib} ({version}) ready")
        except ImportError:
            print(f"[MISSING] {lib}")
            all_found = False

    return all_found


def run_analysis() -> None:
    """Simulates data analysis using the loaded guns (packages)."""
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...\n")
    data = pd.DataFrame({'signal': np.random.randn(1000).cumsum()})
    plt.plot(data['signal'], color='green')
    plt.title("Matrix Signal Analysis")
    plt.savefig("matrix_analysis.png")
    print("Analysis complete! Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    if check_dependencies():
        run_analysis()
    else:
        print("\nERROR: Missing programs! "
              "Run 'pip install -r requirements.txt'")
