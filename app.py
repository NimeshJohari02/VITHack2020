from flask import Flask, render_template, url_for, request
from preprocess_vithack import *
from keras.models import load_model
from output_classify import *


app = Flask(__name__)

@app.route('/',  methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route('/result',  methods=['POST', 'GET'])

def result():
    if request.method == 'POST':
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']
        q8 = request.form['q8']
        q9 = request.form['q9']
        q10 = request.form['q10']
        q=[q2,q3,q4,q5,q6,q7,q8,q9,q10]
        pre_data = preprocess(q)
        model = load_model('model.h5')
        output = model.predict(pre_data)
        score = get_score(output)
        score_round2 = round(score, 2)
        score_round = round(score)
        print(score_round2)
        print(score_round)
        recom = ""
        if score_round<=3:
            recom = "Hello" + q1 + " . It seems that you are going strong .  You are seeing this message because you did relatively well in our psych evaluation . It seems that you are going strong and are not on a path which would hamper your health.. What we recommend you is that you take a few days off from studies .. Probably go out on a trip with your mom and dad . We know you may feel that you are completely fine but there's still a ripple of anxiety in your thoughts and you must not let it go unnoticed . It's a well heard saying that a stitch in time saves nine . If you feel anything's bothering you feel free to reach out to any of us and open up . We may be able to help you analyze  the scenario a little better"
        elif score_round<=7:
            recom = "Hang in there " + q1 + " . It must be a tough and challenging time . We all know the competition is getting more and more challenging as we say but it does not  mean that we lose all hope and sit back . It these challenging times that act as a true strength of mettle .Your journey may be ordinary but the ending will be phenomenal only if you believe so . We would recommend you that sometime in a day you sit back and meditate. We recommend the Headspace Library for self meditation purposes also may recommend few minutes from your schedule to give a try to yoga . Also whenever you feel the ship sinking think about how much effort you've made to keep this brig afloat . All the effort that you have been putting in should and will not go to waste only if you meditate for some time and spent some quality time with your family so you are not sucked in by the monotonic and vicious cycle of loneliness and depression"
        else:
            recom = """<br><br>Hey there """ + q1 + """ Seems like you are facing a bit of an issue regarding your personal health and here we are concerned for your health and well-being in this competitive environment . These are the steps that we recommend <br><br> <ol><li> Visit your nearest  Doctor / psychiatrist for a consultation and adhere to the medicines that he/she prescribes .</li> <li> One On  One counseling sessions with some registered practitioner who would help you to open up to people </li>
            <li> Consider talking to Your friends . Just remember that they are always there and they would always be at your side at whatever may be the circumstances </li>
            <li> If you feel that something is bothering you . You should let any one know keeping it inside would just work life a blow-torch to your heart as well as your emotions .</li>
            <li> Distance yourself from people that you think have a negative impact on your personality </li>
            <li> Always Remember That your health is the first priority . For anybody be it you or your parents your health is of utmost importance and nothing can overshadow that fact.</li>
            <li> If prescribed medication you should consider taking them on time as they will help you mellow the tension down and would help you in any and all aspects of your educational journey.</li>
            </ol>"""

        summary = ""
        if score_round<=3:
            summary = "You're doing fine just a few pit-stops and you'll be on your way to success"
        elif score_round<=7:
            summary = "It's a forest a deep one but don't worry the moonlight shall guide you"
        else:
            summary = "The guardian at the end of the dark tunnel awaits your arrival"
        return render_template('Result.html', score = score_round, rec = recom, Summary = summary)


if __name__ == "__main__":
    app.run(debug=True)

