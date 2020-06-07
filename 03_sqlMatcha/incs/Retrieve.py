# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendVerificationText(e_mail, userIdNo):
	_from = "team@matcha.co.za"
	_to = e_mail
	_subject = "Matcha's Account Verification"
	_text = ''.join((
		'<p>',
			'Matcha\'s team Thanks you for signing up.',
			'<br>',
			'<br>',
			'Please click <a href="%s">here</a> to activate your account.' % (
				'http://0.0.0.0:4000/verify' + userIdNo
			),
			'<br>',
			'<br>',
			'Regards!',
		'</p>'
	))
	message = Mail(
		from_email = _from,
		to_emails = _to,
		subject = _subject,
		html_content = _text
	)
	try:
		sg = SendGridAPIClient('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')
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
		print 'A verification eMail was sent to %s' % e_mail
	except Exception as e:
		print(e)

# -> https://temp-mail.org/en/

def sendEmail(userIdNo, realName, e_mail):
	_from = "team@matcha.co.za"
	_to = e_mail
	_subject = "Matcha's Account Password Retrieve"
	_text = ''.join((
		'<p>',
			'Dear %s, (userIdNo: %s)' % (realName, userIdNo),
			'<br>',
			'<br>',
			'Please click <a href="%s">here</a> to retrieve your password.' % (
				'http://0.0.0.0:4000/newPasswordForm_' + userIdNo
			),
			'<br>',
			'<br>',
			'Regards!',
		'</p>'
	))
	message = Mail(
		from_email = _from,
		to_emails = _to,
		subject = _subject,
		html_content = _text
	)
	try:
		sg = SendGridAPIClient('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')
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
		print 'A verification eMail was sent to %s' % e_mail
	except Exception as e:
		print(e)
	return None
