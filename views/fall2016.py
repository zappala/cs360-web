from flask import render_template

from config import app
from schedule import *

@app.route('/fall-2016/schedule')
def fall2016schedule():
    static = '/static/lectures/winter-2014/'
    new = '/static/lectures/fall-2015/'
    latest = '/static/lectures/fall-2016/'
    term = '/fall-2016/'
    s = Schedule()

    s.week()

    d = s.day("August 30")
    d.lecture('Introduction','The Internet and its Architecture')
    d.reading('The Internet and its Architecture',static + 'the-internet-and-its-architecture.pdf')
    d.reading('Neal Stephenson on laying undersea fiber-optic cables','http://www.wired.com/wired/archive/4.12/ffglass.html')

    d = s.day("September 1")
    d.lecture('Introduction','The Internet and its Architecture')

    s.week()

    d = s.day("September 6")
    d.lecture('Systems','Socket Programming')
    d.reading('Socket Programming',static + 'socket-programming.pdf')
    d.assignment('Homework: Linux Command Line',term + 'homework/linux-command-line')


    d = s.day("September 8")
    d.lecture('Systems','Sockets and the OS')
    d.reading('Sockets and the OS',static + 'sockets-and-the-os.pdf')
    d.tutorial('Homework: Git',term + 'homework/git')
    d.tutorial('Homework: Make',term + 'homework/make')

    s.week()

    d = s.day("September 13")
    d.lecture('Systems','DNS')
    d.reading('DNS',static+'dns.pdf')
    d.assignment('Homework: Socket I/O',term + 'homework/socket-io')
    
    d = s.day("September 15")
    d.lecture('Concurrent Programming','Threads and the OS')
    d.reading('Threads and the OS',latest+'threads-and-the-os.pdf')
    d.reading('Thread Pool Architecture',static+'thread-pool-architecture.pdf')
    
    d = s.day("September 16")
    d.assignment('Lab: Messaging Service',term + 'labs/messaging-service')

    s.week()

    d = s.day('September 20')
    d.lecture('Concurrent Programming','Thread Synchronization')
    d.reading('Thread Synchronization',latest+'thread-synchronization.pdf')
    d.reading('Mutexes and Condition Variables',latest+'mutexes-and-condition-variables.pdf')

    d = s.day('September 22')
    d.lecture('Concurrent Programming','Mutexes and Condition Variables')
    d.assignment('Homework: Mutexes and Condition Variables',term + 'homework/mutexes-and-condition-variables')

    s.week()

    d = s.day('September 27')
    d.lecture('No Class')

    d = s.day('September 29')
    d.lecture('Concurrent Programming','Monitors and Thread-Safe Classes')
    d.assignment('Homework: Synchronization Practice',term + 'homework/synchronization-practice')
    d.reading('Monitors and Thread-Safe Classes',latest+'monitors-and-thread-safe-classes.pdf')

    s.week()

    d = s.day('October 4')
    d.lecture('Concurrent Programming','Semaphores')
    d.reading('Semaphores',latest+'semaphores.pdf')

    d = s.day('October 6')
    d.lecture('Concurrent Programming','Semaphores')
    d.reading('Semaphores',latest+'semaphores.pdf')
    d.assignment('Homework: Semaphores',term + 'homework/semaphores')

    s.week()
    d = s.day('October 10')
    d.assignment('Lab: Threaded Messaging Service',term + 'labs/threaded-messaging-service')
    
    d = s.day('October 11')
    d.lecture('Concurrent Programming and Systems','Deadlock and UNIX Domain Sockets')
    d.reading('Deadlock',static+'deadlock.pdf')
    d.reading('UNIX Domain Sockets',static+'unix-domain-sockets.pdf')


    d = s.day('October 13')    
    d.assignment('Midterm, in class, covers Week 1 - Week7')
    
    s.week()

    d = s.day('October 18')
    d.lecture('Systems','Introduction to Python Programming')
    d.reading('Introduction to Python',static+'introduction-to-python.pdf')
    d.reading('Python at Codecademy','http://www.codecademy.com/tracks/python')
    d.reading('Python Documentation','http://www.python.org/')
    d.reading('Dive Into Python','http://www.diveinto.org/python3/')

    d = s.day('October 20')
    d.lecture('Systems','Python Networking and Threading, Lab Discussion')
    d.reading('Python Networking and Threading',static+'python-networking-and-threading.pdf')
    d.assignment('Homework: Introduction to Python',term + 'homework/introduction-to-python')


    s.week()

    d = s.day('October 25')
    d.lecture('Systems','HTTP')
    d.reading('HTTP',static+'http.pdf')
    d.assignment('Homework: Python Threading',term + 'homework/python-threading')


    d = s.day('October 27')
    d.lecture('Systems','Web Proxies, Caching, and CDNs')
    d.reading('Web Proxies, Caching, and CDNs',latest+'web-proxies-caching-and-cdns.pdf')
    d.reading("O'Reilly Web Caching Book",'http://shop.oreilly.com/product/9781565925366.do')

    s.week()
    d = s.day('October 31')
    d.assignment('Lab: Download Accelerator',term + 'labs/download-accelerator')

    d = s.day('November 1')
    d.lecture('Concurrent Programming','Python Socket Programming, Event Driven Architecture')
    d.reading('Python Socket Programming',static+'python-socket-programming.pdf')
    d.reading('Event-Driven Architecture',static+'event-driven-architecture.pdf')
    d.reading('Why Threads Are A Bad Idea (for most purposes)','http://chess.cs.umd.edu/class/spring2009/cmsc433/Lectures/threadVsEvents.pdf')


    d = s.day('November 3')
    d.lecture('Concurrent Programming','Web Server Lab Discussion')

    s.week()

    d = s.day('November 8')
    d.lecture('Performance Measurement','Queueing Theory')
    d.reading('Queueing Theory',static+'queueing-theory.pdf')

    d = s.day('November 10')
    d.assignment('Homework: Queueing Theory',term + 'homework/queueing-theory')
    d.lecture('Peer-to-Peer Networking','Peer-to-Peer Networking')
    d.reading('Peer-to-Peer Networking',latest+'peer-to-peer-networking.pdf')

    s.week()

    d = s.day('November 15')
    d.lecture('No Class')

    d = s.day('November 17')
    d.assignment('Midterm, in class')

    
    s.week()

    d = s.day('November 22')
    d.lecture('No Class -- Friday Instruction')

    # d.lecture('Peer-to-Peer Networking','Peer-to-Peer Group Experiment')

    s.week()

    d = s.day('November 28')
    d.assignment('Lab: Web Server',term + 'labs/web-server')
    
    d = s.day('November 29')
    d.lecture('Security','Network Security')
    d.reading('Network Security',new+'network-security.pdf')
    
    # d.assignment('Homework: Event-Driven Programming')
    # d.assignment('Homework: CrowdSourced Measurements')

    d = s.day('December 1')
    d.lecture('Security','Network Security')
    
    s.week()

    d = s.day('December 6')
    d.lecture('Security','TBD')
    
    d = s.day('December 8')
    d.lecture('Security','TBD')

    d.assignment('Lab: Secure Messaging')

    s.week()

    d = s.day('Section 1: December 12, 11:00 am')
    d.assignment('Final Exam, 130 MARB','')

    d = s.day('Section 2: December 14, 3:00 pm')
    d.assignment('Final Exam, 130 MARB','')


    return render_template('fall-2016/schedule.html',active='schedule',
                           weeks=s.weeks)
