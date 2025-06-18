import os
import subprocess
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Start Streamlit server if not running
        subprocess.Popen(['streamlit', 'run', '💡_LIAT_MEUNIQUE_SYSTEM.py', '--server.port', '8501'])
        
        # Redirect to Streamlit
        self.send_response(302)
        self.send_header('Location', 'http://localhost:8501')
        self.end_headers() 