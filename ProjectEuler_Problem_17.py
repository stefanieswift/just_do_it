# ProjectEuler - Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.



def findnumberinletter(number_to_convert, letter_array):
    letters_to_numbers_singles = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
    };
        
    letters_to_numbers_tens = {
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety",
    }
    if(len(str(number_to_convert)) == 4):
    		first_number = int(str(number_to_convert)[:1])
    		letter_array.append(letters_to_numbers_singles[first_number])
    		letter_array.append("thousand")
    		number_to_convert = number_to_convert - first_number * 1000
    elif(len(str(number_to_convert)) == 3):
    		first_number = int(str(number_to_convert)[:1])
    		letter_array.append(letters_to_numbers_singles[first_number])
    		letter_array.append("hundred")
    		number_to_convert = number_to_convert - first_number * 100
    		if number_to_convert > 0:
    			letter_array.append("and")
    elif (len(str(number_to_convert)) == 2):
		if number_to_convert < 21:
		    letter_array.append(letters_to_numbers_tens[number_to_convert])
		    return letter_array
		else:
		    first_number = int(str(number_to_convert)[:1])
		    tens = first_number * 10
		    letter_array.append(letters_to_numbers_tens[tens])
		    number_to_convert = number_to_convert - tens
    elif number_to_convert > 0: 
    	letter_array.append(letters_to_numbers_singles[number_to_convert])
    	return letter_array
    else:
    	return letter_array
    findnumberinletter(number_to_convert, letter_array)

def letterstonumbers( function, start_number, end_number ):
    letter_array = []
    for number_to_convert in range(start_number, (end_number+1)):
    	function(number_to_convert, letter_array);
    print len("".join(letter_array))
	


letterstonumbers(findnumberinletter, 1, 1000)



