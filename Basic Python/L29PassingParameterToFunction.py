# def goal(player_name):
#     print(f'Goal for England. Goal for {player_name}')
#
# print("Welcome to the World Cup.")
# goal("Harry Kane")
# goal("Marcus Rashford")


def goal(country_name, player_name):
    print(f'Goal for {country_name}. Goal for {player_name}')

print("Welcome to the World Cup.")
goal("England","Harry Kane")
goal("France","Kylian Mbappe")
goal(player_name="Bruno Fernandes", country_name="Portugal")
# these are called keyword arguments
goal("Germany", player_name="Timo Werner")
# keyword argument after positional argument can work but not vice versa

