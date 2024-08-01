# Write your solution here
def filter_solutions():
    # Baca isi file solutions.csv
    with open('solutions.csv', 'r') as infile:
        lines = infile.readlines()
    
    correct_lines = []
    incorrect_lines = []
    
    # Proses setiap baris
    for line in lines:
        line = line.strip()  # Hilangkan spasi putih di awal dan akhir baris
        name, problem, result = line.split(';')
        result = int(result)
        
        # Evaluasi masalah
        if '+' in problem:
            operands = problem.split('+')
            correct_result = int(operands[0]) + int(operands[1])
        elif '-' in problem:
            operands = problem.split('-')
            correct_result = int(operands[0]) - int(operands[1])
        
        # Periksa apakah hasilnya benar
        if result == correct_result:
            correct_lines.append(line)
        else:
            incorrect_lines.append(line)
    
    # Tulis solusi yang benar ke correct.csv
    with open('correct.csv', 'w') as correct_file:
        for line in correct_lines:
            correct_file.write(line + '\n')
    
    # Tulis solusi yang salah ke incorrect.csv
    with open('incorrect.csv', 'w') as incorrect_file:
        for line in incorrect_lines:
            incorrect_file.write(line + '\n')