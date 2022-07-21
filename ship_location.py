big_ship = int ( input ( "Enter the ship's location = " ) )
for x in range(1,11):
    if x == big_ship:
      print( "W", end="" )
    elif x == big_ship - 1 : 
        print ("w", end="")
    elif x == big_ship + 1 : 
        print ("w", end="")
    else:
      print( "~", end="" )