from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin
import youtube_dl
import os

app = Flask(__name__)
CORS(app)

DOWNLOAD_FOLDER = './assets'

@app.route('/')
def hello_world():
    return "Hello, world!"

def download():
    youtube_url = request.args.get('youtubeURL')

            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '96',
            }],
            'update_extractor': True,
            'nocheckcertificate': True,
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(autonumber)s.%(ext)s'),
            'verbose': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        # Assuming only one MP3 file is downloaded
        mp3_file_path = os.path.join(DOWNLOAD_FOLDER, os.listdir(DOWNLOAD_FOLDER)[0])

        return send_file(mp3_file_path, as_attachment=True)

    else:
        return jsonify({"error": "Invalid request"}), 400
        
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
