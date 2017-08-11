
# coding: utf-8

# In[ ]:

""" Script to convert my notes with latex into anki flashcards. """
""" Take a text file, export text with questions and answers separated by semicolons"""

def has_single_semicolon(line):
    semicolon_count = 0 
    for character in line:
        if character == ';':
            semicolon_count += 1
    if semicolon_count != 1:
        return False
    else:
        return True

def add_latex_tags(card):
    tag_open = True
    tag_positions = []
    new_line = card
    for character_index, character in enumerate(card):
        if character == '$':
            tag_positions.append(character_index)
    if len(tag_positions) % 2 != 0:
        print 'Error, missing tag.'
    for position in sorted(tag_positions, reverse=True):
        if tag_open == True:
            new_line = new_line[:position] + '[/' + new_line[position] + ']' + new_line[position+1:]
            tag_open = False
        else:
            new_line = new_line[:position] + '[' + new_line[position] + ']' + new_line[position+1:]
            tag_open = True 
    return new_line

def anki_conversion(doc, new_filename):
    with open(doc, 'r') as full_text,          open(doc[:-4]+'_formatted.txt','w') as formatted_cards,          open(doc[:-4]+'_errors.txt','w') as card_errors:      
        
        for line in full_text:
            if has_single_semicolon(line):
                formatted_cards.write(add_latex_tags(line))
            else:
                card_errors.write(line)

