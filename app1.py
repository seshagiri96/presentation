# app1.py

from flask import Flask, request, jsonify, render_template, redirect, \
					make_response, session, g
from contextlib import closing
import sqlite3
from uuid import uuid4

import string

import json

import md5

DATABASE = '/home/devloper/sessions.db'
SESSION_REFRESH_EACH_REQUEST=False
	                   
application = Flask(__name__)
application.config.from_object(__name__)

user_credentials = {'test':{'username':'test','password':'test','firstname':'test','lastname':'test','biodata':'test'}}
loggedin_users = []


def _generate_sid():
    return str(uuid4())

@application.before_request
def before_request():
	g.db = connect_db()

@application.route('/',methods=['GET','POST'])
@application.route('/index.html')
def index():
	print 'enterd index'
	#username = request.cookies.get('userId')
	if 'username' in session:
		return jsonify({"loggedin":True})
	else:
		return jsonify({"loggedin":False})

@application.route('/md5', methods = ['POST'])
def ajax_request():
	key_string = request.form['key_string'] 
	digest_message = md5.new()
	digest_message.update(key_string)
	tmp = digest_message.hexdigest()
	print tmp

	return jsonify(dm=tmp)


#----------------------------------------------


@application.route('/register.html', methods = ['GET','POST'])
def register():
	return render_template('register.html')

@application.route('/login.html',methods = ['GET','POST'])
def login():
	print "entered login.html"
	try:	
		return render_template('login.html')
	except:
		return "login.html not found!!"

#----------------------------------------------


@application.route('/register_end',methods = ['GET', 'POST'])
def register_end():
	code=0
	dataDict = request.data
	dataDict=json.loads(dataDict)
	print dataDict
	if dataDict['username'] not in user_credentials:
		user_credentials[dataDict['username']] = dataDict
		response = "User registered Successfully"
		code =1
		#return redirect('/register_success')
	else:
		response = "Username already taken"
	print response
	return jsonify(response=response,code=code)

@application.route('/login_end',methods = ['GET','POST'])
def login_end():
	if request.method == 'POST':
		code =0
		dataDict = request.data
		print dataDict
		dataDict = json.loads(dataDict)
		if dataDict['username'] in user_credentials:
			user = user_credentials[dataDict['username']]
			if dataDict['password'] == user['password']:	
				response = "Successfully logged in"
				session['username'] = dataDict['username']
				myssid = _generate_sid()
				save_session(myssid,"LOGGED IN")
				print session
				code =1

				response = make_response(jsonify(response=response,code=code,userData=user))
				response.set_cookie('myssid',myssid)
				return response
			else:
				response = "Incorrect password !!"
		else:
			response = "User doesn't exists !!"

		print response
		return jsonify(response=response,code=code)
	else:
		return jsonify(response='Please make a post request',code=0)

@application.route('/register_success',methods=['GET'])
def register_success():
	return 'successfully registerd'

@application.route('/profile_end',methods = ['GET','POST'])
def login_success():
	#username=request.cookies.get('userId')
	#sess = request.cookies.get('session')
		
	if 'username' in session :
		print session
		user = user_credentials[session['username']]
		#return render_template('profile.html',user=user_credentials[session['username']])
		return jsonify({'loggedin':True, 
						'firstname':user['username'],
						'lastname' :user['lastname'],
						'username' :user['username'],
						'biodata'  :user['biodata' ] })
	#if username in loggedin_users:
	#	userData = user_credentials[username]
	else:
		
		return jsonify({'loggedin':False})

@application.route('/logout_end',methods=['GET','POST'])
def logout():
	#username = request.cookies.get('userId')
	if 'username' in session:
		print "Existing user logged out!!"
		try:
			session.pop('username',None)
			myssid = request.cookies['myssid']
			print myssid
			delete_session(myssid)
			response = make_response(jsonify({'loggedout':True}))
			response.set_cookie('myssid','')
			return response
		except:
			return jsonify({'loggedout':False})
	else:
		print 'User not loged in!!'
		return jsonify({'loggedout':True})

def connect_db():
    return sqlite3.connect(application.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
	    with application.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
	    db.commit()

def save_session(sess_id, status):
	g.db.execute('INSERT INTO sess_table (sess_id, status) VALUES (?, ?)', [sess_id, status])
	g.db.commit()

def delete_session(sess_id):
	g.db.execute('DELETE FROM sess_table WHERE sess_id = ?', [sess_id])
	g.db.commit()

application.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
	application.run(debug = True,port=3031)
