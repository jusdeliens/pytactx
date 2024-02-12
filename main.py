import j2l.pytactx.agent as pytactx
import env
import event
import time

# 🌐 Connect our robot in the arena
agent = pytactx.Agent(playerId=env.ROBOTID, arena=env.ARENA, username=env.USERNAME, password=env.PASSWORD, server=env.BROKERADDRESS, port=env.BROKERPORT, verbosity=env.VERBOSITY)

# 🆕 Handle all robot events in 👉 event.py  
event.subscribe(agent)

# ➰ Main loop
while True:
  # 🛰️ Synchronize our robot with the arena server 
  agent.update()

  # 🧭 Changing direction every 300 ms
  agent.lookAt((agent.dir + 1) % 4)
  time.sleep(0.3)
