
def calculate(a: float, b: float, operation: str) -> float:
    """Executa uma operação matemática básica."""

    if operation == "add":
        return a + b

    if operation == "subtract":
        return a - b

    if operation == "multiply":
        return a * b

    if operation == "divide":
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

    raise ValueError(
        "Operação inválida. Use add, subtract, multiply ou divide."
    )
