from flask import Flask,request,jsonify,render_template

app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/messages', methods=['GET','POST'])
def receive_message():
    try:
        data = request.json  # Corrected: Use request.json without parentheses
        message = data.get('message', '')
        print(f"Received message: {message}")
        return jsonify({"status": "Message received!"})
    except Exception as e:
        return jsonify({"status": "Error: " + str(e)})


if __name__=='__main__':
    app.run(debug=True,port=8888)