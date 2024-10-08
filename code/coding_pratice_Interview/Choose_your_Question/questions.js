const question_of_the_day = () =>{

    const arr = [ "palindrome_check", "reverse_string", "reverse_array", "armstrong_number", "fibonacci_series", "sum_of_digits", "factorial", "prime_check", "largest_element_in_array", "count_vowels", "anagram_check", "second_largest_in_array", "count_words_in_string", "even_or_odd", "gcd_of_two_numbers", "power_using_recursion", "check_digits_in_string", "merge_sorted_arrays", "leap_year_check", "longest_word_length", "Remove Duplicates from a Sorted Array", "Find the Missing Number in a Series", "Merge Two Sorted Lists", "Program to Find the Prime Factors of a Number.", "Anagram", "find sum of natural numbers", "Longest Palindrome in a String" ]

    const random = Math.trunc(Math.random()*arr.length) 
    console.log("Today Question is:",arr[random]);
    
}

// question_of_the_day()