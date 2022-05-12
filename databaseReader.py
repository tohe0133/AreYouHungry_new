from activity import Activity


def create_activities(database_name):
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
        activity_list.append(Activity(item_activ[0], item_activ[1], item_activ[2], item_activ[3]))
    return activity_list