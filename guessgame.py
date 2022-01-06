print('''
*******************************************************************************
                                  _____
                                 |     |
                                 | | | |
                                 |_____|
                           ____ ___|_|___ ____
                          ()___)         ()___)
                          // /|           |\ \\
                         // / |           | \ \\
                        (___) |___________| (___)
                        (___)   (_______)   (___)
                        (___)     (___)     (___)
                        (___)      |_|      (___)
                        (___)  ___/___\___   | |
                         | |  |           |  | |
                         | |  |___________| /___\
                        /___\  |||     ||| //   \\
                       //   \\ |||     ||| \\   //
                       \\   // |||     |||  \\ //
                        \\ // ()__)   (__()
                              ///       \\\
                             ///         \\\
                           _///___     ___\\\_
                          |_______|   |_______|
''')
print("Welcome to Megatron Moon Island.")
print("Your mission is to find Bumble Bee.")
print("Aperiax Crate","///","Zoolem Crate")
Landing = input("Where do you want to land? AC or ZC \n")
if Landing == "AC":
  print("Launch Drones","///","Ground search- team ALFA")
  Next_move = input("What is your next move?LD or GS\n")
  if Next_move == "LD":
    print("Enemy spotted our drones-- MISSION COMPROMISED!!!!!")
  elif Next_move == "GS":
    print("Divide the ALFA group in to Team A and B","///","Stick together")
    second_move = input("What do you want to do with the team? DV / ST \n")
    if second_move == "DV":
      print("Teams divided to spread Northwest side and Northeast side - one group compromised and so the other during rescue - MISSION COMPROMISED!!!!")
    elif second_move == "ST":
      print("Northwest direction","///","Northeast direction")
      third_move = input("Direction to choose for search in the crater - NW/NE? \n")
      if third_move == "NW":
        print("Enemy spotted our team - MISSION COMPROMISED!!!!!")
      elif third_move == "NE":
        fourth_move = input("Direction to choose - Towards the cave(Left) or away from cave(Right)\n")
        if fourth_move == "Right":
          print("Moon Monsters attacked the team - MISSION COMPROMISED!!!!!")
        elif fourth_move == "Left":
          print("Use explosives","///","Use mechanical arms")
          final_move = input("Open the cave with explosives(EP) or move the boulders using mechanical arms(MA)\n")
          if final_move == "EP":
            print("Explosives sound alerts enemies - MISSION COMPROMISED!!!!")
          elif final_move == "MA":
            print("Rescued BUMBLE BEE from cave and escape - MISSION ACCOMPLISHED!!!!!!!!")
else:
  print("Landing unstable on Zoolem Crater")
  print("MISSION COMPROMISED!!!!!!")

