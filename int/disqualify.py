def disqualify(arr):
    disqualified_teams = set()
    team_counts = {}
    new_arr = []

    # Count the occurrences of each team in the input array
    for team in arr:
        if team not in team_counts:
            team_counts[team] = 0
        team_counts[team] += 1

    # Iterate through the input array
    for i in range(len(arr)):
        # If the team at position i has not been disqualified
        # and has all its members present in the remaining positions
        if arr[i] not in disqualified_teams and team_counts[arr[i]] == 4:
            # Add the positions of the team members to the new array
            new_arr.extend([arr[j] for j in range(i, i + 4)])
            # Mark the team as disqualified
            disqualified_teams.add(arr[i])
            # Decrease the count of team members
            team_counts[arr[i]] -= 4

    # Iterate through the input array again to add the disqualified teams
    for i in range(len(arr)):
        # If the team at position i has been disqualified
        if arr[i] in disqualified_teams:
            # Add the team members to the new array
            new_arr.append(arr[i])
    print(new_arr)
    return new_arr


arr = [1,1,3,4,2,1,1,3,3,3,2,4,4,2,4,2]
print(disqualify(arr))
#[1, 1, 3, 4, 1, 1, 3, 3, 3, 4, 4, 4, 2, 2, 2, 2]