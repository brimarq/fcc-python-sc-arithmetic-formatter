def arithmetic_arranger(problems, print_answers=False):
    # Check number of problems (limit 5)
    if len(problems) > 5:
        return "Error: Too many problems."

    problems = [prob.split() for prob in problems]
    top, bottom, bases, answers = list(), list(), list(), list()

    for prob in problems:
        operand1, operator, operand2 = prob[0], prob[1], prob[2]

        # Check operator (only accept '+' or '-')
        if not ['+', '-'].count(operator):
            return "Error: Operator must be '+' or '-'."

        # Validate operand types (must only contain digits)
        if not operand1.isnumeric() or not operand2.isnumeric():
            return "Error: Numbers must only contain digits."

        # Validate operand lengths (no more than four digits)
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        result = str(int(operand1) + int(operator + operand2))
        width = max(len(operand1), len(operand2)) + 2

        top.append(operand1.rjust(width))
        bottom.append(operator + operand2.rjust(width - 1))
        bases.append('-' * width)
        answers.append(result.rjust(width))

    space = ' ' * 4
    top = space.join(top)
    bottom = space.join(bottom)
    bases = space.join(bases)
    answers = space.join(answers)

    if print_answers:
        arranged_problems = top + '\n' + bottom + '\n' + bases + '\n' + answers
    else:
        arranged_problems = top + '\n' + bottom + '\n' + bases

    return arranged_problems
