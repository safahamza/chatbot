import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook() :
    req = request.get_json(silent=true, force=true)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req) :
    if req.get("result").get("action")!= "soldeConge":
       return{}
    result = req.get("result")
    parameters = result.get("parameters")  
    typeConge = parameters.get("conge")
    conges={'congées payés':10, 'RTT':5}
    #Pas de congés
    if conges['congées payés']+ conges['RTT'] == 0 :
       speech="Vous n'avez pas de congés"


    #sans spécification du type de congés: Réponse ventilée
    elif typeConge == "congés" :
         speech= "Vous avez " + str(conges['congées payés']) + " jours de congés payés et " + str(conges['RTT'])+ "jours deRTT"
    #spécification du type
 
       #RTT
    elif typeConge == "RTT":
          speech = "vous avez"+ str(conges['RTT']) + "jours  de RTT"
       #congés payés
    elif typeConge == "congés payés" :
          speech = "vous avez"+ str(conges['congées payés']) + "jours  de congés payés"

    print("Response :")
    print(speech)
    return{
           "speech": speech,
           "displayText": speech
          }
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
     
   






    
