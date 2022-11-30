file = open("data 4.txt", 'r')

first_line = file.readline()
stripped = first_line.rstrip()
numbers = stripped.split(",")

rest_of_file = file.read()
step_1 = rest_of_file.strip()
step_2 = step_1.split("\n\n")
step_3 = [x.split("\n") for x in step_2]
step_4 = [[line.split() for line in board] for board in step_3]
boards = [[[[element, 0] for element in line] for line in board] for board in step_4]

score = 0

for k in numbers:
    for board in boards:
        for line in board:
            for element in line:
                if element[0] == k:
                    element[1] = 1

    row_sums = [[sum(line[i][1] for i in range(5)) for line in board] for board in boards]
    column_sums = [[sum(line[i][1] for line in board) for i in range(5)] for board in boards]

    # part 1

    # winners = 0

    # for board in row_sums:
    #     if 5 in board:
    #         print("A winner has been found!")
    #         winning_board = row_sums.index(board)
    #         winners += 1

    # for board in column_sums:
    #     if 5 in board:
    #         print("A winner has been found!")
    #         winning_board = column_sums.index(board)
    #         winners += 1

    # if winners > 0:
    #     for line in boards[winning_board]:
    #         for element in line:
    #             if element[1] == 0:
    #                 score += int(element[0])
    #     print(score*int(k))
    #     break

    if len(boards) > 1:
        for board in row_sums:
            if 5 in board:
                winning_board = row_sums.index(board)
                row_sums.remove(row_sums[winning_board])
                column_sums.remove(column_sums[winning_board])
                boards.remove(boards[winning_board])

        for board in column_sums:
            if 5 in board:
                winning_board = column_sums.index(board)
                row_sums.remove(row_sums[winning_board])
                column_sums.remove(column_sums[winning_board])
                boards.remove(boards[winning_board])
    else:
        if 5 in row_sums[0] or 5 in column_sums[0]:
            for row in boards[0]:   
                for element in row:
                    if element[1] == 0:
                        score += int(element[0])
            print(score*int(k))
            break




        
