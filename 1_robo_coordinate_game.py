length = int ( input ( "Enter the path length = " ) )
robo_x =  int ( input ( "Enter the number of robot steps = " ) )
x = 1
while x <= length :
    if robo_x > length :
        print ( "This operation is not possible" )
        break
    elif robo_x <= 0 :
        print ( "This operation is not possible" )
        break
    else:
        print ( "-" , end = " " )
        x += 1 
        if x == robo_x :
            print ( "@" , end = " " )
