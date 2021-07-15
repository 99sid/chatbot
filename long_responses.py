import random

R_EATING = "I don't likke eating anything beacuse I'm a bot obviously!"

def unknown():
    response = ['Could you please re pharse that',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response
