def create_abbreviation(phrase):
    words = phrase.split()  
    abbreviation = []  
    
    for word in words:  
        if len(word) > 0 and word[0].isalpha():  
            abbreviation.append(word[0].upper())  
    
    return ''.join(abbreviation)  

# Примеры из задачи
print(create_abbreviation("Today I learned"))  
print(create_abbreviation("Высшее учебное заведение"))  
print(create_abbreviation("Кот обладает талантом"))  
print(create_abbreviation("Ар 2 Ди #2"))  
print(create_abbreviation("Анна-Мария Волхонская"))  
def create_abbreviation(phrase):
    words = phrase.split()  
    abbreviation = []  
    
    for word in words:  
        if len(word) > 0 and word[0].isalpha():  
            abbreviation.append(word[0].upper())  
    
    return ''.join(abbreviation)  

# Примеры из задачи
print(create_abbreviation("Today I learned"))  
print(create_abbreviation("Высшее учебное заведение"))  
print(create_abbreviation("Кот обладает талантом"))  
print(create_abbreviation("Ар 2 Ди #2"))  
print(create_abbreviation("Анна-Мария Волхонская"))  
