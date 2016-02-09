<p align="center">
  <img src="https://raw.githubusercontent.com/davidedc/QR-and-JIRA-check-in-check-out-system/master/objectIcon.png" alt="icon" width="200px" height="200px">
</p>

#QR+JIRA check-in / check-out system

This is based on the Miniqr.reader() library here: https://github.com/franzenzenhofer/miniqr , which is a simple client-side QR code reader written in CoffeeScript.

This QR + JIRA check-in / check-out system allows you to do check-in and check-out of any object (from person to person, of from person to place and viceversa) using JIRA. The check-in and check-out happens waving QR tags in front of the camera.

##How a user uses it
Let's say you pick up a phone from a drawer and use it for the day.
 * go to drawer and pick the phone. Wave the QR code of the phone in front of camera,
 * wave the drawer-specific QR card in front of the camera (checkout)
 * wave your personal QR card in front of the camera (check-in)
The JIRA issue associated with the mobile phone is updated.

##How to configure and run
 * the client(s) only need Chrome and a camera.
 * the server only needs Python and the jira-python library from http://jira-python.readthedocs.org/
 * configure the JIRA URL, admin login and password in minimalLoggingServer.py file
 * run the server by doing " python -m minimalLoggingServer.py "
 * point the browser in the client to http://ipOfServer:8080/index.html
 * in index.html, find "WPS" and replace it with your JIRA project name where you keep your tracking tickets.
 * there is an indexLighter.html page that can be used on netbooks and "weaker" machines - basically contains no animations. If you use that, change "WPS" string in there.

##How to create the QR codes
 * The "items" to be checked in and out are QR codes of the following string: "JIRAISSUEID*BASE64ENCODEOFJIRAISSUEID". For example is a mobile phone is tracked by JIRA issue WPS-1463, then the QR must encode for WPS-1463*V1BTLTE0NjM=
 * Base64 encoding can be done online here:  http://www.opinionatedgeek.com/dotnet/tools/base64encode/
 * QR encoding can be done online here: http://goqr.me/
 * The reason why the base64 part is added is because the javascript library occasionally picks up the wrong QR code, so extra checks are done in the browser to discard those based on the base64 validation
 * any of the locations need to start with "place."
