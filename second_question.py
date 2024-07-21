def check_bracket(example_list: list) -> list:
    results = []
    for example in example_list:
        left_bracket = []
        result = [' '] * len(example)
        for i, char in enumerate(example):
            # check unmatched right bracket
            if char == '(':
                left_bracket.append(i)
            elif char == ")":
                if left_bracket:
                    left_bracket.pop()
                else:
                    result[i] = '?'
        # check unmatched left bracket
        if left_bracket:
            for i in left_bracket:
                result[i] = 'x' 

        results.append(example + '\n' + ''.join(result))
    return results

if __name__ == '__main__':
    example_str = [
                    "bge)))))))))",
                    "((IIII))))))",
                    "()()()()(uuu",
                    "))))UUUU((()"
                ]
    results = check_bracket(example_str)
    for result in results:
        print(result)
        print()
