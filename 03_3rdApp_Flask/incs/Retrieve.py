import smtplib

gMailUser = 'saburadi@student.wethinkcode.co.za'
gMailPass = 'pmjddppqmkknnjim'

def sendVerificationText(app, e_mail, userIdNo):
	try:
		server = smtplib.SMTP('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gMailUser, gMailPass)

		_from = "From: saburadi@student.wethinkcode.co.za"
		_to = "To: %s" % e_mail
		_subject = "Matcha's Account Verification"
		_text = """
			'<p>',
				'Matcha\'s team Thanks you for signing up.',
				'',
				'Please click <a href="%s">here</a> to activate your account.' % (
					'http://0.0.0.0:4000/verify' + userIdNo
				),
				'',
				'Regards!',
			'</p>',
		"""
		_text = ''.join((
			_from,
			_to,
			_subject,
			_text
		))

		server.sendmail(gMailUser, e_mail, _text)
		server.close()
	except Exception as e:
		print "failed to send; %s" % str(e)

def sendEmail(hashName, e_mail):
	return None
