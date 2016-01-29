
# coding: utf-8

# In[117]:

import urllib2
import subprocess

address='http://france.usembassy.gov/non-immigrant_visas.html'


print "Open address ", address
response1=urllib2.urlopen(address)
page=response1.read()
page1=page.split('\n')
#print 'Pending Visas' in page1

i=0
for c in page1:
    #print c.find('Pending Visas')
    if 'vpending.pdf' in c:
        #print i
        found=i
    i+=1
        


link = page1[found].split('\"')[1]
print "found a link: ", link



file_name = link.split('/')[-1].strip()
print "Downloading to file: ", file_name
u = urllib2.urlopen(link)
f = open(file_name, 'wb')
f.write(u.read())
#print subprocess.check_output(['bash','-c', 'ls'])
f.close()
#pdf = response.read()
bashCommand="pdf2txt.py vpending.pdf"
output = subprocess.check_output(['bash','-c', bashCommand])

lines=output.split('\n\n')

import numpy as np
lines=np.array(lines)
lines1=[]
found1, found2=[],[]

index=0
for c in lines:
    c=c.replace('\x0c','')
    index+=1
    lines1.append(c)
    if '2016014 286 1' in c:
        found1=index
    if '2016022 378 1' in c:
        found2=index
        
print 'Mr. Danilov 2016014 286 1: ', 
if found1:
    print lines[found1], ' [', found1,'] line'
else:
    print 'not found'
    
print 'Mr. Aristov 2016022 378 1: ', 
if found2:
    print lines[found2], ' [', found2,'] line'
else:
    print 'not found'
    
    

#print (lines[lines 2016014 286 1'])


# In[121]:

# Import smtplib for the actual sending function
#import smtplib

# Import the email modules we'll need
#from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open(textfile, 'rb')
# Create a text/plain message
#msg = MIMEText("test")
#fp.close()

#me ="andrey.aristov@gmail.com"
#you = "andrey.aristov@gmail.com"
#msg['Subject'] = 'Test' #% textfile
#msg['From'] = me
#msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
#s = smtplib.SMTP('localhost')
#s.sendmail(me, [you], msg.as_string())
#s.quit()


# In[ ]:



