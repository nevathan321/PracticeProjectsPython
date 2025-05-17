# Import necessary libraries
import os            # To work with file and directory paths
import shutil        # To copy files and directories
import datetime     # To get the current date
import schedule     # To schedule tasks at specific times
import time         # To pause the execution of the program (sleep)

# Define source and destination directories
source_dir = "C:\Users\Niruban\Pictures\Screenshots"   # Directory with the screenshots to back up
destination_dir = "C:\Users\Niruban\Pictures\Saved Pictures"  # Destination directory to store backups

# Function to copy the folder to the destination
def copy_folder_to_directory(source, dest):
    today = datetime.date.today()  # Get today's date (for creating a new backup folder)
    dest_dir = os.path.join(dest, str(today))  # Create a folder in the destination directory named by today's date

    try:
        # Attempt to copy the source directory to the destination directory
        shutil.copytree(source, dest_dir)  # This will copy the entire folder (including subfolders)
        print(f"Folder copied to: {dest_dir}")  # Print confirmation if the folder is copied successfully
    except FileExistsError:
        # Handle the case where the folder already exists
        print(f"Folder already exists in: {dest_dir}")  # Print a message if the folder is already there

# Schedule the task to run every day at 18:55 (6:55 PM)
schedule.every().day.at("18:55").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Call the function immediately to back up the folder once
copy_folder_to_directory(source_dir, destination_dir)

# This infinite loop keeps the script running to check for scheduled tasks
while True:
    # Run any scheduled tasks that are due to be executed
    schedule.run_pending()
    # Sleep for 60 seconds before checking again (so it doesn't consume too much CPU)
    time.sleep(60)
