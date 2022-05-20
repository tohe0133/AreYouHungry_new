from activity import Activity
import geopy.distance

# coordinates for a place in central Umeå
my_coords = (63.82587043650309, 20.26303012372108)


def create_activities(database_name):
    global my_coords
    data_base = open(database_name, "r")
    _activity_info = data_base.readlines()
    data_base.close()
    fix_items = ""
    for line in _activity_info:
        fix_items += "\n" + line.strip()

    activity_list = []
    activityDatabase = fix_items

    # Creates a list containing all info from each
    # activity as single elements in the list.
    all_activities = activityDatabase.split('\n')
    del all_activities[0]

    # Creates a new list where the elements consist of
    # lists containing all info from each activity as elements.
    activ_lists = []
    for i in range(len(all_activities)):
        activ_lists.append(all_activities[i].split(','))

    # Creates a temporary list, takes each element
    # from activ_lists, creates an instance of
    # an Activity which is then put into the final list.
    for i in range(len(activ_lists)):
        item_activ = activ_lists[i]
        item_coords = (item_activ[1],item_activ[2])
        distance = geopy.distance.distance(my_coords, item_coords).m
        activity_list.append(Activity(item_activ[0], distance, item_activ[3], item_activ[4], item_coords[0], item_coords[1]))
        # test to print the activity created
        # print(activity_list[0].coords)
    return activity_list
