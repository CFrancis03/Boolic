# Boolic: Boolean Logic Evaluator written in Python

This is my little passion project where I dove into **lambda calculus** using Python. It’s a simple **Boolean Logic Evaluator** that lets you mess around with TRUE, FALSE, AND, OR, and NOT, all built with pure lambda functions (thanks to Church encoding). I built this in a day to get a hands-on feel for lambda calculus and sharpen my Python skills. 

## What’s This About?

I’m fascinated by how lambda calculus—a super abstract way of thinking about computation—can represent something as basic as Boolean logic with just functions. This project encodes TRUE and FALSE as lambda functions, implements AND, OR, and NOT operations, and includes a parser and REPL to play with expressions like `AND TRUE FALSE` or `NOT TRUE`. It’s a fun way to see how Python’s lambda functions can bring theoretical ideas to life.

### What’s in It?
- **Church Encoding**: Booleans and operations are defined as pure lambda functions (e.g., TRUE picks the first of two arguments).
- **Simple Parser**: Turns prefix-notation inputs (like `OR TRUE FALSE`) into lambda function calls.
- **REPL**: Type expressions and get instant results, with basic error messages if you mess up.
- **No Dependencies**: Just pure Python, keeping things lightweight.

## How to Play With It

1. **What You Need**: Python 3.6 or later. That’s it!
2. **Get the Code**:
   ```bash
   git clone https://github.com/your-username/boolean-logic-evaluator.git
   cd boolean-logic-evaluator
   python3 main.py
