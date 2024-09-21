#https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps

'''
To send mail 
    enable in gmail the 2 step verification 
Then 
    use below link to create app password
    with app password and your mail id try to run the below code

    #https://support.google.com/accounts/answer/185833?hl=en
'''

import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'shreyasmooli007@gmail.com'
email_passwd = 'xxev xqyy lbai onut'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='mtd.nithin@gmail.com', msg="NAME: Shreyas Moolya, TEAMMATE NAME: Sanjay Puttaswamy, TEAM NO: 8(T8), CASE STUDY NO: 4, GITHUB REPO:https://github.com/shreyasmoolya007/python_training_sep2024")
connection.close()
print('Mail sent successfully')