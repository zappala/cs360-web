from flask import render_template

from config import app
from schedule import *

@app.route('/fall-2015/schedule')
def fall2015schedule():
    static = '/static/lectures/winter-2014/'
    new = '/static/lectures/fall-2015/'
    term = '/fall-2015/'
    s = Schedule()

    s.week()

    d = s.day("August 31/September 1")
    d.lecture('Introduction','The Internet and its Architecture')
    d.reading('The Internet and its Architecture',static + 'the-internet-and-its-architecture.pdf')
    d.reading('Neal Stephenson on laying undersea fiber-optic cables','http://www.wired.com/wired/archive/4.12/ffglass.html')

    d = s.day("September 2/3")
    d.lecture('Systems','Socket Programming')
    d.reading('Socket Programming',static + 'socket-programming.pdf')
    d.assignment('Homework: Linux Command Line',term + 'homework/linux-command-line')

    s.week()

    d = s.day("September 8")
    d.lecture('Systems','Socket Programming, DNS')
    d.reading('DNS',static+'dns.pdf')

    d = s.day("September 9/10")
    d.lecture('Systems','Sockets and the OS')
    d.reading('Sockets and the OS',static + 'sockets-and-the-os.pdf')
    d.tutorial('Homework: Make',term + 'homework/make')
    d.tutorial('Homework: Git',term + 'homework/git')

    s.week()

    d = s.day("September 14/15")
    d.lecture('Concurrent Programming','Threads and the OS')
    d.reading('Threads and the OS',static+'threads-and-the-os.pdf')
    d.reading('Pthreads Tutorial','http://www.llnl.gov/computing/tutorials/pthreads/')
    d.assignment('Homework: Socket I/O (Due 15/16)',term + 'homework/socket-io')

    d.lecture('Systems','Thread Pool Architecture, Lab Discussion')
    d.reading('Thread Pool Architecture',static+'thread-pool-architecture.pdf')


    d = s.day("September 16/17")
    d.lecture('Concurrent Programming','Thread Synchronization')
    d.reading('Thread Synchronization',static+'thread-synchronization.pdf')
    d.reading('Mutexes, Condition Variables, and Monitors',static+'mutexes-condition-variables-and-monitors.pdf')

    s.week()

    d = s.day("September 21")
    d.assignment('Lab: Messaging Service',term + 'labs/messaging-service')

    d = s.day('September 21/22')
    d.lecture('Concurrent Programming','Mutexes, Condition Variables, and Monitors')
    d.reading('Mutexes, Condition Variables, and Monitors',static+'mutexes-condition-variables-and-monitors.pdf')
    d.assignment('Homework: Threading',term + 'homework/threading')

    d = s.day('September 23/24')
    d.lecture('Concurrent Programming','Semaphores')
    d.reading('Semaphores',static+'semaphores.pdf')
    d.assignment('Homework: Mutexes and Condition Variables',term + 'homework/mutexes-and-condition-variables')


    s.week()

    d = s.day('September 28/29')
    d.lecture('Concurrent Programming','Semaphores')
    d.assignment('Homework: Semaphores',term + 'homework/semaphores')

    d = s.day('September 30/October 1')
    d.lecture('Concurrent Programming and Systems','Deadlock and UNIX Domain Sockets')
    d.reading('Deadlock',static+'deadlock.pdf')
    d.reading('UNIX Domain Sockets',static+'unix-domain-sockets.pdf')
    d.assignment('Homework: Mutual Exclusion',term + 'homework/mutual-exclusion')

    d = s.day('October 2')
    d.assignment('Lab: Threaded Messaging Service',term + 'labs/threaded-messaging-service')
        
    s.week()

    d = s.day('October 5/6')
    d.lecture('Systems','Introduction to Python Programming')
    d.reading('Introduction to Python',static+'introduction-to-python.pdf')
    d.reading('Python at Codecademy','http://www.codecademy.com/tracks/python')
    d.reading('Python Documentation','http://www.python.org/')
    d.reading('Dive Into Python','http://www.diveinto.org/python3/')
  
    d = s.day('October 7/8')
    d.lecture('Systems','Python Networking and Threading, Lab Discussion')
    d.reading('Python Networking and Threading',static+'python-networking-and-threading.pdf')
    d.assignment('Homework: Python')

    s.week()
    
    d = s.day('October 12/13')
    d.lecture('Systems','HTTP')
    d.reading('HTTP',static+'http.pdf')
    d.assignment('Homework: Python Threading')

   
    d = s.day('October 14/15')
    d.lecture('Systems','Web Proxies, Caching, and CDNs')
    d.reading('Web Proxies, Caching, and CDNs',static+'web-proxies-caching-and-cdns.pdf')
    d.reading("O'Reilly Web Caching Chapter",'http://www.oreilly.com/catalog/webcaching/chapter/ch05.html')
    d.assignment('Homework: Python Requests Library')

    d = s.day('October 16')
    d.assignment('Lab: Download Accelerator',term + 'labs/download-accelerator')

    s.week()

    d = s.day('October 19/20')
    d.lecture('Concurrent Programming','Python Socket Programming, Event Driven Architecture')
    d.reading('Python Socket Programming',static+'python-socket-programming.pdf')
    d.reading('Event-Driven Architecture',static+'event-driven-architecture.pdf')
    d.reading('Why Threads Are A Bad Idea (for most purposes)','http://chess.cs.umd.edu/class/spring2009/cmsc433/Lectures/threadVsEvents.pdf')
    d.assignment('Homework: CrowdSourced Measurements')

    d = s.day('October 21/22')
    d.lecture('Performance Measurement','Performance Evaluation')
    d.assignment('Homework: Event-Driven Programming')

    d = s.day('October 19-22')
    d.assignment('Exam in Testing Center | Weeks 1 - 7','')

    s.week()

    d = s.day('October 26/27')
    d.lecture('Security','Network Security')
    d.reading('Network Security',new+'network-security.pdf')

    d = s.day('October 28/29')
    d.lecture('Security','Network Security')
    d.assignment('Homework: Network Security',term + 'homework/network-security')

    d = s.day('October 30')
    d.assignment('Lab: Web Server',term + 'labs/web-server')


    s.week()

    d = s.day('November 2/3')
    d.lecture('Web Programming','Web Design and CSS')
    d.reading('Web Design',static+'web-design.pdf')
    d.reading('HTML and CSS Tutorial','http://www.codecademy.com/tracks/web')
    d.reading('CSS Tutorial','http://www.htmldog.com/guides/css/')
    d.reading('Learn CSS Layout','http://learnlayout.com/')
    d.reading('Design Process in the Responsive Age','http://uxdesign.smashingmagazine.com/2012/05/30/design-process-responsive-age/')
    d.reading('Twitter Bootstrap','http://getbootstrap.com/')
    d.reading('Foundation','http://foundation.zurb.com/')
    d.assignment('Homework: Web Application Proposals',term + 'homework/web-application-proposals')
    
    d = s.day('November 4/5')
    d.lecture('Web Programming','Javascript')
    d.reading('Javascript at Codecademy','http://www.codecademy.com/tracks/javascript?jump_to=4fa836e5996b00000302064a')
    d.reading('JQuery at Codecademy','http://www.codecademy.com/tracks/jquery')
    d.assignment('Homework: Javascript')
    
    s.week()

    d = s.day('November 9/10')
    d.lecture('Web Programming','React')
    d.assignment('Homework: React')

    d = s.day('November 11/12')
    d.lecture('Web Programming','React')
    d.assignment('Homework: React')
    d.assignment('Homework: Web Application Idea and Features',term+'/homework/web-application-idea-and-features')

    s.week()

    d = s.day('November 16/17')
    d.lecture('Web Programming','Node/Express/Sequelize')
    d.reading('Designing Relational Database Models',static+'designing-relational-database-models.pdf')

    d = s.day('November 18/19')
    d.lecture('Web Programming','Node/Express/Sequelize')
    
    d = s.day('November 20')
    d.assignment('Homework: Web Application Front End')
    
    s.week()

    d = s.day('November 23/24')
    d.lecture('Web Programming: Group Meetings')

    s.week()

    d = s.day('November 30/December 1')
    d.lecture('Web Programming','User Registration and Token-Based Authentication')

    d = s.day('December 2/3')
    d.lecture('Web Programming','NoSQL Databases and Mongoose')
    d.reading('Designing Document Database Models',static+'designing-document-database-models.pdf')
    d.reading('Starbucks Does Not Use Two-Phase Commit','http://eaipatterns.com/ramblings/18_starbucks.html')
    d.assignment('Homework: Mongoose')

    d = s.day('December 4')
    d.assignment('Homework: Web Application Back End')

    s.week()

    d = s.day('December 7/8')
    d.lecture('Security','Web Vulnerabilities')
    d.reading('Web Vulnerabilities',static+'web-vulnerabilities.pdf')


    d = s.day('December 9/10')
    d.lecture('Web Programming','Users and Authentication')
    d.reading('Users and Authentication',static+'users-and-authentication.pdf')
    d.reading('Research on passwords by Cormac Herley','http://research.microsoft.com/en-us/people/cormac/')
    d.reading('The Quest to Replace Passwords: A Framework for Comparative Evaluation of Web Authentication Schemes','http://research.microsoft.com/apps/pubs/?id=161585')
    d.reading('Does My Password Go up to Eleven? The Impact of Password Meters on Password Selection','http://research.microsoft.com/apps/pubs/?id=192108')

    d = s.day('December 10')
    d.assignment('Lab: Web Application',term+'/labs/web-application')

    s.week()

    d = s.day('Section 1: December 17, 7:00 am')
    d.assignment('Final Exam, B106 JFSB','')

    d = s.day('Section 2: December 17, 11:00 am')
    d.assignment('Final Exam, B094 JFSB','')


    return render_template('fall-2015/schedule.html',active='schedule',
                           weeks=s.weeks)
