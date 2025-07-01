def get_pascal_row(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        row.append(row[-1] * (rowIndex - i + 1) // i)
    return row

# Примеры использования:
print(get_pascal_row(3))  
  