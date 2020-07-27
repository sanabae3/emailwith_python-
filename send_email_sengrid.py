import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Set environment variables
os.environ['SENDGRID_API_KEY'] = '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'
#setting file path
filepath = 'email.txt'
notsent = []

#opening fille and extracting feilds 
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        content = line.strip()
        content_splited=content.split(',')
        to_email=content_splited[0]
        to_name=content_splited[1]
        to_fee=content_splited[2]
	#formating Emails
        message = Mail(
        from_email='contact@usapropheticconvention.com',
        to_emails=to_email,
        subject='USA Prophetic Convention 2020 Refund',
        html_content='<p>Hello '  +to_name+',</p><p>Thank you for requesting a refund to your <strong>USA Prophetic Convention 2020</strong> registration. Your refund of  $'+to_fee+'  was successfully processed, and will reflect in a couple of days in the same debit or credit card used when registering.</p><p>As in prior years, the event will be livestreamed on our YouTube channel and Facebook page.<br>https://youtube.com/cmfimd<br>https://facebook.com/cmfimaryland</p><p>Feel free to reply if you have any question.</p><p>Blessings,</p><p>The USA Prophetic Convention Committee</p>')
        try:
	    # sending the email using the foramted message and API key
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
        except Exception as e:
	    #exception to handle cases of bad emails
            print(e , to_email)
            notsent.append(to_email)
            pass
        finally:
            line = fp.readline()

print(notsent)           
