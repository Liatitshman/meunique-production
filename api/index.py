import streamlit.web.bootstrap as bootstrap
import os
import sys

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Streamlit configuration
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_SERVER_PORT"] = "8501"
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"

# Run the final MeUnique system
if __name__ == "__main__":
    # Use the final production system
    flag_options = {
        "server.headless": True,
        "server.port": 8501,
        "server.address": "0.0.0.0",
        "server.enableCORS": True,
        "server.enableXsrfProtection": False,
    }
    
    bootstrap.run(
        "💡_MEUNIQUE_ENGLISH_SYSTEM.py",
        "streamlit run",
        flag_options,
        []
    ) 