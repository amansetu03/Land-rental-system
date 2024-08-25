from operations import Land
def load_land(file_name):
    """this function read the land_data.txt and get all the land data"""
    lands = []
    try:
        # read file
        with open(file_name,'r') as file:
            #loop through the file line by line and make object of Land class
            for line in file:
                data = line.strip().split(',')
                # make object
                land = Land(int(data[0].strip()),data[1],data[2],data[3],int(data[4].strip()),data[5].strip())
                lands.append(land)
    except FileNotFoundError:
        # print error message
        print("File note found.")
    return lands

