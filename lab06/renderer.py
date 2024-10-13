def print_table(values: list[tuple[float, float]]):
    table: list[str] = [
        "+---",
        "| x ",
        "+---",
        "| y ",
        "+---",
    ]
    for [x, y] in values:
        strx = str(x)
        stry = str(y)
        maxlen = max(len(strx), len(stry))
        horiz = "+" + "-" * (maxlen + 2)
        table[0] += horiz
        table[1] += "| " + strx.rjust(maxlen) + " "
        table[2] += horiz
        table[3] += "| " + stry.rjust(maxlen) + " "
        table[4] += horiz

    table[0] += "+"
    table[1] += "|"
    table[2] += "+"
    table[3] += "|"
    table[4] += "+"

    print("\n".join(table))