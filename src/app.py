from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # Pretty JSON

@app.route('/api/v1/details')
def details():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message_1' : 'Hi 😊 This is a Test <3 ^m',
        'env': 'dev',
        'app_name': 'prerna'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#'/api/v1/details'
#'/api/v1/healthz'
