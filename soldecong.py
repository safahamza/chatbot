import urllib
import json
import os
from flask import flask
from flask import request
from flask import make_response

app = flask(_name_)
@app.route('/webhook', method=["POST"])
def webhook()
    req = request.get_json(silent=true, force=true)
	print ("Request:")
	print(json.dumps(req, indent=4))
	res = makeWebhookResult(req)
	res = json.dumps(res, indent=4)
	print(res)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	reurn r
	
def makeWebhookResult(req)
    if req.get("result").get("action")!= "soldeConge"
	   return{}
	result = req.get("result")
	parameters = result.get("parameters")  
	typeConge =  parameters.get("conge")
	conges={'congées payés':10, 'RTT':5}
	if typeConge in {"congés", "congé", "conge", "conges"} :
	   if conges['congées payés']+ conges['RTT'] == 0 :
	      speech= "Vous n'avez pas de congés"
	   else:
	      speech= "Vous avez " conges['congées payés']+ conges['RTT']  " jours de congés"

	else:
	     if typeConge == "RTT":
		    speech = "vous avez"  conges['RTT'] "jours  de RTT"
			
    print("Response :")
	print(speech)
	return{
	       "speech": speech,
		   "displayText": speech
		   }
if _name_ == '_main_'
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
     
	   
	
	
	
	
	
	
    
