from flask import Flask,render_template,make_response
import time,re,urllib
app = Flask(__name__)
chop_time = lambda x: int(str(x)[:-3])
@app.route('/<ts>')
def index(ts=None):
	ts = str(urllib.unquote(ts))
	if ts != None:
		if re.match(r'[A-z].+',ts) != None:
			natural = ts
			unix = chop_time(time.mktime(time.strptime(ts,'%B %d, %Y')))
		else:
			unix = ts
			natural = time.strftime('%B %d, %Y',time.localtime(float(ts)))
	else:
		unix = 'null'
		natural = 'null'

	resp = make_response(str({'unix': unix,'natural': natural}),200)
	resp.headers['Content-Type'] = 'application/json'
	return resp

@app.route('/')
def ndx():
	resp = make_response(str({'unix': 'null','natural': 'null'}),200)
	resp.headers['Content-Type'] = 'application/json'
	return resp

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=80)