from client import *

import random
import time

# "ovaXXXXXXXXXXXX" A REMPLACER PAR UNE STR CONTENANT L'IDENTIFIANT DE VOTRE OVA
robot:IRobot = OvaClientMqtt(robotId="ova1097bdcc944d", server="mqtt.jusdeliens.com", port=1883, useProxy=False)
#robot:IRobot = OvaClientHttpV2(url="192.168.71.1", verbosity=3)

def onRobotEvent(source, event, value):
	...
	#print("Rx event", event, "from",source,":",value)

# Appel de la callback onRobotEvent pour chaque évènements du robot 
robot.addEventListener(RobotEvent.imageReceived, onRobotEvent)
robot.addEventListener(RobotEvent.robotChanged, onRobotEvent)
robot.addEventListener(RobotEvent.robotConnected, onRobotEvent)
robot.addEventListener(RobotEvent.robotDisconnected, onRobotEvent)

print("########################")
while (robot.isConnectedToRobot() == False):
	print("Awaiting robot connection...")
	robot.update()
	time.sleep(1)	

print("########################")
print("🟢 BEGIN TEST")
robot.enableCamera(False)
beginMelody = []
for i in range(3,11,1):
	beginMelody.append((i,50))
robot.playMelody(beginMelody)
robot.setMotorSpeed(0,0)
robot.setLedColor(0,0,0)
robot.update()

print("########################")
print("🔦 Test sensors")
print("Change the light above the robot to see how sensors values change")
for i in range(10):
	robot.update()
	time.sleep(0.1)
	print("⬆️ Photo front lum: ", robot.getFrontLuminosity())
	print("⬇️ Photo back lum: ", robot.getBackLuminosity())
	print("🔋 Battery voltage: ", robot.getBatteryVoltage())
	print("⏱️ Timestamp: ", robot.getTimestamp())
	print("📸 Camera img "+str(robot.getImageWidth())+"x"+str(robot.getImageHeight())+" shot after "+str(robot.getImageTimestamp())+"ms")

print("########################")
print("🔊 Test actuators")
robot.stop()
for i in range(20):
	robot.update()
	robot.setLedColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	robot.playMelody([[random.randint(0,12),200]])
	robot.setMotorSpeed(random.randint(0,50), random.randint(0,50))
robot.stop()

print("########################")
print("📸 Test camera")
robot.enableCamera(True)
for i in range(50):
	robot.update()
	sr = 0
	sg = 0
	sb = 0
	n = 0
	w = robot.getImageWidth()
	h = robot.getImageHeight()
	for x in range(0,w,10):
		for y in range(0,h,10):
			color = robot.getImagePixelRGB(x,y)
			sr += color[0]
			sg += color[1]
			sb += color[2]
			n+=1
	if ( n > 0 ):
		sr = sr//n
		sg = sg//n
		sb = sb//n
		print("📸 Camera img "+str(w)+"x"+str(h)+" shot after "+str(robot.getImageTimestamp())+"ms")
		print("🔴<R>="+str(sr)+" 🟢<G>="+str(sg)+" 🔵<B>="+str(sb))
		robot.setLedColor(sr,sg,sb)
	time.sleep(0.1)
robot.enableCamera(False)

# End
print("########################")
print("🔴 END TEST")
endMelody = []
for i in range(10,2,-1):
	endMelody.append((i,50))
robot.playMelody(endMelody)
robot.setMotorSpeed(0,0)
robot.setLedColor(0,0,0)
robot.update()

