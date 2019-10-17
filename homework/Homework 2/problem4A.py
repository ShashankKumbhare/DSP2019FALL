#!/usr/bin/env python

abbr = input ("What is the three-letter abbreviation of this course? ")

answer_status = 'correct' if abbr == 'DSP' else 'wrong'

if answer_status=='correct':
    print('You answer is correct!')
else:
    print("wrong buddy...try again") 