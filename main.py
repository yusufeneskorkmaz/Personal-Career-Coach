import uvicorn
from src.PersonalCareerCoach.api.routes import app
import subprocess
import threading

def run_streamlit():
    subprocess.run(["streamlit", "run", "src/PersonalCareerCoach/dashboard/app.py"])

if __name__ == "__main__":
    # Start Streamlit in a separate thread
    streamlit_thread = threading.Thread(target=run_streamlit)
    streamlit_thread.start()

    # Run FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)