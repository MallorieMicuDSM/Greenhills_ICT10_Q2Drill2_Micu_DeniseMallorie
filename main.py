#Seatwork 1
from pyscript import display, document

def student_candidate(e):
    document.getElementById('output').innerHTML = ' '
    first_name = document.getElementById('student_firstname').value
    last_name = document.getElementById('student_lastname').value

    volleyball_team = ['Poppy' + 'Yeng', 'Aster' + 'Kitchie', 'Caspian' + 'Jhene', 'Zinnia' + 'Niki']
    member_checker = first_name + last_name in volleyball_team 

    display_message = (f'Sorry, you are not in the team', f'Congratulations {first_name +  last_name} you are now in the OBMC volleyball varsity! ')
    
    display(display_message[member_checker], target='output')