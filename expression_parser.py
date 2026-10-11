import math
import re


TOKEN_PATTERN = re.compile(
    r"\s*(?:(\d+(?:\.\d*)?|\.\d+)|([()+\-*/%^]))"
)


class ExpressionParser:
    def __init__(self, expression):
        self.tokens = []
        self.position = 0

        index = 0

        while index < len(expression):
            match = TOKEN_PATTERN.match(expression, index)

            if not match:
                if expression[index:].strip() == "":
                    break
                raise ValueError(
                    f"Invalid character at position {index}: "
                    f"{expression[index]!r}"
                )

            number, operator = match.groups()

            if number is not None:
                self.tokens.append(("NUMBER", float(number)))
            else:
                self.tokens.append((operator, operator))

            index = match.end()

        self.tokens.append(("EOF", None))

    def peek(self):
        return self.tokens[self.position][0]

    def consume(self, expected=None):
        token_type, value = self.tokens[self.position]

        if expected is not None and token_type != expected:
            raise ValueError(
                f"Expected {expected}, found {token_type}"
            )

        self.position += 1
        return value

    def parse(self):
        if self.peek() == "EOF":
            raise ValueError("Expression cannot be empty.")

        result = self.parse_expression()

        if self.peek() != "EOF":
            raise ValueError(
                f"Unexpected token: {self.tokens[self.position][1]}"
            )

        if not math.isfinite(result):
            raise ValueError("Result is not finite.")

        return result

    def parse_expression(self):
        result = self.parse_term()

        while self.peek() in ("+", "-"):
            operator = self.consume()

            right = self.parse_term()

            if operator == "+":
                result += right
            else:
                result -= right

        return result

    def parse_term(self):
        result = self.parse_unary()

        while self.peek() in ("*", "/", "%"):
            operator = self.consume()
            right = self.parse_unary()

            if operator in ("/", "%") and right == 0:
                raise ZeroDivisionError("Division by zero.")

            if operator == "*":
                result *= right
            elif operator == "/":
                result /= right
            else:
                result %= right

        return result

    def parse_unary(self):
        if self.peek() == "+":
            self.consume("+")
            return self.parse_unary()

        if self.peek() == "-":
            self.consume("-")
            return -self.parse_unary()

        return self.parse_power()

    def parse_power(self):
        result = self.parse_primary()

        # Right-associative exponentiation:
        # 2 ^ 3 ^ 2 means 2 ^ (3 ^ 2).
        if self.peek() == "^":
            self.consume("^")
            exponent = self.parse_unary()

            if abs(exponent) > 10000:
                raise ValueError("Exponent is too large.")

            result = math.pow(result, exponent)

        if not math.isfinite(result):
            raise ValueError("Intermediate result is not finite.")

        return result

    def parse_primary(self):
        if self.peek() == "NUMBER":
            return self.consume("NUMBER")

        if self.peek() == "(":
            self.consume("(")
            result = self.parse_expression()
            self.consume(")")
            return result

        raise ValueError(
            f"Unexpected token: {self.tokens[self.position][1]}"
        )


def main():
    print("Arithmetic Expression Evaluator")
    print("Supported operators: +, -, *, /, %, ^")
    print("Parentheses are supported. Type 'quit' to exit.")

    while True:
        try:
            expression = input("\nEnter expression: ").strip()

            if expression.lower() == "quit":
                break

            parser = ExpressionParser(expression)
            result = parser.parse()

            print(f"Result: {result:g}")

        except (ValueError, ZeroDivisionError, OverflowError) as error:
            print(f"Error: {error}")

        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
