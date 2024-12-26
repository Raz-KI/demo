from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from evaluation.precise_evaluation import evaluate_ssc_precis
from evaluation.essay_evaluation import evaluate_ssc_essay
from evaluation.letter_evaluation import evaluate_ssc_letter

app = Flask(__name__)


with open('static/questions/tier1_json/paper1.json', 'r') as file:
    tier1_questions = json.load(file)

with open('static/questions/tier1_json/paper1.json', 'r') as file:
    tier2_questions = json.load(file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tier1')
def tier1():
    return render_template('tier1.html', questions=tier1_questions)


@app.route('/tier1_result', methods=['POST'])
def tier1_result():
    score = 0
    answers = request.form  
    print(answers)
    for section in tier1_questions:
        
        # print("section = ",section)
        for question in section['data']:
            
            question_identifier = question['question']  # Fetch the question ID
            # print(qid)
            # print("q id = ",str(question)[0])
            
            if str(question_identifier) in answers:
                user_answer = answers[str(question_identifier)]
                print(user_answer)
                correct_answer = question['answer']
                
                if user_answer == correct_answer:
                    score += 2  
                else:
                    score -= 0.5 

    
    print(f"Final Tier 1 Score: {score}")

    if score >= 20:
        return render_template('tier1_result.html', score=score, pass_tier1=True)
    else:
        return render_template('tier1_result.html', score=score, pass_tier1=False)


@app.route('/tier2')
def tier2():
    return render_template('tier2.html', questions=tier2_questions)



@app.route('/tier2_result', methods=['POST'])
def tier2_result():
    score = 0
    answers = request.form  
    print(answers)
    for section in tier2_questions:
       
        # print("section = ",section)
        for question in section['data']:
            
            question_identifier = question['question']  # Fetch the question ID
            # print(qid)
            # print("q id = ",str(question)[0])
            
            if str(question_identifier) in answers:
                user_answer = answers[str(question_identifier)]
                print(user_answer)
                correct_answer = question['answer']
                
                if user_answer == correct_answer:
                    score += 3  
                else:
                    score -= 1  

    
    print(f"Final Tier 2 Score: {score}")

    if score >= 20:
        return render_template('tier2_result.html', score=score, pass_tier2=True)
    else:
        return render_template('tier2_result.html', score=score, pass_tier2=False)


@app.route('/tier3')
def tier3():
    return render_template('tier3.html')


@app.route('/tier3_result', methods=['POST', 'GET'])
def tier3_result():
    question1 = "Write an essay on 'Importance of education in present time'. (250 words)"
    question2 = "You are Sunita/Sunil, resident of Gandhi road, Dwarka, New Delhi, 110083, write a letter to manager, G D resaurant complaining about their poor service and the quality of food. (150 words)"
    answer1 = request.form.get('answer1')
    answer2 = request.form.get('answer2')
    result1=evaluate_ssc_essay(question1,answer1,'easy')
    result2=evaluate_ssc_letter(question2,answer2,'easy')
    return render_template('tier3_result.html',result1=result1,result2=result2 )


if __name__ == '__main__':
    app.run(debug=True)


