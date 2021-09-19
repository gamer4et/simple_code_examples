# My solution of https://www.hackerrank.com/challenges/climbing-the-leaderboard

def my_find(array,el): #el - current player score
					   #array - list of other players scores
	if el>=array[0]: return 1 
	if el == array[-1]: return len(array)
	if el < array[-1]: return len(array) +1
    #using binary search for acceleration
	l = 1
	r = len(array)-1
	while l<r:
		m = (l+r)//2
		if array[m] > el:
			l = m+1
		if array[m] < el:
			r = m
		if array[m] == el:
			return m+1
	#we need one more condition,because m is approximate place(+-1)
	if array[m] > el: return m+2
	return m+1
def climbingLeaderboard(ranked,player):
	#ranked = list of players ranks
	#player = list of player scores
	last = ranked[0]
	new_ranked = [last]
	for el in ranked:
		if el != last:
			new_ranked += [el]
			last = el
	return [(my_find(new_ranked,p)) for p in player]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

