def introduction():
  print("""
  Batman and Green Lantern are on a mission to find an underground enemy base.
  While they are looking for the base, the enemy is notified of their mission
  Batman and Green Lantern need to find their way out and escape the temple.

  You can go only four directions to escape:
  forward, backward, right, left
  """)  

  print("""
  Here is a printed map of the temple. You can use this or a hint, provided in the menu, to find your way out of the temple 
  """)

  file = open("map.txt", "r")
  print(file.read())
  file.close()