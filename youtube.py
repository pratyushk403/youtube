import argparse
from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    
    # Get available video streams
    video_streams = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
    
    # Print available quality options with size
    print("Available Quality Options:")
    for i, stream in enumerate(video_streams):
        print(f"{i+1}. Resolution: {stream.resolution}, Type: {stream.mime_type}, Size: {stream.filesize_approx/(1024*1024):.2f} MB")
    
    # Prompt user to select quality option
    choice = int(input("Enter the number corresponding to the desired quality: "))
    selected_stream = video_streams[choice-1]
    
    # Download the video
    print("Downloading video...")
    selected_stream.download()
    print("Video downloaded successfully!")

# Create an argument parser
parser = argparse.ArgumentParser(description='YouTube Downloader')

# Add an argument for the URL
parser.add_argument('-url', '--video_url', type=str, help='YouTube video URL')

# Parse the command-line arguments
args = parser.parse_args()

# Check if the video URL argument is provided
if args.video_url:
    # Call the download_video function with the video_url argument
    download_video(args.video_url)
else:
    print('Please provide the YouTube video URL using the -url argument.')
