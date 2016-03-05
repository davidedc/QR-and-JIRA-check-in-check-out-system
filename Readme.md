<p align="center">
  <img src="https://raw.githubusercontent.com/davidedc/QR-and-JIRA-check-in-check-out-system/master/objectIcon.png" alt="icon" width="200px" height="200px">
</p>

#QR+JIRA check-in / check-out system

This QR + JIRA check-in / check-out system allows you to do check-in and check-out of any object (from person to person, of from person to place and viceversa) using JIRA. The check-in and check-out happens waving QR tags in front of the camera.

Just create a JIRA issue for each object you want to track. Then generate the QR for the objects, the people and the places involved in the check-ins and check-outs.

(see also my other JIRA-related projects [here](https://github.com/davidedc/JIRA-composable-command-line-tools) [here](https://github.com/davidedc/Customise-JIRA-Cards-Appearance) [here](https://github.com/davidedc/Basic-JIRA-And-Wiki-automation-with-Python-And-Mechanize) and [here](https://github.com/davidedc/JIRA-multi-board-view))

##Example
Let's say you pick up a phone from a drawer and use it for the day.
 * go to drawer and pick the phone. Wave the QR code of the phone in front of camera (the QR code represents a JIRA issue that tracks the phone, which will be updated with the info related to the checkout/checkin that is happening),
 * wave the drawer-specific QR card (representing a place) in front of the camera (checkout).
 * wave your personal QR card (representing a person) in front of the camera (check-in)
The JIRA issue associated with the mobile phone is updated with the place and the person.

<p align="center">
  <img src="https://raw.githubusercontent.com/davidedc/QR-and-JIRA-check-in-check-out-system/master/readme-images/QR-codes-of-mobile-phone-place-person.png" alt="QRs as used" width="70%">
</p>

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
 * any of the locations need to start with "place." (see "place.safe" in the image below)

##Example generated QR codes for the example in the picture above

<p align="center">
  <img src="https://raw.githubusercontent.com/davidedc/QR-and-JIRA-check-in-check-out-system/master/readme-images/generated-QR-codes-1-of-2.png" alt="QRs as used" width="70%">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/davidedc/QR-and-JIRA-check-in-check-out-system/master/readme-images/generated-QR-codes-2-of-2.png" alt="QRs as used" width="70%">
</p>

#Credits

This is based on the Miniqr.reader() library here: https://github.com/franzenzenhofer/miniqr , which is a simple client-side QR code reader written in CoffeeScript.
