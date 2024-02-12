def onAmmoChange(agent, evType, ammoBefore, ammoAfter):
  """Play melody and colors on fire"""
  if ( ammoBefore > ammoAfter ):
    agent.robot.setLedAnimation([
      (255,128,64, 100), # 👈 Modifier 255 par la composante rouge de votre couleur, 128 vert, 64 bleu, et 100 par la durée d'allumage de la LED en ms
      # 👆 Copier coller la ligne au dessus pour jouer d'autres couleurs
    ])
    agent.robot.playMelody([
      (440, 100), # 👈 Modifier 440 par la fréquence en Hz, et 100 par la durée en ms
      # 👆 Copier coller la ligne au dessus pour jouer d'autres notes
    ])

def onLifeChange(agent, evType, lifeBefore, lifeAfter):
  """Play melody and colors on damage"""
  if ( lifeBefore > lifeAfter ):
    agent.robot.setLedAnimation([
      (255,128,64, 100), # 👈 Modifier 255 par la composante rouge de votre couleur, 128 vert, 64 bleu, et 100 par la durée d'allumage de la LED en ms
      # 👆 Copier coller la ligne au dessus pour jouer d'autres couleurs
    ])
    agent.robot.playMelody([
      (440, 100), # 👈 Modifier 440 par la fréquence en Hz, et 100 par la durée en ms
      # 👆 Copier coller la ligne au dessus pour jouer d'autres notes
    ])

def onRobotDeath(agent, evType, lifeBefore, lifeAfter):
  """Play melody and colors on damage"""
  if ( lifeBefore > lifeAfter ):
    agent.robot.setLedAnimation([
      (255,128,64, 100), # 👈 Modifier 255 par la composante rouge de votre couleur, 128 vert, 64 bleu, et 100 par la durée d'allumage de la LED en ms
      # 👆 Copier coller la ligne au dessus pour jouer d'autres couleurs
    ])
    agent.robot.playMelody([
      (440, 100), # 👈 Modifier 440 par la fréquence en Hz, et 100 par la durée en ms
      # 👆 Copier coller la ligne au dessus pour jouer d'autres notes
    ])

def onRobotConnected(agent, evType, nExeBefore, nExeAfter):
  """Play melody and colors the robot enters the arena"""
  agent.robot.setLedAnimation([
    (255,128,64, 100), # 👈 Modifier 255 par la composante rouge de votre couleur, 128 vert, 64 bleu, et 100 par la durée d'allumage de la LED en ms
    # 👆 Copier coller la ligne au dessus pour jouer d'autres couleurs
  ])
  agent.robot.playMelody([
    (440, 100), # 👈 Modifier 440 par la fréquence en Hz, et 100 par la durée en ms
    # 👆 Copier coller la ligne au dessus pour jouer d'autres notes
  ])

def subscribe(agent):
  """Abonnement au évènements du jeu pour appeler les fonctions ci-dessous"""
  agent.addEventListener("ammo",onAmmoChange)
  agent.addEventListener("life",onLifeChange)
  agent.addEventListener("nDeath",onRobotDeath)
  agent.addEventListener("nExe",onRobotConnected)
