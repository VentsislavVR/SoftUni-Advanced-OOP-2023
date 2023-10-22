def team_lineup(*args):
    lineup = {}

    for player in args:
        if player[1] not in lineup:
            lineup[player[1]] = []
        lineup[player[1]].append(player[0])
    result = sorted(lineup.items(), key=lambda x: (-len(x[1]), x[0]))

    total = ''
    for team,player in result:
        total += f"{team}:\n"
        for p in player:
            total += f"  -{p}\n"

    return total


# def team_lineup(*args):
#    # Create a dictionary to organize players by country and count the number of players per country
#    lineup = {}
#
#    for player, country in args:
#       if country not in lineup:
#          lineup[country] = []
#       lineup[country].append(player)
#
#    result = sorted(lineup.items(), key=lambda x: (-len(x[1]), x[0]))
#    formatted_result = ''
#
#    for country, players in result:
#       formatted_result += f"{country}:\n"
#       for player in sorted(players):
#          formatted_result += f"  -{player}\n"
#
#    return formatted_result

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

