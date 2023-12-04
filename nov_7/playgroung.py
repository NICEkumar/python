paragraph= 'package  paddle  painful  painted  ' \
           'pancake  paper  parade  parent  parking' \
           'parrot  passing  password  peacock  peanut  ' \
           'pencil  penguin  people  pizza  pocket  popcorn ' \
           'Syllable Pacific  pajamas  papaya  passenger  passionate  ' \
           'Pearl Harbor  penalty  penmanship  peppermint  persevere  ' \
           'personal  piano  piggybank  pillowcase  pineapple  policeman  ' \
           'Portugal  post office  potato  public school ' \
           'Syllable pacifier  pardonable  parenthesis ' \
           ' participate  peanut butter  peninsula  perfectionist  ' \
           'perishable  personable  personalize  personalized  pistachio  ' \
           'poison ivy  police station  pomegranate  potato chips  ' \
           'punctuation  punishable   Syllable Panama Canal  ' \
           'pandemonium  particularly  pediatrician  Pennsylvania ' \
           ' perfectionism  perpendicular  personality  possibility'

new= [test for test in paragraph.split()]

para = ''
for text in new:
    para += text.lower() + ' '
print(para)