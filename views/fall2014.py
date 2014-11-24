from flask import render_template

from config import app
from schedule import *

@app.route('/fall-2014/schedule')
def fall2014schedule():
    static = '/static/lectures/winter-2014/'
    term = '/fall-2014/'
    s = Schedule()

    s.week()

    d = s.day("September 3")
    d.lecture('Introduction','The Internet and its Architecture')
    d.reading('The Internet and its Architecture',static + 'the-internet-and-its-architecture.pdf')
    d.reading('Neal Stephenson on laying undersea fiber-optic cables','http://www.wired.com/wired/archive/4.12/ffglass.html')
    d.tutorial('Tutorial: Linux Command Line',term + 'tutorials/linux-command-line')

    d = s.day("September 5")
    d.lecture('Introduction','The Internet and its Architecture, Lab Discussion')

    s.week()

    d = s.day("September 8")
    d.lecture('Systems','Socket Programming')
    d.reading('Socket Programming',static + 'socket-programming.pdf')
    d.tutorial('Tutorial: Make',term + 'tutorials/make')

    d = s.day("September 10")
    d.lecture('Systems','Sockets and the OS')
    d.reading('Sockets and the OS',static + 'sockets-and-the-os.pdf')
    d.tutorial('Tutorial: Git',term + 'tutorials/git')

    d = s.day("September 12")
    d.lecture('Concurrent Programming','Threads and the OS')
    d.reading('Threads and the OS',static+'threads-and-the-os.pdf')
    d.reading('Pthreads Tutorial','http://www.llnl.gov/computing/tutorials/pthreads/')

    s.week()

    d = s.day("September 15")
    d.lecture('Systems','Thread Pool Architecture, Lab Discussion')
    d.reading('Thread Pool Architecture',static+'thread-pool-architecture.pdf')


    d = s.day("September 17")
    d.lecture('Concurrent Programming','Thread Synchronization')
    d.reading('Thread Synchronization',static+'thread-synchronization.pdf')

    d = s.day('September 19')
    d.lecture('Concurrent Programming','Semaphores')
    d.reading('Semaphores',static+'semaphores.pdf')
    d.assignment('Lab: Messaging Service',term + 'labs/messaging-service')

    s.week()

    d = s.day('September 22')
    d.lecture('Concurrent Programming','Mutexes and Monitors')
    d.reading('Mutexes and Monitors',static+'mutexes-and-monitors.pdf')

    d = s.day('September 24')
    d.lecture('Concurrent Programming and Systems','Deadlock and UNIX Domain Sockets')
    d.reading('Deadlock',static+'deadlock.pdf')
    d.reading('UNIX Domain Sockets',static+'unix-domain-sockets.pdf')

    d = s.day('September 26')
    d.lecture('Concurrent Programming','Help With Lab 2')

    d = s.day('September 27')
    d.assignment('Lab: Threaded Messaging Service',term + 'labs/threaded-messaging-service')

    s.week()

    d = s.day('September 29')
    d.lecture('Systems','Introduction to Python Programming')
    d.reading('Introduction to Python',static+'introduction-to-python.pdf')
    d.reading('Python at Codecademy','http://www.codecademy.com/tracks/python')
    d.reading('Python Documentation','http://www.python.org/')
    d.reading('Dive Into Python','http://www.diveinto.org/python3/')

    d = s.day('October 1')
    d.assignment('Exam | Weeks 1 - 4','')

    d = s.day('October 3')
    d.lecture('Systems','Python Networking and Threading, Lab Discussion')
    d.reading('Python Networking and Threading',static+'python-networking-and-threading.pdf')
    s.week()

    d = s.day('October 6')
    d.lecture('Systems','HTTP')
    d.reading('HTTP',static+'http.pdf')
  
    d = s.day('October 8')
    d.lecture('Systems','DNS')
    d.reading('DNS',static+'dns.pdf')

    d = s.day('October 10')

    s.week()

    d = s.day('October 13')
    d.lecture('Concurrent Programming','Python Socket Programming, Lab Discussion')
    d.reading('Python Socket Programming',static+'python-socket-programming.pdf')
    d.assignment('Lab: Download Accelerator',term + 'labs/download-accelerator')

    d = s.day('October 15')
    d.lecture('Systems','Event Driven Architecture, Lab Discussion')
    d.reading('Event-Driven Architecture',static+'event-driven-architecture.pdf')
    d.reading('Why Threads Are A Bad Idea (for most purposes)','http://chess.cs.umd.edu/class/spring2009/cmsc433/Lectures/threadVsEvents.pdf')

    d = s.day('October 17')
    d.lecture('Systems','Web Proxies, Caching, and CDNs')
    d.reading('Web Proxies, Caching, and CDNs',static+'web-proxies-caching-and-cdns.pdf')
    d.reading("O'Reilly Web Caching Chapter",'http://www.oreilly.com/catalog/webcaching/chapter/ch05.html')

    s.week()

    d = s.day('October 20')
    d.lecture('Security','Network Security')
    d.reading('Network Security',static+'network-security.pdf')

    d = s.day('October 22')
    d.lecture('Security','Network Security')


    d = s.day('October 24')
    d.lecture('Security','Network Security')

    d = s.day('October 25')
    d.assignment('Lab: Web Server',term + 'labs/web-server')

    s.week()

    d = s.day('October 27')
    d.lecture('Performance Measurement','Queueing Theory')
    d.reading('Queueing Theory',static+'queueing-theory.pdf')

    d = s.day('October 29')
    d.lecture('Performance Measurement','Queueing Theory Practice')

    d = s.day('October 31')
    d.lecture('Performance Measurement','Lab Discussion')

    s.week()

    d = s.day('November 3')
    d.lecture('Performance Measurement','Performance Measurement and Workload Models')
    d.reading('Performance Measurement',static+'performance-measurement.pdf')

    d = s.day('November 5')
    d.assignment('Exam | Weeks 5 - 8','')

    d = s.day('November 7')
    d.lecture('No Class')

    d = s.day('November 8')
    d.assignment('Lab: Queueing Theory',term + '/labs/queueing-theory')

    s.week()

    d = s.day('November 10')
    d.lecture('Web Programming','Team Formation and Agile Development')
    d.assignment('Web Application: Proposals','https://docs.google.com/document/d/1_nfHF3iQEdm4diifVBGUQ3OGI1peHRopp-nK3pb0x3Q/edit?usp=sharing')

    d = s.day('November 12')
    d.lecture('Web Programming','Web Design and CSS')
    d.reading('Web Design',static+'web-design.pdf')
    d.reading('HTML and CSS Tutorial','http://www.codecademy.com/tracks/web')
    d.reading('CSS Tutorial','http://www.htmldog.com/guides/css/')
    d.reading('Learn CSS Layout','http://learnlayout.com/')
    d.reading('Design Process in the Responsive Age','http://uxdesign.smashingmagazine.com/2012/05/30/design-process-responsive-age/')
    d.reading('Twitter Bootstrap','http://getbootstrap.com/')
    d.reading('Foundation','http://foundation.zurb.com/')


    d = s.day('November 14')
    d.lecture('Web Programming','Introduction to Web Frameworks and MVC')
    d.reading('Web Frameworks and MVC',static+'web-frameworks-and-mvc.pdf')
    d.assignment('Web Application: Idea and Features',term+'/labs/web-application')
    s.week()

    d = s.day('November 17')
    d.lecture('Web Programming','Databases')
    d.reading('Designing Relational Database Models',static+'designing-relational-database-models.pdf')
    d.reading('Designing Document Database Models',static+'designing-document-database-models.pdf')
    d.reading('Starbucks Does Not Use Two-Phase Commit','http://eaipatterns.com/ramblings/18_starbucks.html')

    d = s.day('November 19')
    d.lecture('Web Programming','node.js')

    d = s.day('November 21')
    d.lecture('Web Programming','Angular.js')
    d.reading('AngularJS in 20ish Minutes','https://www.youtube.com/watch?v=tnXO-i7944M')
    d.reading('10 Reasons Why You Should Use AngularJS','http://www.sitepoint.com/10-reasons-use-angularjs/')
    d.reading('Why Does Angular.js Rock?','http://angular-tips.com/blog/2013/08/why-does-angular-dot-js-rock/')
    d.reading('The Top 10 Mistakes AngularJS Developers Make','https://www.airpair.com/angularjs/posts/top-10-mistakes-angularjs-developers-make')

    d = s.day('November 22')
    d.assignment('Web Application: Interface Design',term+'/labs/web-application')

    s.week()

    d = s.day('November 24')
    d.lecture('Web Programming','Javascript')
    d.reading('Javascript',static+'javascript.pdf')
    d.reading('Javascript at Codecademy','http://www.codecademy.com/tracks/javascript?jump_to=4fa836e5996b00000302064a')
    d.reading('JQuery at Codecademy','http://www.codecademy.com/tracks/jquery')

    d = s.day('November 25')
    d.lecture('Web Programming','Group Meetings')
    d.reading('Front End Ops','http://www.ianfeather.co.uk/presentations/front-end-ops/#/t0-begin')

    d = s.day('November 26')
    d.lecture('No Class')

    d = s.day('November 28')
    d.lecture('No Class')

    s.week()

    d = s.day('December 1')
    d.lecture('Web Programming','Users and Authentication')
    d.reading('Users and Authentication',static+'users-and-authentication.pdf')
    d.assignment('Web Application: Milestone 1',term+'/labs/web-application')

    d = s.day('December 3')
    d.lecture('Web Programming','Web Services')
    d.reading('Web Services',static+'web-services.pdf')
    d.reading('Interactive REST Tutorial','http://phprestsql.sourceforge.net/')

    d = s.day('December 5')
    d.lecture('Web Programming','Web Services')


    s.week()

    d = s.day('December 8')
    d.lecture('Security','Web Vulnerabilities')
    d.reading('Web Vulnerabilities',static+'web-vulnerabilities.pdf')


    d = s.day('December 10')
    d.assignment('Lab: Web Application: Final Report and Submission',term+'/labs/web-application')

    s.week()

    d = s.day('Section 1: December 15, 2:30 pm')
    d.assignment('Final Exam, 111 TMCB','')

    d = s.day('Section 2: December 16, 11:00 am')
    d.assignment('Final Exam, 111 TMCB','')


    return render_template('fall-2014/schedule.html',active='schedule',
                           weeks=s.weeks)
