# Importing libraries 
import imaplib, email,datetime
import time
 

user = 'aditya@novelvista.com'
password = 'novel@vista'
imap_url = 'imap.gmail.com'

# Function to get email content part i.e its body part 
def get_body(msg):
	if msg.is_multipart(): 
		return get_body(msg.get_payload(0)) 
	else: 
		return msg.get_payload(None, True) 

# Function to search for a key value pair 
def search(key, value, con): 
	#date = (datetime.date.today() - datetime.timedelta(5)).strftime("%d-%b-%Y") 
	result, data = con.search(None,'(FROM {0})'.format(value.strip())) 
	return data 

# Function to get the list of emails under this label 
def get_emails(result_bytes): 
	msgs = [] # all the email data are pushed inside an array 
	for num in result_bytes[0].split(): 
		typ, data = con.fetch(num, '(RFC822)') 
        
		msgs.append(data) 

	return msgs 

# this is done to make SSL connnection with GMAIL 
con = imaplib.IMAP4_SSL(imap_url) 


# logging the user in 
con.login(user, password) 

# calling function to check for email under this label 
con.select('Inbox') 

# fetching emails from this user "tu**h*****1@gmail.com" 
msgs = get_emails(search('FROM', 'no-reply@sns.amazonaws.com', con))
#msgs = get_emails(search('FROM', 'rathi.aditya@gmail.com', con)) 

# Uncomment this to see what actually comes as data 
# print(msgs) 


# Finding the required content from our msgs 
# User can make custom changes in this part to 
# fetch the required content he / she needs 

# printing them by the order they are displayed in your gmail 
i = 0
for msg in msgs[::-1]:
	
	for sent in msg: 
		 
		i += 1
		f = open(f"D:\\bounce1\\email_notification_{i}.txt","w+")
		if type(sent) is tuple: 

			# encoding set as utf-8 
			content = str(sent[1], 'utf-8') 
			data = str(content) 

			# Handling errors related to unicodenecode 
			try: 
				indexstart = data.find("ltr") 
				data2 = data[indexstart + 5: len(data)] 
				indexend = data2.find("</div>") 

				# printtng the required content which we need 
				# to extract from our email i.e our body 
				email_object = email.message_from_string(data)
				if (email_object.is_multipart): 
					f.write(str(email_object.get_payload(i=None, decode=False)))  
					
				else: 
					f.write(str(email_object.get_payload(i=None,decode=False))) 

				f.close()  	

			except UnicodeEncodeError as e: 
				pass

		