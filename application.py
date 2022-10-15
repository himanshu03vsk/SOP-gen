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
        prompt = f''' Write statement of purpose using the details and template given below -

        template- To,
        The Visa Officer
        High Commission of {argdict["tarcont"]} 
        Write captial of {argdict["loc"]} here
        Subject: Statement of Purpose / Explanation regarding previous student visa refusal
        Dear Sir/ Madam,
        I wish to provide the following additional information supporting my application for a student visa.

        Introduce yourself along stating your date of birth and location and which program you applied to at what college
        Write that you got rejected for visa when you applied previously and list the reasons in bullet points
        Start with writing what program you have applied to and the eligibility criteria
        write that you are going to explain the issues that were present in previous letter

        Purpose of Visit and Reason to Return :
        write why do you wish to visit {argdict["tarcont"]} and study the course you have chosen, link this to your parents and curiosity
        Write how your parents encouraged and supported you regarding your studies and how the course has helped you
        Mention your academic skills and write your academic percentages like what school you went how was your performance there and percentages, write what college you went to complete your bachelor degree, along with that mention any extracurricular activities you did.
        Write why the {argdict["course"]} is your favourite and your aptitude for that.
        Write what have you learned in your bachelors course and if it relates to the course you are planning to choose.
        Write any internships or any kind of work experience you did relevant to the course.
        Write to pursue the course you did IELTS and your marks in that.
        Write the subjects offered by the course in {argdict["college"]}
        Write why the course will be advantageous for you and write about job market for {argdict["course"]} in {argdict["loc"]}
        Write if you have any gap

        Reason to Return:
        Write that you will return to India with your degree and how it will affect you in recruitment process, explain this in 1 paragraph
        Write the job prospects of the course you chose in India and its history in your country write some historical data and stats about the job availability and salary packages and how it affects the GDP, explain this in 1 paragraph
        Write how the course you chose will be crucial for india and mention its responsibility explain this in 1 paragraph
        Write some average salary of a typical cs graduate from {argdict["tarcont"]}, explain this in 1 paragraph
        Write reasons other than job prospects like family being your reason to return to India in bullet points 

        Proof of Financial Funds:
        Write your finances here and how your parents will support you, explain this in 1 paragraph

        Language Abilites:
        Write your ielts score here and your language skills

        Why {argdict["tarcont"]} for education and why {argdict["college"]}, explain this in 1 paragraph?
        Write about the international exposure you will get and communication skills, explain this in 1 paragraph
        write various advantages you get by studying in {argdict["tarcont"]} explain this in 1 paragraph
        write any course time related fact like how some country have shorter study duration, explain this in 1 paragraph
        Write advantages of your college ,explain this in 1 paragraph

        Conclusion:
        conclude the letter mentioning that you have presented the necessary information and reasons of return in the document and resolved all the concerns of last visa officer. Write your sole purpose of visiting canada
        write that you are looking for positive response

        Sincerely,
        {argdict["name"]}
        


        Details-
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

        Statement of purpose-
'''
        response = openai.Completion.create(model="text-davinci-002",
                                            prompt=prompt,
                                            temperature=1,
                                            max_tokens=3000,
                                            top_p=0.5,
                                            frequency_penalty=0.74,
                                            presence_penalty=0.36)

        # print(response["choices"][0]["text"])
        return render_template("index.html", response=response["choices"][0]["text"], resFlag=True)
    else:
        return render_template("index.html", resFlag=False)


if __name__ == '__main__':
    app.run()















