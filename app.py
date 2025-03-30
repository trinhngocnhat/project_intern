from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    input_text = request.form['input_text']
    detected_lang = request.form['detected_lang']
    desired_lang = request.form['desired_lang']

    # Giả lập kết quả dịch (bạn có thể tích hợp API dịch thực sự ở đây)
    translated_text = f"Translated '{input_text}' from {detected_lang} to {desired_lang}"

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
