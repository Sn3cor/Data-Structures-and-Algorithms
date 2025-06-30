#jak sprawdzic czy slowo jest anagramem
#tablica liter
#dodajemy wystąpeinia liter z pierwszego slowa
#odejmujemy wysąpeinia liter z drugiego słowa

def is_anagram(string1, string2):
    alphabet = [0 for _ in range(26)]
    for char in string1:
        alphabet[ord(char)-97]+=1

    for char in string2:
        alphabet[ord(char)-97]-=1

    for el in alphabet:
        if el!=0:
            return False
    return True

print(is_anagram("all","lla"))