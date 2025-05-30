from flask import Flask, render_template, request, jsonify
from Cipher.caesar import CaesarCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/api/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    try:
        data = request.form
        plain_text = data.get('plain_text')
        key = int(data.get('key'))
        if not plain_text or key < 0:
            return jsonify({'error': 'Invalid input: plain_text and positive key required'}), 400
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({
            'type': 'encrypt',
            'text': plain_text,
            'key': key,
            'output': encrypted_text
        })
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input: plain_text and valid key required'}), 400

@app.route("/api/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    try:
        data = request.form
        cipher_text = data.get('cipher_text')
        key = int(data.get('key'))
        if not cipher_text or key < 0:
            return jsonify({'error': 'Invalid input: cipher_text and positive key required'}), 400
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({
            'type': 'decrypt',
            'text': cipher_text,
            'key': key,
            'output': decrypted_text
        })
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input: cipher_text and valid key required'}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)