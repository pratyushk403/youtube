# Youtube Video Downloader 
Download Youtube with Just One Command

# Features

- Fetches available video quality options from a given YouTube URL.
- Allows the user to select the desired video quality for downloading.
- Downloads the video file in the selected quality option.
- Supports downloading videos in the MP4 format.


# Installation
## Clone this repository:
git clone https://github.com/pratyushk403/youtube
## Navigate to Directory 
cd <current_directory>/youtube
## Make it Executable
chmod +x youtube.py
## Now go to user home directory and make changes in bashrc file
nano .bashrc
## set this alias at last 
alias youtube='python3 <current_directory>/youtube.py'
![image](https://github.com/pratyushk403/youtube/assets/46959127/0818511a-7961-4851-9b08-a71c760425b9)


## To apply the changes, either restart your terminal or run the following command to reload the .bashrc file:
source ~/.bashrc
## Now you can use the youtube alias in your terminal to execute the Python script by simply typing youtube. 
youtube -url <url>
