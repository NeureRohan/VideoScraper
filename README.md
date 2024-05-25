# VideoScraper

1) Make sure you have Flask and yt-dlp installed. You can install them using pip:

bash : pip install Flask yt-dlp


2) Run the Flask Application:
Navigate to the directory containing app.py and run the following command to start the Flask development server:

bash : python app.py


Explanation

Flask Setup: The Flask application has a route for the homepage (/) that renders an HTML form. Another route (/download) handles the form submission.
HTML Form: The form takes a video URL and a platform (Facebook, TikTok, or Instagram) and submits it to the /download route.
Video Download: The download_video function uses yt-dlp to download the video from the provided URL and save it to the static directory.
File Delivery: After downloading, the video file is sent to the user as an attachment.
