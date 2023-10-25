from flask import Flask,render_template,request,url_for,redirect
import requests

list_1=[]
app=Flask(__name__)

url="https://api.mfapi.in/mf/"
@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
       name=request.form.get("name")
       fund_code=request.form.get("fund_code")
       funds=requests.get(url+str(fund_code))
       fund_house1=funds.json().get("meta").get("fund_house")
       investment=request.form.get("investment")
       uni_theld=request.form.get("uni_theld")
       nav=funds.json().get("data")[0].get("nav")


       dict_1={}
       dict_1.update({"name":name})
       dict_1.update({"fund_house1":fund_house1})
       dict_1.update({"investment":investment})
       dict_1.update({"uni_theld":uni_theld})
       dict_1.update({"nav":nav})
       current_value=float(dict_1.get("nav"))*int(dict_1.get("investment"))
       dict_1.update({"current_value":current_value})
       print(current_value)
       growth=(dict_1.get("current_value"))-int(dict_1.get("uni_theld"))
       dict_1.update({"growth":growth})
       list_1.append(dict_1)

    return render_template("index.html",fd=list_1)

@app.route('/edit/<string:id>',methods=["GET","POST"])
def edit(id):
    if request.method=="POST":
        dict_1=list_1[int(id)-1]
        dict_1.update({"name":request.form.get("name")})
        dict_1.update({"fund_code":request.form.get("fund_code")})
        dict_1.update({"investment":request.form.get("investment")})
        dict_1.update({"uni_theld":request.form.get("uni_theld")})
        return redirect(url_for("home"))
    a=list_1[int(id)-1]
    return render_template("edit.html",a=a)
@app.route('/delete/<string:id>')
def delete(id):
    list_1.pop(int(id)-1)
    return render_template("index.html",an=list_1)
           
if __name__ =="__main__":
    app.run(debug=True)  