from __future__ import unicode_literals

from django.db import models
import bcrypt, re

# Create your models here.
class UserManager(models.Manager):
	def login(self, post_data):
		user = User.objects.get(username = post_data.POST['l_username'])
		password = post_data.POST['l_password']
		print (password)
		print (user.password)
		try:
			user = User.objects.get(username = post_data.POST['l_username'])
			password = post_data.POST['l_password']
			print (password)
			print (user.password)
			if bcrypt.hashpw(password.encode(), user.password.encode()):
				return (True, user)
		except:
			print "excepted"
			pass
		return (False, None)

	# returns false if invalid, returns true if logged them in successfully
	def register(self, post_data):
		# validate inputs
		errors = self.validate_registration(post_data)
		# if valid, make user... or not if invalid
		if len(errors) > 0:
			return (False, errors)

		hashed_pw = bcrypt.hashpw(post_data.POST['r_password'].encode(), bcrypt.gensalt())

		new_user = self.create(
			first_name 	= post_data.POST["r_first"],
			last_name 	= post_data.POST["r_last"],
			email 		= post_data.POST["r_email"],
			username 	= post_data.POST["r_username"],
			password 	= hashed_pw
		)
		print "a peep was added"
		return (True, new_user)


	def validate_registration(self, post_data):
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		# input lengths/presence
		errors = []
		if not 2 <= len(post_data.POST['r_first']) <= 45:
			print "error1"
			errors.append("first has gotta be betwist 2 and 45 characters in length")
		if not 2 <= len(post_data.POST['r_last']) <= 45:
			print "error2"
			errors.append("last has gotta be betwixt 2 adn 45 characters in length")
		if not 2 <= len(post_data.POST['r_username']) <= 45:
			print "error3"
			errors.append("username has gotta be betwixt 2 and 45 characters in length")
		if not 8 <= len(post_data.POST['r_password'])  <= 100:
			print 'error4'
			errors.append("password has to be at least 8")	
		if not 2 < len(post_data.POST['r_email']) <= 100:
			print "error5"
			errors.append("email needs to be longer than 2")
		# unique username
		if len(User.objects.filter(username = post_data.POST['r_username'])) > 0:
			print "error6"
			errors.append("invalid username")
		# # email is an email
		if not EMAIL_REGEX.match(post_data.POST['r_email']):
			print "error7"
			errors.append('is that really how you email address?')
		# # password and confirm password match eachother
		if not post_data.POST['r_password'] == post_data.POST['r_password2']:
			print "error8"
			errors.append("those passwords gotta be the same!")
		return errors


class User(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	email = models.CharField(max_length = 100)
	username = models.CharField(max_length = 45)
	password = models.CharField(max_length = 254)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()

	def __unicode__(self):
		return self.username

	def full_name(self):
		return first_name.concat(' ', last_name)
