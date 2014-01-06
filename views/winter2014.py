from flask import render_template

from config import app
from schedule import *

@app.route('/winter-2014/schedule')
def schedule():
    static = '/static/lectures/winter-2014/'
    term = '/winter-2014/'
    s = Schedule()

    s.week()

    d = s.day("January 6")
    d.lecture('Introduction','The Internet and its Architecture')
    d.reading('The Internet and its Architecture',static + 'the-internet-and-its-architecture.pdf')
    d.reading('Neal Stephenson on laying undersea fiber-optic cables','http://www.wired.com/wired/archive/4.12/ffglass.html')

    d = s.day("January 8")
    d.lecture('Introduction','The Internet and its Architecture, Lab Discussion')

    d = s.day("January 10")
    d.lecture('Systems','Socket Programming')
    d.reading('Socket Programming',static + 'socket-programming.pdf')

    s.week()

    d = s.day("January 13")
    d.lecture('Systems','Sockets and the OS')
    d.reading('Sockets and the OS',static + 'sockets-and-the-os.pdf')

    d = s.day("January 15")
    d.lecture('Concurrent Programming','Threads and the OS')
    d.reading('Threads and the OS',static+'threads-and-the-os.pdf')
    d.reading('Pthreads Tutorial','http://www.llnl.gov/computing/tutorials/pthreads/')

    d = s.day("January 17")
    d.lecture('Systems','Thread Pool Architecture, Lab Discussion')
    d.reading('Thread Pool Architecture',static+'thread-pool-architecture.pdf')

    d = s.day("January 18")
    d.assignment('Lab: Messaging Service',term + 'labs/messaging-service')

    s.week()

    d = s.day("January 20")
    d.lecture('No Class','Martin Luthor King Jr. Holiday')

    d = s.day("January 22")
    d.lecture('Concurrent Programming','Thread Synchronization')
    d.reading('Thread Synchronization',static+'thread-synchronization.pdf')

    d = s.day('January 24')
    d.lecture('Concurrent Programming','Semaphores')
    d.reading('Semaphores',static+'semaphores.pdf')

    s.week()

    d = s.day('January 27')
    d.lecture('Concurrent Programming','Mutexes and Monitors')
    d.reading('Mutexes and Monitors',static+'mutexes-and-monitors.pdf')

    d = s.day('January 29')
    d.lecture('Concurrent Programming and Systems','Deadlock and UNIX Domain Sockets')
    d.reading('Deadlock',static+'deadlock.pdf')
    d.reading('UNIX Domain Sockets',static+'unix-domain-sockets.pdf')

    d = s.day('January 31')
    d.lecture('Concurrent Programming','Help With Lab 2')

    d = s.day('February 1')
    d.assignment('Lab: Threaded Messaging Service',term + 'labs/threaded-messaging-service')

    s.week()

    d = s.day('February 3')
    d.lecture('Systems','Introduction to Python Programming')
    d.reading('Introduction to Python',static+'introduction-to-python.pdf')
    d.reading('Python at Codecademy','http://www.codecademy.com/tracks/python')
    d.reading('Python Documentation','http://www.python.org/')
    d.reading('Dive Into Python','http://www.diveinto.org/python3/')

    d = s.day('February 5')
    d.assignment('Exam | Weeks 1 - 4','')

    d = s.day('February 7')
    d.lecture('Systems','Python Networking and Threading, Lab Discussion')
    d.reading('Python Networking and Threading',static+'python-networking-and-threading.pdf')
    s.week()

    d = s.day('February 10')
    d.lecture('Systems','HTTP')
    d.reading('HTTP',static+'http.pdf')
  
    d = s.day('February 12')
    d.lecture('Systems','DNS')
    d.reading('DNS',static+'dns.pdf')

    d = s.day('February 14')

    s.week()

    d = s.day('February 17')
    d.lecture('No Class','Presidents Day Holiday')

    d = s.day('February 18')
    d.assignment('Lab: Download Accelerator',term + 'labs/download-accelerator')

    d = s.day('February 19')
    d.lecture('Concurrent Programming','Python Socket Programming, Lab Discussion')
    d.reading('Python Socket Programming',static+'python-socket-programming.pdf')

    d = s.day('February 21')
    d.lecture('Systems','Event Driven Architecture, Lab Discussion')
    d.reading('Event-Driven Architecture',static+'event-driven-architecture.pdf')

    s.week()

    d = s.day('February 24')
    d.lecture('Systems','Web Proxies, Caching, and CDNs')
    d.reading('Web Proxies, Caching, and CDNs',static+'web-proxies-caching-and-cdns.pdf')
    d.reading("O'Reilly Web Caching Chapter",'http://www.oreilly.com/catalog/webcaching/chapter/ch05.html')


    d = s.day('February 26')
    d.lecture('Security','Network Security')
    d.reading('Network Security',static+'network-security.pdf')


    d = s.day('February 28')
    d.lecture('Security','Network Security')

    d = s.day('March 1')
    d.assignment('Lab: Web Server',term + 'labs/web-server')

    s.week()

    d = s.day('March 3')
    d.lecture('Performance Measurement','Queueing Theory')
    d.reading('Queueing Theory',static+'queueing-theory.pdf')

    d = s.day('March 5')
    d.lecture('Performance Measurement','Lab Discussion')

    d = s.day('March 7')
    d.lecture('Performance Measurement','Performance Measurement and Workload Models')
    d.reading('Performance Measurement',static+'performance-measurement.pdf')
    d.assignment('Web Application Proposals','https://drive.google.com/folderview?id=0B09H8qp1t9fAdzgwaTg1aERpems&usp=sharing')

    s.week()

    d = s.day('March 10')
    d.lecture('Security','Network Security')

    d = s.day('March 12')
    d.lecture('Web Programming','Team Formation and Agile Development')

    d = s.day('March 13')
    d.assignment('Lab: Queueing Theory',term + '/labs/queueing-theory')

    d = s.day('March 14')
    d.lecture('Web Programming','Introduction to Web Frameworks and MVC')
    d.reading('Web Frameworks and MVC',static+'web-frameworks-and-mvc.pdf')

    s.week()

    d = s.day('March 17')
    d.assignment('Exam | Weeks 5 - 10','')

    d = s.day('March 19')
    d.lecture('Web Programming','Web Design')
    d.reading('Web Design',static+'web-design.pdf')

    d = s.day('March 21')
    d.lecture('Web Programming','Designing Relational Database Models')
    d.reading('Designing Relational Database Models',static+'designing-relational-database-models.pdf')

    s.week()

    d = s.day('March 24')
    d.lecture('Web Programming','Designing Document Database Models')
    d.reading('Designing Document Database Models',static+'designing-document-database-models.pdf')
    d.reading('Starbucks Does Not Use Two-Phase Commit','http://eaipatterns.com/ramblings/18_starbucks.html')
    d.assignment('Web Application Idea, Features, and Architecture',term+'/labs/web-application')

    d = s.day('March 26')
    d.lecture('Web Programming','Users and Authentication')
    d.reading('Users and Authentication',static+'users-and-authentication.pdf')

    d = s.day('March 28')
    d.lecture('Web Programming','CSS')
    d.reading('HTML and CSS Tutorial','http://www.codecademy.com/tracks/web')
    d.reading('CSS Tutorial','http://www.htmldog.com/guides/css/')
    d.reading('Test HTML',static+'css/test.html')
    d.reading('Test CSS',static+'css/style.css')
    d.reading('Learn CSS Layout','http://learnlayout.com/')
    d.reading('SASS','http://alistapart.com/article/why-sass')
    d.reading('Design Process in the Responsive Age','http://uxdesign.smashingmagazine.com/2012/05/30/design-process-responsive-age/')
    d.reading('Twitter Bootstrap','http://getbootstrap.com/')
    d.reading('Responsive Grid System','http://www.responsivegridsystem.com/')

    s.week()

    d = s.day('March 31')
    d.lecture('Web Programming','Javascript')
    d.reading('Javascript',static+'javascript.pdf')
    d.reading('Javascript at Codecademy','http://www.codecademy.com/tracks/javascript?jump_to=4fa836e5996b00000302064a')
    d.reading('JQuery at Codecademy','http://www.codecademy.com/tracks/jquery')
    d.assignment('Web Application Layout',term+'/labs/web-application')

    d = s.day('April 2')
    d.lecture('Web Programming','Group Meetings')

    d = s.day('April 4')

    s.week()

    d = s.day('April 7')
    d.lecture('Web Programming','Web Services')
    d.reading('Web Services',static+'web-services.pdf')
    d.reading('Interactive REST Tutorial','http://phprestsql.sourceforge.net/')

    d = s.day('April 9')
    d.lecture('Web Programming','Web Services')


    d = s.day('April 11')
    d.lecture('Security','Web Vulnerabilities')
    d.assignment('Web Application Milestone',term+'/labs/web-application')
    d.reading('Web Vulnerabilities',static+'web-vulnerabilities.pdf')

    s.week()

    d = s.day('April 14')
    d.assignment('Exam | Weeks 11 - 15','')

    s.week()

    d = s.day('April 23')
    d.assignment('Lab: Web Application',term+'/labs/web-application')

    return render_template('winter-2014/schedule.html',active='schedule',
                           weeks=s.weeks)
