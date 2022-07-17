from os import system

# Parameters.1
length = 20
robo_x = 10
right_cliff = 20
left_cliff = 1
battery = 3
bombX_1 = 9
bombX_2 = 13
bombX_3 = 6
medic_1 = 7
medic_2 =18
money_bag_1 = 8
money_bag_2 = 14
money_bag_3 = 17
portal = 16
# Parameters.2
health_level = 100
battery_level = 105
bomb_damage = 40
charging = 30
medic_help = 30
battery_charging = 40
energy_consumption_for_each_step = 5
initial_number_of_steps = -1
finite_number_of_steps = 1
points_earned = 0
cash_earnings = 150
###################################################################################################
while True :
    system ( "cls" )
# Introduction to the game
    print ( "Cyborg Killer\n")
    print ( "Level 2\n")
    print ( "Difficulty = easy\n")
    print ( "◾" * 20 , "\n" )
# Code for money
    print ( "Total points earned = " , points_earned , " .\n" )
# Code for battery
    if battery_level > 10 :
        initial_number_of_steps += finite_number_of_steps
        battery_level -= energy_consumption_for_each_step
        print ( "Steps = " , initial_number_of_steps , " . Battery_level = " , battery_level , " .\n")
    else :
        battery_level <= 10 
        print ( "You're exhausted . GAME OVER !!! ☠\n" )
        break
# Code for health
    if health_level > 1 :
        print ( "Your health level = " , health_level , "\n")
    else :
        health_level <= 0
        print ( "Your health level = 0\n" ) 
        print ( "You 're dead 😈 . GAME OVER !!! ☠\n" )
        break
# Code for left cliff
    if robo_x == left_cliff :
        print ( "Your health level = 0\n" )
        print ( "You 're dead 😈 ( The reason is you fell off a cliff ) . GAME OVER !!! ☠\n" )
        break
# Code for right cliff
    if robo_x == right_cliff :
        print ( "Your health level = 0\n" )
        print ( "You 're dead 😈 ( The reason is you fell off a cliff ) . GAME OVER !!! ☠\n" )
        break
# Code for bombs
    if robo_x == bombX_1 :
        print ( "You stepped on a bomb and lost 40 percent of your health .\n" )
        health_level -= bomb_damage
        print ( "Your health level = " , health_level , "\n" )
    if robo_x == bombX_2 :
        print ( "You stepped on a bomb and lost 40 percent of your health .\n" )
        health_level -= bomb_damage
        print ( "Your health level = " , health_level , "\n" )
    if robo_x == bombX_3 :
        print ( "You stepped on a bomb and lost 40 percent of your health .\n" )
        health_level -= bomb_damage
        print ( "Your health level = " , health_level , "\n" )
# Code for medics
    if robo_x == medic_1 :
        print ( "You have received medical help , your health has increased by 30 percent .\n" )
        health_level += medic_help
        print ( "Your health level = " , health_level , "\n" )
    if robo_x == medic_2 :
        print ( "You have received medical help , your health has increased by 30 percent .\n" )
        health_level += medic_help
        print ( "Your health level = " , health_level , "\n" )

# Code for battery charging
    if robo_x == battery :
        print ( "You got a battery , your charge increased by 40 percent .\n" )
        battery_level += battery_charging
        print ( "Your battery_level = " , battery_level , " .\n")
# Code for money
    if robo_x == money_bag_1 :
        print ( "You got 150 points 💸$$$💸\n" )
        points_earned += cash_earnings
        print ( "Total points earned = " , points_earned , " .\n" )
    if robo_x == money_bag_2 :
        print ( "You got 150 points 💸$$$💸\n" )
        points_earned += cash_earnings
        print ( "Total points earned = " , points_earned , " .\n" )
    if robo_x == money_bag_3 :
        print ( "You got 150 points 💸$$$💸\n" )
        points_earned += cash_earnings
        print ( "Total points earned = " , points_earned , " .\n" )
# Code for portal
    if robo_x == portal :
        level_complet = input ( "Do you want to complete the level ( yes or no ) ? ____" )
        print ( "\n" )
        if level_complet == "yes" :
            print ( "🎇🎇🎇You have successfully completed the level !!!🎇🎇🎇\n") 
            print ( "Total points earned = " , points_earned , end = ".\n" )
            print ( "Thank you for playing !!!" )
            break
    x= 1
    print ( "\n" )
# Code for designations
    while x <= length :
        if x == robo_x :
            print ( "🤖" , end= "")
        elif x == bombX_1 :
            print ( "💣" , end= "")
        elif x == bombX_2 :
            print ( "💣" , end= "")
        elif x == bombX_3 :
            print ( "💣" , end= "")
        elif x == battery :
            print ( "🔋" , end= "")
        elif x == medic_1 :
            print ( "⛑" , end= "")
        elif x == medic_2 :
            print ( "⛑" , end= "")
        elif x == left_cliff :
            print ( "⛒" , end= "")
        elif x == right_cliff :
            print ( "⛒" , end= "")
        elif x == money_bag_1 :
            print ( "💰" , end= "")
        elif x == money_bag_2 :
            print ( "💰" , end= "")
        elif x == money_bag_3 :
            print ( "💰" , end= "")
        elif x == portal :
            print ( "🌀" , end= "")        
        else :
            print ( "▬" , end= "")
        x += 1
    print ( "\n" )
# Code for direction
    direction = input ( "dir ( a / b ) > " )
    if direction == "a" :
        robo_x -= 1
    if direction == "b" :
        robo_x += 1