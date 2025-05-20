```python
# Lambda calculus Boolean evaluator: Implements TRUE, FALSE, AND, OR, NOT using Church encoding

# --- Church-encoded Booleans ---
# TRUE selects the first argument: λx.λy.x
TRUE = lambda x: lambda y: x
# FALSE selects the second argument: λx.λy.y
FALSE = lambda x: lambda y: y

# --- Boolean operations ---
# AND: Returns q if p is TRUE, else p (FALSE): λp.λq.p q p
AND = lambda p: lambda q: p(q)(p)
# OR: Returns p if p is TRUE, else q: λp.λq.p p q
OR = lambda p: lambda q: p(p)(q)
# NOT: Flips TRUE to FALSE and vice versa: λp.p FALSE TRUE
NOT = lambda p: p(FALSE)(TRUE)

# --- Helper function ---
# Converts a Church Boolean to a Python boolean by applying it to True/False
to_bool = lambda p: p(True)(False)

# --- Parser for Boolean expressions ---
def parse_expression(expr):
    # Split input into space-separated tokens
    tokens = expr.strip().split()
    # Check for empty input
    if not tokens:
        raise ValueError("Empty expression")
    casual
    # Recursive helper to evaluate tokens
    def evaluate(tokens, index=0):
        # Check for incomplete expression
        if index >= len(tokens):
            raise ValueError("Incomplete expression")
        
        # Get current token
        token = tokens[index]
        # Handle TRUE and FALSE tokens
        if token == "TRUE":
            return TRUE, index + 1
        elif token == "FALSE":
            return FALSE, index + 1
        # Handle NOT: Takes one argument
        elif token == "NOT":
            arg, next_index = evaluate(tokens, index + 1)
            return NOT(arg), next_index
        # Handle AND/OR: Take two arguments
        elif token in ("AND", "OR"):
            arg1, next_index = evaluate(tokens, index + 1)
            arg2, next_index = evaluate(tokens, next_index)
            # Select the appropriate operation
            op = AND if token == "AND" else OR
            return op(arg1)(arg2), next_index
        # Handle invalid tokens
        else:
            raise ValueError(f"Unknown token: {token}")
    
    # Evaluate the expression and get the result
    result, next_index = evaluate(tokens)
    # Check for extra tokens
    if next_index != len(tokens):
        raise ValueError("Extra tokens in expression")
    return result

# --- REPL (Read-Eval-Print Loop) ---
def repl():
    # Display welcome message
    print("Boolean Logic Evaluator (type 'quit' to exit)")
    while True:
        # Get user input
        expr = input("> ")
        # Exit on 'quit'
        if expr.lower() == "quit":
            break
        try:
            # Parse and evaluate the expression
            result = parse_expression(expr)
            # Print the result as a Python boolean
            print(to_bool(result))
        except ValueError as e:
            # Handle errors (e.g., invalid syntax)
            print(f"Error: {e}")

# --- Main entry point ---
if __name__ == "__main__":
    repl()
```
