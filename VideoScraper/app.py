from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    platform = request.form['platform']
    output_path = f'static/{platform}_video.mp4'
    try:
        download_video(url, output_path)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
