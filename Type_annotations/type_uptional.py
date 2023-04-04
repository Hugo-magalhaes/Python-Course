def soma(x: int, y: float | None = None) -> float:
    if isinstance(y, float | int):
        return x + y
    return x + x
