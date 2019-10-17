#!/usr/bin/env python

abbr = input ("What is the three-letter abbreviation of this course? ")

nswer_status = 'wrong'
if abbr == 'DSP':
	answer_status = 'correct'

print('You answer is correct!' if answer_status=='correct' else "wrong buddy...try again")