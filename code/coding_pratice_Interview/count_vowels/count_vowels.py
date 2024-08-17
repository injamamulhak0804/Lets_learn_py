def count_vowels(value):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0;
    for letter in value:
        if(letter in vowels):
            count += 1
    print("The Total numbers of Vowels are: ", count)


count_vowels("education")