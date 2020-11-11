# solution
def whichExit2(theatre):
	# get the row, and seat that i'm in
	row = [row for row in theatre if 0 in row]
	seat = row.index(0)

	# get the number of people sitting on the right side
	right_seats = row[seat:]
	right = sum([1 for person in right_seats if person > 0])

	# get the number of people sitting on the left side
	left_seats = row[:seat]
	left = sum([1 for person in left_seats if person > 0])

	return ["left", "right"][right < left] if right != left else "same"


print(whichExit([
	[1, 1, 1, 1, 1],
	[-1, 1, -1, 1, 1],
	[1, 0, -1, 1, 1]
]))
