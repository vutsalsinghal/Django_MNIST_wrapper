from django.shortcuts import render
from django.http import HttpResponse
from blog.models import UserProfile
from django import forms
from django.contrib.auth.models import User
import hashlib, datetime, random
from django.core.mail import send_mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context, Template
import smtplib

# Send confirmation email:-
html_email = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

						<html xmlns="http://www.w3.org/1999/xhtml">
						<head>
						  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
						  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
						  <title>[SUBJECT]</title>
						  <style type="text/css">

						@media screen and (max-width: 600px) {
							table[class="container"] {
								width: 95% !important;
							}
						}

						  #outlook a {padding:0;}
							body{width:100% !important; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; margin:0; padding:0;}
							.ExternalClass {width:100%;}
							.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {line-height: 100%;}
							#backgroundTable {margin:0; padding:0; width:100% !important; line-height: 100% !important;}
							img {outline:none; text-decoration:none; -ms-interpolation-mode: bicubic;}
							a img {border:none;}
							.image_fix {display:block;}
							p {margin: 1em 0;}
							h1, h2, h3, h4, h5, h6 {color: black !important;}

							h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {color: blue !important;}

							h1 a:active, h2 a:active,  h3 a:active, h4 a:active, h5 a:active, h6 a:active {
							  color: red !important;
							 }

							h1 a:visited, h2 a:visited,  h3 a:visited, h4 a:visited, h5 a:visited, h6 a:visited {
							  color: purple !important;
							}

							table td {border-collapse: collapse;}

							table { border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt; }

							a {color: #000;}

							@media only screen and (max-device-width: 480px) {

							  a[href^="tel"], a[href^="sms"] {
									text-decoration: none;
									color: black; /* or whatever your want */
									pointer-events: none;
									cursor: default;
								  }

							  .mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {
									text-decoration: default;
									color: orange !important; /* or whatever your want */
									pointer-events: auto;
									cursor: default;
								  }
							}


							@media only screen and (min-device-width: 768px) and (max-device-width: 1024px) {
							  a[href^="tel"], a[href^="sms"] {
									text-decoration: none;
									color: blue; /* or whatever your want */
									pointer-events: none;
									cursor: default;
								  }

							  .mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {
									text-decoration: default;
									color: orange !important;
									pointer-events: auto;
									cursor: default;
								  }
							}

							@media only screen and (-webkit-min-device-pixel-ratio: 2) {
							  /* Put your iPhone 4g styles in here */
							}

							@media only screen and (-webkit-device-pixel-ratio:.75){
							  /* Put CSS for low density (ldpi) Android layouts in here */
							}
							@media only screen and (-webkit-device-pixel-ratio:1){
							  /* Put CSS for medium density (mdpi) Android layouts in here */
							}
							@media only screen and (-webkit-device-pixel-ratio:1.5){
							  /* Put CSS for high density (hdpi) Android layouts in here */
							}
							/* end Android targeting */
							h2{
							  color:#181818;
							  font-family:Helvetica, Arial, sans-serif;
							  font-size:22px;
							  line-height: 22px;
							  font-weight: normal;
							}
							a.link1{

							}
							a.link2{
							  color:#fff;
							  text-decoration:none;
							  font-family:Helvetica, Arial, sans-serif;
							  font-size:16px;
							  color:#fff;border-radius:4px;
							}
							p{
							  color:#555;
							  font-family:Helvetica, Arial, sans-serif;
							  font-size:16px;
							  line-height:160%;
							}
						  </style>

						<script type="colorScheme" class="swatch active">
						  {
							"name":"Default",
							"bgBody":"ffffff",
							"link":"fff",
							"color":"555555",
							"bgItem":"ffffff",
							"title":"181818"
						  }
						</script>

						</head>
						<body>
						  <!-- Wrapper/Container Table: Use a wrapper table to control the width and the background color consistently of your email. Use this approach instead of setting attributes on the body tag. -->
						  <table cellpadding="0" width="100%" cellspacing="0" border="0" id="backgroundTable" class='bgBody'>
						  <tr>
							<td>
						  <table cellpadding="0" width="620" class="container" align="center" cellspacing="0" border="0">
						  <tr>
							<td>
							<!-- Tables are the most common way to format your email consistently. Set your table widths inside cells and in most cases reset cellpadding, cellspacing, and border to zero. Use nested tables as a way to space effectively in your message. -->


							<table cellpadding="0" cellspacing="0" border="0" align="center" width="600" class="container">
							  <tr>
								<td class='movableContentContainer bgItem'>



								  <div class='movableContent'>
							  <table cellpadding="0" cellspacing="0" border="0" align="center" width="600" class="container">
								<tr height="40">
								  <td width="200">&nbsp;</td>
								  <td width="200">&nbsp;</td>
								  <td width="200">&nbsp;</td>
								</tr>
								<tr>
								  <td width="200" valign="top">&nbsp;</td>
								  <td width="200" valign="top" align="center">
									<div class="contentEditableContainer contentImageEditable">
									  <div class="contentEditable" align='center' >
										<img src="http://allsafe.pythonanywhere.com/static/hello.jpg" width="325" height="255" data-default="placeholder" />
									  </div>
									</div>
								  </td>
								  <td width="200" valign="top">&nbsp;</td>
								</tr>
								<tr height="25">
								  <td width="200">&nbsp;</td>
								  <td width="200">&nbsp;</td>
								  <td width="200">&nbsp;</td>
								</tr>
							  </table>
							</div>

								  <div class='movableContent'>
									<table cellpadding="0" cellspacing="0" border="0" align="center" width="600" class="container">
									  <tr>
										<td width="100%" colspan="3" align="center" style="padding-bottom:10px;padding-top:25px;">
										</td>
									  </tr>
									  <tr>
										<td width="100">&nbsp;</td>
										<td width="400" align="center">
										  <div class="contentEditableContainer contentTextEditable">
													<div class="contentEditable" align='left' >
														<p<h2>Hi {{ name }}</h2>,
														  <br/>
														  <br/>
												Click on the button below to confirm your emial.</p>
													</div>
												  </div>
										</td>
										<td width="100">&nbsp;</td>
									  </tr>
									</table>
									<table cellpadding="0" cellspacing="0" border="0" align="center" width="600" class="container">
									  <tr>
										<td width="200">&nbsp;</td>
										<td width="200" align="center" style="padding-top:25px;">
										  <table cellpadding="0" cellspacing="0" border="0" align="center" width="200" height="50">
											<tr>
											  <td bgcolor="#1B5E20" align="center" style="border-radius:4px;" width="200" height="50">
												<div class="contentEditableContainer contentTextEditable">
														  <div class="contentEditable" align='center' >
															  <a style='color:#ffffff; text-decoration:none' target='_blank' href="{{ link }}" class='link2'>CONFIRM</a>
														  </div>
														</div>
											  </td>
											</tr>
										  </table>
										</td>
										<td width="200">&nbsp;</td>
									  </tr>
									</table>
								  </div>


								  <div class='movableContent'>
									<table cellpadding="0" cellspacing="0" border="0" align="center" width="600" class="container">
									  <tr>
										<td width="100%" colspan="2" style="padding-top:65px;">
										  <hr style="height:1px;border:none;color:#333;background-color:#ddd;" />
										</td>
									  </tr>
									  <tr>
										<td width="60%" height="70" valign="middle" style="padding-bottom:20px;">
										  <div class="contentEditableContainer contentTextEditable">
													<div class="contentEditable" align='left' >
																	<span style="font-size:11px;color:#555;font-family:Helvetica, Arial, sans-serif;line-height:200%;"><hr><span style='color:#ff0000'>This link is valid only for 24 hours.</span>
																	<br/>If the above link is un-clickable, then copy-paste the following in your browser:
																	<br/> {{ link }}</span>
																	<br/>
														<span style="font-size:13px;color:#181818;font-family:Helvetica, Arial, sans-serif;line-height:200%;">Sent to {{ email }} by pyofey.pythonanywhere@gmail.com</span>
											  <br/>
											  <span style="font-size:11px;color:#555;font-family:Helvetica, Arial, sans-serif;line-height:200%;"></span>
											  <br/>
											  <span style="font-size:13px;color:#181818;font-family:Helvetica, Arial, sans-serif;line-height:200%;">
											  <a target='_blank' href="[FORWARD]" style="text-decoration:none;color:#555"></a>
											  </span>
											  <br/>
											  <span style="font-size:13px;color:#181818;font-family:Helvetica, Arial, sans-serif;line-height:200%;">
											  <a target='_blank' href="[UNSUBSCRIBE]" style="text-decoration:none;color:#555">click here to unsubscribe</a></span>
													</div>
												  </div>
										</td>
										<td width="40%" height="70" align="right" valign="top" align='right' style="padding-bottom:20px;">
										  <table width="100%" border="0" cellspacing="0" cellpadding="0" align='right'>
											<tr>
											  <td width='57%'></td>
											  <td valign="top" width='34'>

											  </td>
											  <td valign="top" width='34'>

											  </td>
											  <td valign="top" width='34'>

											  </td>
											</tr>
										  </table>
										</td>
									  </tr>
									</table>
								  </div>
								</td>
							  </tr>
							</table>
						  </td></tr></table>

							</td>
						  </tr>
						  </table>

						</body>
						</html>
			'''

def page(request):
	global html_email
	if request.POST:
		form = Form_inscription(request.POST)
		if form.is_valid():
			name     = form.cleaned_data['name']
			email    = form.cleaned_data['email']
			password = form.cleaned_data['password']

			string1        = str(random.random()).encode('utf-8')
			salt           = hashlib.sha1(string1).hexdigest()[:5]
			string2        = str(salt+email).encode('utf-8')
			activation_key = hashlib.sha1(string2).hexdigest()
			key_expires    = datetime.datetime.today() + datetime.timedelta(1)

			link = 'http://192.168.1.2:8000/accounts/confirm/' + str(activation_key)

		# User auth details:-
			admin_users = User.objects.all()
			for i in admin_users:
				if name == i.first_name:
					return render(request, 'create_user.html', {'user_exists':True})
				if email == i.email:
					return render(request, 'create_user.html', {'email_exists':True})

			try:
				new_user  = User.objects.create_user(username = name, password = password)
				try:
					htmly                   = Template(html_email)
					d                       = Context({'name': name, 'link':link, 'email':email})
					subject, from_email, to = 'Email confirmation - pyofeyblogs.pythonanywhere.com', 'pyofey.pythonanywhere@gmail.com', email
					html_content            = htmly.render(d)
					msg                     = EmailMultiAlternatives(subject, '', from_email, [to])
					msg.attach_alternative(html_content, "text/html")
					msg.send()
				except:
					user_del = User.objects.filter(username=name)
					task     = user_del.get()
					task.delete()
					return render(request, 'create_user.html', {'email_exists':True})
			except:
				return render(request, 'create_user.html', {'user_exists':True})

			new_user.is_active  = False
			new_user.first_name = name
			new_user.email      = email
			new_user.save()
			new_user            = UserProfile(user_auth = new_user, name = name, email=email, password = password, activation_key=activation_key, key_expires=key_expires)
			new_user.save()
			return render(request, 'create_user.html', {'user_added':True})
		else:
			return render(request, 'create_user.html', {'form' : form})
	else:
		form = Form_inscription()
		return render(request, 'create_user.html', {'form' : form})

class Form_inscription(forms.Form):
	name         = forms.CharField(label="User Name", max_length=30, help_text="Username must be unique")
	email        = forms.EmailField(label="Email")
	password     = forms.CharField(label="Password", widget = forms.PasswordInput)
	password_bis = forms.CharField(label="Re-enter Password", widget = forms.PasswordInput)
	def clean(self):
		cleaned_data = super(Form_inscription, self).clean()
		password     = self.cleaned_data.get('password')
		password_bis = self.cleaned_data.get('password_bis')

		if type(password) != 'str':
			raise forms.ValidationError("")
		if len(password) < 10:
			raise forms.ValidationError("Passowrd Is Too Short! Atleast 10 Characters")
		if password and password_bis and password != password_bis:
			raise forms.ValidationError("Passwords are not identical.")
		if password.isalpha() or password.isdigit():
			raise forms.ValidationError("Passowrd MUST be Alphanumeric with Special charaters!")
		if password.isalnum():
			raise forms.ValidationError("Passowrd MUST be Alphanumeric with Special charaters!")
		
		name = self.cleaned_data.get('name')
		return self.cleaned_data

def py_mail(SUBJECT, BODY, TO, FROM):
	MESSAGE = MIMEMultipart('alternative')
	MESSAGE['subject'] = SUBJECT
	MESSAGE['To'] = TO
	MESSAGE['From'] = FROM
	MESSAGE.preamble = """Your mail reader does not support the report format."""

	HTML_BODY = MIMEText(BODY, 'html')
	MESSAGE.attach(HTML_BODY)
	server = smtplib.SMTP('smtp.gmail.com:587')
	password = "Bluepavi1!"
	server.starttls()
	server.login(FROM,password)
	server.sendmail(FROM, [TO], MESSAGE.as_string())
	server.quit()