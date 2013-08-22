from flask import render_template

from config import app
from schedule import *

@app.route('/fall-2012/schedule')
def schedule():
    static = '/static/2012f/'
    term = '/fall-2012/'
    s = Schedule()

    s.week()

    d = s.day("August 27")
    d.lecture('Introduction','The Internet and its Architecture')
    d.reading('The Internet and its Architecture',static + 'lectures/the-internet-and-its-architecture.pdf')

    d = s.day("August 29")
    d.lecture('Systems','Socket Programming')
    d.reading('Socket Programming',static + 'lectures/socket-programming.pdf')

    s.week()

    d = s.day("September 3")
    d.lecture('No Class','Labor Day Holiday')

    d = s.day("September 5")
    d.lecture('Systems','Socket Programming')
    d.assignment('Lab: Messaging Service',term + 'labs/messaging-service')

    s.week()

    d = s.day("September 10")
    d.lecture('Systems','DNS, HTTP')
    d.reading('DNS',static+'lectures/dns.pdf')
    d.reading('HTTP',static+'lectures/http.pdf')
    d.reading('HTTP -- The Gory Details',static+'lectures/http-the-gory-details.pdf')

    d = s.day('September 12')
    d.lecture('Concurrent Programming','Programming Threads in C')
    d.reading('Programming Threads in C',static+'lectures/programming-threads-in-c.pdf')
    d.reading('Pthreads Tutorial','http://www.llnl.gov/computing/tutorials/pthreads/')

    s.week()

    d = s.day('September 17')
    d.lecture('Concurrent Programming','Thread Synchronization, Thread Pool Server Architecture')
    d.reading('Thread Synchronization',static+'lectures/thread-synchronization.pdf')
    d.reading('Java Monitors','http://java.sun.com/developer/Books/performance2/chap4.pdf')

    d = s.day('September 19')
    d.lecture('Concurrent Programming','Thread Synchronization')
    d.assignment('September 22: Lab: Download Accelerator',term + '/labs/download-accelerator')

    s.week()

    d = s.day('September 24')
    d.lecture('Concurrent Programming','Thread Synchronization')

    d = s.day('September 26')
    d.lecture('Concurrent Programming','Event-Driven Server Architecture')
    d.reading('Event-Driven Server Architecture',static+'lectures/event-driven.pdf')

    s.week()

    d = s.day('October 1')
    d.lecture('Systems','System Calls')
    d.reading('System Calls',static+'lectures/system-calls.pdf')
    d.assignment('Lab: Threaded Messaging Service',term + '/labs/threaded-messaging-service')

    d = s.day('October 3')
    d.lecture('Performance Measurement','Queueing Theory')
    d.reading('Queueing Theory',static+'lectures/queueing-theory.pdf')

    s.week()

    d = s.day('October 8')
    d.lecture('No Class','')

    d = s.day('October 10')
    d.lecture('Systems','Introduction to Python Programming')
    d.reading('Python Introduction',static+'lectures/python-introduction.pdf')
    d.reading('Python Documentation','http://www.python.org/')
    d.reading('Dive Into Python','http://diveintopython.org/')
    d.assignment('October 12: Lab: Web Server',term + '/labs/web-server')

    s.week()

    d = s.day('October 15')
    d.lecture('Performance Measurement','Performance Measurement and Workload Models')
    d.reading('Performance Measurement',static+'/lectures/performance-measurement.pdf')

    d = s.day('October 17')
    d.lecture('Midterm','Weeks 1 - 7')
    d.assignment('Midterm','')

    s.week()

    d = s.day('October 22')
    d.lecture('Systems','Web Proxies and Caching')
    d.reading('Web Proxies and Caching',static+'/lectures/web-proxies-and-caching')
    d.reading("O'Reilly Web Caching Chapter",'http://www.oreilly.com/catalog/webcaching/chapter/ch05.html')
    d.assignment('October 23: Lab: Queueing Theory',term + '/labs/queueing-theory')

    d = s.day('October 24')
    d.lecture('Security','Buffer Overflow Attacks')
    d.reading('Buffer Overflow Primer','http://www.securitytube.net/groups?operation=view&groupId=4')

    s.week()

    d = s.day('October 29')
    d.lecture('Security','Network Security')
    d.reading('Network Security',static+'lectures/network-security.pdf')

    d = s.day('October 31')
    d.lecture('Security','Network Security')

    s.week()

    d = s.day('November 5')
    d.lecture('Web Programming','Relational Databases and Entity Relationship Modeling, MySQL')
    d.reading('See WDA Chapters 1, 5.1, Appendix E','')
    d.reading('Database Normalization','http://dev.mysql.com/tech-resources/articles/intro-to-normalization.html')
    d.assignment('Lab: Stack Smashing',term + '/labs/stack-smashing')

    d = s.day('November 7')
    d.lecture('Web Programming','Python Web Frameworks')
    d.assignment('Midterm: MySQL Queries','')

    s.week()

    d = s.day('November 12')
    d.lecture('Web Programming','CSS, Web Design')

    d = s.day('November 14')
    d.lecture('Web Programming','Javascript')
    d.reading('Javascript',static+'/lectures/javascript.pdf')

    s.week()

    d = s.day('November 19')
    d.lecture('Web Programming','Application Review')

    d = s.day('November 21')
    d.lecture('No Class','Thanksgiving Holiday')

    s.week()

    d = s.day('November 26')
    d.lecture('Web Programming','Web Services')
    d.reading('Interactive REST Tutorial','http://phprestsql.sourceforge.net/')
    d.reading('How I Explained REST to My Wife','http://tomayko.com/writings/rest-to-my-wife')
    d.reading('Google Custom Search API','https://developers.google.com/custom-search/v1/overview')
    d.reading('REST for Amazon','http://scripts.incutio.com/amazon/')
    d.reading('Microsoft Bing JSON Interface','http://msdn.microsoft.com/en-us/library/dd250846.aspx')
    d.assignment('Lab: Web Application',term+'/labs/web-application')

    d = s.day('November 28')
    d.lecture('Web Programming','MongoDB')
    d.reading('Why MongoDB Is Awesome','http://www.slideshare.net/jnunemaker/why-mongodb-is-awesome')
    d.reading('Starbucks Does Not Use Two-Phase Commit','http://eaipatterns.com/ramblings/18_starbucks.html')

    s.week()

    d = s.day('December 3')
    d.lecture('Security','Web Vulnerabilities')
    d.assignment('Lab: Rest Interface',term+'/labs/rest-interface')

    d = s.day('December 5')
    d.lecture('Internet Research Lab, Preview of CS 460','')
    d.assignment('Lab: Web Application Vulnerabilities',term+'/labs/web-application-vulnerabilities')

    s.week()

    d = s.day('December 13')
    d.lecture('Final Exam','Section 2')
    d.assignment('Final Exam: 11:00 am - 2:00 pm, 191 SFH','')

    d = s.day('December 14')
    d.lecture('Final Exam','Section 1')
    d.assignment('Final Exam: 11:00 am - 2:00 pm, 191 SFH','')

    return render_template('fall-2012/schedule.html',active='schedule',
                           weeks=s.weeks)
