from flask import Flask,jsonify,render_template,request

from project_app.utils import IrisData


# Creating instance here
app = Flask(__name__)



@app.route("/")    # HOME API
def hello_Flask():
    print("Welcome to the Iris Flower  Prediction System")   # console
     
    return render_template("index.html")     # for html
    #return "Success"                        # for postman



@app.route("/predict_flower",methods = ["POST","GET"])
def get_predicted_flower():
    if request.method == "GET":
        print("WE are in a GET method")

        
        

        Id = (request.args.get("Id"))
        SepalLengthCm = (request.args.get("SepalLengthCm"))
        SepalWidthCm = (request.args.get("SepalWidthCm"))
        PetalLengthCm = (request.args.get("PetalLengthCm"))
        PetalWidthCm = (request.args.get("PetalWidthCm"))
        

        print("******************* Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm ***************************\n",Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)

        flower_pre = IrisData(Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
        flower = flower_pre.get_predicted_Iris()
        return render_template("index.html",prediction = flower)

   # return jsonify({"Result":f"Predicted Charges is {charges}/- Rs."})


print("__name__ ---->",__name__)

if __name__ == "__main__":
    app.run()
