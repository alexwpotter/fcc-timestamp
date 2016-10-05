from flask import Flask,render_template,make_response
import time,re,urllib
app = Flask(__name__)
chop_time = lambda x: int(str(x)[:-3])
@app.route('/<ts>')
def index(ts):
	ts = str(urllib.unquote(ts))
	if ts:
		if re.match(r'[A-z].+',ts) != None:
			natural = ts
			unix = chop_time(time.mktime(time.strptime(ts,'%B %d, %Y')))
		else:
			unix = ts
			natural = time.strftime('%B %d, %Y',time.localtime(float(ts)))
		resp = make_response(str({'unix': unix,'natural': natural}),200)
		resp.headers['Content-Type'] = 'application/json'
		return resp
	else:
		return 'null'

if __name__ == "__main__":
	app.run("0.0.0.0")