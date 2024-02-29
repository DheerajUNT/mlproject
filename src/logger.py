import logging
import os
from datetime import datetime

# declaring the way in which we want our log file named, this is the naming convention
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#the log file needs to have a path, so this is how we do it
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) 
# the log file will be like "logs+LOG_FILE" in the current working directory which is in this case
# src folder
os.makedirs(logs_path, exist_ok=True) 
#this tells the os that even if there is an existing directory
# keep appending to it

LOGS_FILE_PATH = os.path.join(logs_path, LOG_FILE) 
#this is the path to the logs files.

# if we want to use our logging then we need to override the basic functionality
# we can do that by setting the basicConfig

logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
