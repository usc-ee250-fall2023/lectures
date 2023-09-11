from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
succeeded = set()
@app.route("/")
def hello():
    return "<h1>Please try to make your post request to <tt>/verify</tt> </h1>"

@app.route("/check", methods=["GET"])
def check():
    global succeeded
    myname = request.args.get("name")
    if myname  not in succeeded:
        return myname + " not in list of successful submissions"
    else:
        return myname + " has successfully submitted"

@app.route('/submit', methods=["POST"])
def verify_stu():
    global succeeded
    print("Here")
    print(request)
    content = request.json
    print(content)
    if("scores" not in content):
        return "key 'scores' not found", 400
    elif("name" not in content):
        return "key 'name' not found", 400
    elif("dp-the-best" not in content):
        return "key 'dp-the-best' not found", 400
    scores = content["scores"]
    if( len(scores) < 3):
        return "not enough scores", 400
    if(scores[0] != 56 or scores[1] != 66 or scores[2] != 56):
        return "Wrong scores!", 400
    if(content["dp-the-best"] == False):
        return "You should consider changing your taste in soft drinks", 400
    succeeded.add(content["name"])
    return "You have succeeded!"

		
if __name__ == "__main__":
    app.run()

