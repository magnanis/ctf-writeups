# parse libinput debug events

def read_slots(line: str):
    slots = line.split('(')
    # slot = slots[0].rsplit(' ')[1]
    seat_slot = slots[1].split(')')[0]
    return int(seat_slot)

def read_coords(line: str):
    # coords = line.partition("/")
    # coords = re.findall("(.+/)-(.+)", line)
    coords = line.rsplit("/")
    # return coords
    x = coords[0].rsplit(' ', 1)[1]
    y = coords[1].split(' ', 1)[0]
    return float(x), float(y)