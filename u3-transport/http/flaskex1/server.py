from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
scores = []
@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/avg/")
def do_avg():
    if(len(scores) == 0):
        return "No scores\n"
    #return str(sum(scores)/len(scores))
    return render_template('result.html', mycount=str(len(scores)), myavg=str(sum(scores)/len(scores)))

@app.route("/lookup", methods=["GET"])
def lookup_score():
    myidx = int(request.args.get("index"))
    if myidx >= len(scores):
        return "error, index out of range\n"
    else:
        return str(scores[myidx])+"\n"

@app.route('/scores', methods=["POST"])
def add_score():
    global scores

    if request.method == "POST":
        if 'score' in request.form:
            scores.append( int(request.form['score']) )
            #flash(request.form['score'])
            return "You added score: " + request.form['score'] + " via formdata\n"
        elif request.is_json:
            if 'score' in request.json:
                scores.append( int(request.json['score']))
                return "You add score: " + request.json['score'] + " via json\n"
            else:
                return "Expected form data\n"
    return "error\n"

		
if __name__ == "__main__":
    app.run()

