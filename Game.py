print('Hello, welcome to our project..!!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. What is the best Propgramming Language? ')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('2. What is 2 + 8 + 9 - 1? ')
    if ans.lower() == '18':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('3. What is better a 1050ti or a 1060 (graphics cards)? ')
    if ans.lower() == '1060':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('4. Who come second in the stanely cup finals? ')
    if ans.lower() == 'nights' or ans.lower() == 'vegas':
        score += 1
        print('Correct')
    else:
        print('Incorrect')   

print('Thank you for playing, you got', score, "question correct..")
mark = (score/total_q) * 100

print("Mark: ", str(mark) + '%' )
print('Goodbye')
