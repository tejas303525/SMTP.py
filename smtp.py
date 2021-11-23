#Turn off less secure from your google account by going to manage your account >> security >> scroll to less secure #





from smtplib import SMTP
import getpass

server = SMTP('smtp.gmail.com',587)
server.starttls() #not req if we use ssl
server.ehlo()     # to describe info 

server.login("123015109@sastra.ac.in" ,getpass.getpass("enter password: "))



server.sendmail(from_addr='Type in the from addr',to_addrs='type in the to addr',msg="hello foo!")
print("Email sent")
server.quit()
