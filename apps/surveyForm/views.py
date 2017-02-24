from django.shortcuts import render, redirect
  

def index(request):
	return render(request,'surveyForm/index.html')


def create(request):
	print ('*'*1000)
	if request.method == 'POST':
		request.session['data'] = {
		'Name' : request.POST["name"],
		'Location' : request.POST["location"],
		'Language' : request.POST["language"],
		'Comment' : request.POST["comment"],

		}
		
	# else:
	# 	return redirect('/')
	
	return redirect('/surveyForm/users.html')

def users(request):
	# if request.method == 'POST':
	# 	context = {
	# 	'name' : name,
	# 	'location' : location
	# 	'language' : language
	# 	'comment' : comment
	# }

	return render(request,'surveyForm/users.html')






# @app.route("/")
# def index():
# 	return render_template('index.html')

# @app.route("/users", methods=["POST"])
# def create_user():
# 	# print ("Got Post Info")
# 	name = request.form["name"]
# 	location = request.form["location"]
# 	language = request.form["language"]
# 	comment = request.form["comment"]

# 	return render_template("result.html",name = name, location = location, language = language, comment = comment )
