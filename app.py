import model as fl
from flask import Flask, render_template, request, jsonify
# from flask_socketio import SocketIO, send

app = Flask(__name__)



 # @app.route('/', methods=['GET', 'POST']) handle routing when use make either a get or post request

@app.route('/', methods=['GET', 'POST'])
def search():
	if request.method == 'POST':
		text = request.form['projectFilepath']
		term = request.form['term']
		data=fl.get_data_for_web(text, term)
		city_info=fl.get_from_db(text)

	else:
		data=fl.get_data_for_web("Ann Arbor")
		city_info=fl.get_from_db("Ann Arbor")
	return render_template("final_project.html", city_info=city_info, data=data)




# @app.route('/process', methods=['POST']) is to handle all the AJAX call from client side (javascript from client side, and information would be updated without refreshing the page)

@app.route('/process', methods=['POST'])
def chat_bot():

	input_text=request.data
	reply=fl.get_from_mitsuku(input_text)
	return jsonify({"reply":reply})









# app.config["SECRET_KEY"]="mysecret"
# socketio=SocketIO(app)

# @socketio.on('message')
# def handleMessage(msg):
# 	msg=fl.get_from_mitsuku(msg)
# 	send(msg, broadcast=True)

if __name__ == '__main__':
	app.run(debug=True)

	# socketio.run(app, debug=True)

