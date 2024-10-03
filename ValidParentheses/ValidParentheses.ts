function isValid(s: string): boolean {
    const stack: string[] = [];

    for (let i = 0; i < s.length; i++) {
        console.log(stack);
        const currentChar = s[i];
        if (currentChar === '(' || currentChar === '{' || currentChar === '[') {
            stack.push(currentChar);
            continue;
        }
        else {
            if (stack.length === 0) {
                return false;
            }

            const topChar = stack.pop();

            if (currentChar === ')') {
                if (topChar !== '(') {
                    return false;
                }
            } else if (currentChar === '}') {
                if (topChar !== '{') {
                    return false;
                }
            } else if (currentChar === ']') {
                if (topChar !== '[') {
                    return false;
                }
            }
        }
    }

    return stack.length === 0;
};
