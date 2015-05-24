#!/usr/bin/python
import time
from daemon import runner
import graphitesend
from pywatts import get_data

class App():
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path =  '/tmp/currentcost_daemon.pid'
		self.pidfile_timeout = 5


        def run(self):
                while True:
                        graphitesend.init(graphite_server='localhost', system_name='', group='power', prefix='house')                        
                        try:
                                watts, temperature = get_data()
                                graphitesend.send_dict({'temperature':temperature, 'usage':watts})
                                time.sleep(5)
                        except (KeyboardInterrupt, SystemExit):
                                raise
                        except:
                                pass
                                
                        time.sleep(5)
                                
                                
app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
                                
