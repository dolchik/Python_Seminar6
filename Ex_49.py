
def find_farthest_orbit(orbits):
    elip = [i for i in orbits if i[0] != i[1]]
    areas = [i[0] + i[1] for i in elip ]
    maxindex = areas.index(max(areas))
    return elip[maxindex]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 


print(*find_farthest_orbit(orbits))