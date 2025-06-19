import subprocess
import sys
import os

# Simple wrapper to run the Streamlit app
if __name__ == "__main__":
    # Import and run the English version
    subprocess.run([
        sys.executable, 
        "-m", 
        "streamlit", 
        "run", 
        "💡_MEUNIQUE_ENGLISH_SYSTEM.py",
        "--server.port", os.environ.get("PORT", "8501"),
        "--server.address", "0.0.0.0"
    ]) 