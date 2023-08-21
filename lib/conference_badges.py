def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]  

def assign_rooms(names):
    room_assignments = []
    room_number = 1

    for name in names:
        room_assignment = f"Hello, {name}! You'll be assigned to room {room_number}!"
        room_assignments.append(room_assignment)
        room_number += 1

    return room_assignments


def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)
