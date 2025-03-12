## For Logging purpose
import logging 
import os 
from datetime import datetime 


LOG_FILE_name= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# print(f"ROOT_DIR: {ROOT_DIR}")


logs_path = os.path.join(ROOT_DIR,"logs_folder") #os.path.join(...) → Joins all the parts into a complete file path, ensuring correct formatting across different operating systems.
os.makedirs(logs_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE_name)

# We use logging.basicConfig() to: ✅ Save logs to a file instead of just printing to the console.
# ✅ Define a clear log format for better debugging.
# ✅ Set the log level (INFO, WARNING, ERROR, etc.).

logging.basicConfig( #We use logging.basicConfig() to configure the logging system so that logs are written to a file with a specific format and log level.
    filename= LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, #Set the log level (INFO, WARNING, ERROR, etc.). Only logs with a level equal to or higher than this level will be saved.logging. INFO logs INFO, WARNING, ERROR, and CRITICAL messages.
)


# if __name__ == "__main__":
#    logging.info("✅ Logging system initialized successfully!")

