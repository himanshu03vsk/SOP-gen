import os
from dotenv import load_dotenv
import openai
load_dotenv()
openai.api_key=os.getenv('API_KEY')
from flask import Flask, flash, redirect, render_template, request, session, url_for



# Configure application 
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
# Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        argdict = {}
        argdict["name"] = request.form.get('name')
        argdict["dob"]  = request.form.get('dob')
        argdict["loc"] = request.form.get('currloc')
        argdict["contact"] = request.form.get('contact')
        argdict["tarcont"] = request.form.get('tarcont')
        argdict["college"]= request.form.get('college')
        argdict["course"] = request.form.get('course')
        argdict["ielts"] = request.form.get('ielts')
        argdict["visa"] =request.form.get('visa')
        argdict["academic"] = request.form.get('academics')
        argdict["hobbiesexp"] = request.form.get('hobbiesexp')
        argdict["parinfo"] = request.form.get('parinfo')
        argdict["addinfo"] = request.form.get('addinfo')
        argdict["gap"] = request.form.get('gap')
        argdict["fee"] = request.form.get('fee')
        argdict["sopfee"] = request.form.get('sopfee')
        prompt = f'''
        Generate statement of purpose because you got previously refused for visa.
        using below information, explain the reasoning behind choosing the college and country and follow the format given in the example below
        example: To,
        The Visa Officer
        High Commission of {argdict["tarcont"]} 
        Write captial of {argdict["loc"]}
        Subject: Statement of Purpose / Explanation regarding previous student visa refusal
        Dear Sir/ Madam,
        introduce yourself in brief
        mention your academic skills and write your academic percentages 
        mention what  is your family background and about parents what your father does what your mom is doing etc in detail
        use the family information and relevent information as a reason for returning to {argdict["loc"]}
        mention finances and how your parents will support you
        mention you need to return to your home country due to family and current background
        show proof that you have sufficient money
        conclusion:
        conclude the letter mentioning that you hope that you will definately return to {argdict["loc"]} 



        Details:
        Name- {argdict["name"]}
        Date of birth- {argdict["dob"]}
        Current location- {argdict["loc"]}
        Contact Number- {argdict["contact"]}
        Country for which applying- {argdict["tarcont"]}
        College Name- {argdict["college"]}
        Course- {argdict["course"]}
        IELTS(Overall, Listening, Reading, Writing, Speaking)- {argdict["ielts"]}
        Academic Percentage and graduation information- {argdict["academic"]}
        Experience-{argdict["hobbiesexp"]}
        Information about parents- {argdict["parinfo"]}
        Any visa refusal in past- {argdict["visa"]}
        Any GAP- {argdict["gap"]}
        Anything relevent to course you are taking-{argdict["addinfo"]}
        GIC and fee info-  {argdict["fee"]}
        SOP fee paid- {argdict["sopfee"]}

        SOP:
'''
        response = openai.Completion.create(model="text-davinci-002",
                                            prompt=prompt,
                                            temperature=0.92,
                                            max_tokens=2500,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0)

        # print(response["choices"][0]["text"])
        return render_template("index.html", response=response["choices"][0]["text"], resFlag=True)
    else:
        return render_template("index.html", resFlag=False)


if __name__ == '__main__':
    app.run()


