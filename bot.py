from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/locate', methods=['GET'])
def locate_image():
    image_url = request.args.get('img')
    if not image_url:
        return "Error: Image URL is missing.", 400

    result = process_image(image_url)
    return result

def process_image(image_url):
    url = 'https://us-central1-phaseoneai.cloudfunctions.net/locate_image'

    headers = {
        'Host': 'us-central1-phaseoneai.cloudfunctions.net',
        'Content-Type': 'multipart/form-data; boundary=dart-http-boundary-zEDT_cKh5lXBX_ZzZw9ZYLB8wPP+Zf-njJ-Oz80+cHqm2Sb2y1W',
        'Origin': 'https://geospy.web.app',
        'Referer': 'https://geospy.web.app/',
    }

    # Fetch image data from URL
    image_data = requests.get(image_url).content

    data = (
        b'--dart-http-boundary-zEDT_cKh5lXBX_ZzZw9ZYLB8wPP+Zf-njJ-Oz80+cHqm2Sb2y1W\r\n'
        b'Content-Disposition: form-data; name="list_of_strings"\r\n\r\n'
        b'[]\r\n'
        b'--dart-http-boundary-zEDT_cKh5lXBX_ZzZw9ZYLB8wPP+Zf-njJ-Oz80+cHqm2Sb2y1W\r\n'
        b'Content-Type: image/jpeg\r\n'
        b'Content-Disposition: form-data; name="image"; filename="online_image.jpg"\r\n\r\n'
        + image_data +
        b'\r\n'
        b'--dart-http-boundary-zEDT_cKh5lXBX_ZzZw9ZYLB8wPP+Zf-njJ-Oz80+cHqm2Sb2y1W--\r\n'
    )

    response = requests.post(url, headers=headers, data=data)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
