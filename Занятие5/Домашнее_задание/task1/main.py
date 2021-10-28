count_row = 10
count_col = 10
correct_matrix =[
    [(i * j) + j for j in range(1, count_col)]
    for i in range(1, count_row)
]
for row in range(len(correct_matrix)):
    for col in range(len(correct_matrix[0])):
        print(f"{correct_matrix[count_row][count_col]:2}")




if __name__ == "__main__":
    # Write your solution here
    pass
