import os
import serial
import datetime

ser = serial.Serial('/dev/ttyUSB0', 9600)

while 1:
	buffer=ser.readline()
	today = datetime.datetime.today()
	aDate = datetime.datetime.strftime(today,"%Y-%m-%d %H:%M:%S")
	bDate = datetime.datetime.strftime(today,"%d.%m.%y - %H:%M")
	t1 = buffer[0:5];
	t2 = buffer[6:11];
	luefter = buffer[12];

	h = file("/tmp/temp.html","w")

	h.write('<META HTTP-EQUIV="refresh" CONTENT="15">')
	h.write('<HTML><HEAD>')
	h.write('<font face="Arial,Helvetica">')
	h.write('<TITLE>DB0HE Temperatur</TITLE></HEAD>')
	h.write('<BODY><H1>DB0HE Temperaturstatus</h1>')
	h.write("<b>aktuelle Messwerte:</b> ("+bDate+"):<P>70cm:<b> "+t1+"&degC"+"</b><P>2m:<b> "+t2+"&degC</b>"+"<P>Luefterstatus:<b> 
"+luefter+"</b>")
	h.write('<P>weitere Informationen: ')
	h.write('<A HREF="http://db0he.de/"')
	h.write('>db0he.de</A> </font></BODY></HTML>')

	h.close()
