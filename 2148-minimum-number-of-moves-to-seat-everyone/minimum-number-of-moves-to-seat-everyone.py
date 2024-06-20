class Solution(object):
    def minMovesToSeat(self, seats, students):
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)

        moves_counter = 0

        for i in range(len(sorted_seats)):
            moves_counter += abs(sorted_seats[i] - sorted_students[i])

        return moves_counter