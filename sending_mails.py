import smtplib
from details import my_mail,my_pass

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()

s.login('yourmail','yours password')
msg='Hello World How are you all....!'

reciever_mail=['gopianandakumar@gmail.com']
s.sendmail(my_mail,reciever_mail,msg)
s.quit()

print('SuccessFully Send....!')
