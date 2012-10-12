# a truly minimal HTTP proxy

import SocketServer
import SimpleHTTPServer
import urllib
from jira.client import JIRA

PORT = 8080

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.
options = {
    'server': 'JIRA URL'
}

jira = JIRA(options, basic_auth=('JIRA USERNAME', 'JIRA PASSWORD'))


class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        theFile = "."+self.path
        print "requested ", self.path
        if not "pickedUpQR" in theFile:
        	self.copyfile(urllib.urlopen(theFile), self.wfile)
        else:
        	print "QR code ", theFile
        	with open("log.txt", "a+") as f:
        		f.write(theFile+"\n")
        	issueNumber = (theFile.split('|',2)[0]).split('=',1)[1];
        	theFrom = theFile.split('|',2)[1];
        	theTo = theFile.split('|',2)[2];
        	print "issue number " ,  issueNumber;
        	print "from " , theFrom;
        	print "to " , theTo;
        	# Get an issue.
        	issue = jira.issue(issueNumber)
        	#issue.update(assignee={'name': 'andy.jones'})
        	#issue.update(assignee={'name': ''})
        	if theTo.startswith('place.'):
        		issue.update(assignee={'name': ''})
        		jira.add_comment(issueNumber, 'placed into ' + theTo.split('.',1)[1] + ' by ' + theFrom)
        	else :
        		issue.update(assignee={'name': theTo})

httpd = SocketServer.ForkingTCPServer(('', PORT), Proxy)
print "serving at port", PORT
httpd.serve_forever()