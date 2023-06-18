def get_patient_people(community: list):
    """
    Get a list of all dictionaries where the value for "foes" is an empty list.

    Args:
        community (list): List of dictionaries to iterate through. Each dictionary
                          must contain the keys "name", "friends", and "foes".
                          The "name" values should be unique, and the "friends" and "foes"
                          values must be lists.

    Returns:
        list: List of dictionaries of those with no foes.
    """
    return [person for person in community if person["foes"] == []]


def leave_community(community: list, name: str) -> None:
    """
    Go through the list of dictionaries passed in, removing name from lists for keys "friends" and "foes"
    and the dictionary associated with their name.

    Args:
        community (list): List of dictionaries to iterate through. Each dictionary must contain the keys
                          "name", "friends", and "foes". The "name" values should be unique, and the
                          "friends" and "foes" values must be lists.
        name (str): Name of the person being removed from the list.

    Returns:
        None
    """

    to_remove = []  # List to store dictionaries to be removed

    for person in community:
        if person["name"] == name:
            for friend in person["friends"]:
                friend_dict = next((d for d in community if d["name"] == friend), None)
                if friend_dict is not None and name in friend_dict["foes"]:
                    friend_dict["foes"].remove(name)
            for foe in person["foes"]:
                foe_dict = next((d for d in community if d["name"] == foe), None)
                if foe_dict is not None:
                    if name in foe_dict["friends"]:
                        foe_dict["friends"].remove(name)
                    if name in foe_dict["foes"]:
                        foe_dict["foes"].remove(name)
            to_remove.append(person)  # Add the dictionary to the removal list

    # Remove the dictionaries outside the loop
    for person in to_remove:
        community.remove(person)


def are_community_besties(community: list, name1: str, name2: str) -> bool:
    """
    Determine if the two names passed in are within the community and if they are on each
    other's "friends" list.

    Args:
        community (list): List of dictionaries to iterate through. Each dictionary must contain the keys
                          "name", "friends", and "foes". The "name" values should be unique, and the
                          "friends" and "foes" values must be lists.
        name1 (str): Name of the first person being examined within the list.
        name2 (str): Name of the second person being examined within the list.

    Returns:
        bool: True if both names are within the community and their names are in each other's "friends" list,
              False otherwise.
    """
    for person in community:
        if person["name"] == name1:
            if name2 in person["friends"]:
                for friend in community:
                    if friend["name"] == name2:
                        if name1 in friend["friends"]:
                            return True
                        else:
                            return False
            else:
                return False

    return False
def testing():
    # General Inputs
    def get_inputs():
        return [
            # Case 1: Empty List
            [],
            # Case 2: Single Element with friends, no foes
            [{"name": "Bugs",
              "friends": ["Tweety"],
              "foes":[]}],
            # Case 3: Single Element with no friends or foes
            [{"name": "Bugs",
              "friends": [],
              "foes": []
              }],
            # Case 4: Single element with no friends, has foes
            [{"name": "Bugs",
              "friends": [],
              "foes": ["Elmer"]
              }],
            # Case 5: Slightly complicated community
            [{"name": "Bugs",
              "friends": [],
              "foes": ["Elmer"]},
             {"name": "Tweety",
              "friends": ["Bugs","Granny","Lola"],
              "foes": []},
             {"name": "Taz",
              "friends": [],
              "foes": ["Bugs"]},
             {"name": "Granny",
              "friends": ["Bugs", "Tweety"],
              "foes": []}],
            # Case 6: Even more complex community
            [{"name": "Bugs",
              "friends": ["Tweety","Sylvester","Lola"],
              "foes": ["Elmer","Taz","WileE"]},
             {"name": "Tweety",
              "friends": ["Bugs","Granny"],
              "foes": ["Sylvester"]},
             {"name": "Taz",
              "friends": ["Daffy"],
              "foes": ["Bugs"]},
             {"name": "Granny",
              "friends": ["Bugs", "Tweety","Sylvester"],
              "foes": []},
             {"name": "Sylvester",
              "friends": ["Bugs", "Granny"],
              "foes": ["Tweety","Bugs"]}
             ]]
    def test_get_patient_people():
        test_count = 0
        case1,case2,case3,case4,case5,case6 = get_inputs()
        case5_expects = [{"name": "Tweety",
              "friends": ["Bugs","Granny","Lola"],
              "foes": []},
              {"name": "Granny",
              "friends": ["Bugs", "Tweety"],
              "foes": []}]
        case6_expects = [{"name": "Granny",
              "friends": ["Bugs", "Tweety","Sylvester"],
              "foes": []}]
        test_cases = [{"input": case1,
                        "expect": [],
                        "output":get_patient_people(case1),
                        "message" : "Empty list should get back empty list"},
                    {"input": case2,
                    "expect": case2,
                    "output": get_patient_people(case2),
                    "message": "Bugs has no foes and should be in the list returned"},
                    {"input": case3,
                     "expect": case3,
                     "output": get_patient_people(case3),
                     "message": "Bugs has no foes and should be in the list returned"},
                    {"input": case4,
                     "expect": [],
                     "output": get_patient_people(case4),
                     "message": "Bugs has foes and should have empty list returned"},
                    {"input": case5,
                     "expect": case5_expects,
                     "output": get_patient_people(case5),
                     "message": "Two dictionaries have empty lists associated with key 'foes' (Tweety, Granny)"},
                      {"input": case6,
                       "expect": case6_expects,
                       "output": get_patient_people(case6),
                       "message": "One dictionary has an empty lists associated with key 'foes' (Granny)"}
                      ]
        for test in test_cases:
            test_count += 1
            assert test["output"] == test["expect"], "Error Test Case "+str(test_count)+": " +test["message"]+"\n"+\
                                                     "Input: " + str(test["input"]) + "\n" +\
                                                     "Expected: " + str(test["expect"]) + "\n" +\
                                                     "Output: " + str(test["output"])

        return test_count

    def test_leave_community():
        test_count = 0
        case1,case2,case3,case4,case5,case6 = get_inputs()
        test_cases = [{"input": (case1,"Taz"),
                        "expect": None,
                        "output":leave_community(case1, "Taz"),
                        "message" : "Name not in community list should be unchanged."},
                    {"input": (case2,"Bugs"),
                    "expect": None,
                    "output": leave_community(case2,"Bugs"),
                    "message": "Bugs is in list and should be removed"},
                    {"input": (case3, "Lola"),
                     "expect": None,
                     "output": leave_community(case3,"Lola"),
                     "message": "Bugs has no foes and should not be impacted"},
                    {"input": (case4,"Elmer"),
                     "expect": None,
                     "output": leave_community(case4,"Elmer"),
                     "message": "Bugs has name in list associated with 'foes' and should no longer have name present in list"},
                    {"input": (case5,"Foghorn Leghorn"),
                     "expect": None,
                     "output": leave_community(case5,"Foghorn Leghorn"),
                     "message": "Expect no impact on the list passed in because name not present"},
                      {"input": (case5, "Lola"),
                       "expect": None,
                       "output": leave_community(case5, "Lola"),
                       "message": "Expect name to be removed from list associated with key 'friends' and key 'foes'."},
                      {"input": (case6,"Bugs"),
                       "expect": None,
                       "output": leave_community(case6,"Bugs"),
                       "message": "Name present within numerous lists and as as a dictionary, make sure it is removed from all occurrences"}
                      ]
        for test in test_cases:
            community = test["input"][0]
            name_removed = test["input"][1]
            test_count += 1
            for person in community:
                assert name_removed != person["name"], "Error Test Case "+str(test_count)+": " +test["message"]+"\n"+\
                                                     "Input: " + str(test["input"]) + "\n" +\
                                                     "Output: " + str(community)
                assert name_removed not in  person["friends"], "Error Test Case "+str(test_count)+": " +test["message"]+"\n"+\
                                                     "Input: " + str(test["input"]) + "\n" +\
                                                     "Output: " + str(community)
                assert name_removed not in person["foes"], "Error Test Case "+str(test_count)+": " +test["message"]+"\n"+\
                                                     "Input: " + str(test["input"]) + "\n" +\
                                                     "Output: " + str(community)
        return test_count


    def test_are_community_besties():
        test_count = 0
        case1,case2,case3,case4,case5,case6 = get_inputs()
        test_cases = [{"input": (case1, "Bugs", "Taz"),
                        "expect": False,
                        "output":are_community_besties(case1, "Bugs", "Taz"),
                        "message" : "Neither name is in the list."},
                    {"input": (case2,"Bugs","Foghorn Leghorn"),
                    "expect": False,
                    "output": are_community_besties(case2, "Bugs", "Foghorn Leghorn"),
                    "message": "Bugs is in list but is not friends with 'Foghorn Leghorn'"},
                    {"input": (case3, "Bugs", "Lola"),
                     "expect": False,
                     "output": are_community_besties(case3,"Bugs","Lola"),
                     "message": "Bugs is friends with 'Lola' but Lola not in community list"},
                    {"input": (case4, "Bugs", "Elmer"),
                     "expect": False,
                     "output": are_community_besties(case4,"Bugs","Elmer"),
                     "message": "Bugs has Elmer in list associated with 'foes' not 'friends'"},
                    {"input": (case5, "Elmer", "Foghorn Leghorn"),
                     "expect": False,
                     "output": are_community_besties(case5,"Elmer", "Daffy"),
                     "message": "Neither are within the community"},
                      {"input": (case5, "Tweety", "Granny"),
                       "expect": True,
                       "output": are_community_besties(case5, "Tweety", "Granny"),
                       "message": "Granny and Tweety are in each other's friends lists"},
                      {"input": (case6, "Bugs", ""),
                       "expect": True,
                       "output": are_community_besties(case6, "Bugs", "Sylvester"),
                       "message": "Bugs is in both Sylvester's list of 'foes' and 'friends', should still get True."}
                      ]
        for test in test_cases:
            test_count += 1
            assert test["output"] == test["expect"], "Error Test Case " + str(test_count) + ": " + test[
                "message"] + "\n" + \
                                                       "Input: " + str(test["input"]) + "\n" + \
                                                       "Expected: " + str(test["expect"]) + "\n" + \
                                                       "Output: " + str(test["output"])
        return test_count

    def test_get_all_community_besties():
        test_count = 0
        case1, case2, case3, case4, case5, case6 = get_inputs()
        # Case 5: Expected Output
        tweeties_besties = [{"name": "Granny",
              "friends": ["Bugs", "Tweety"],
              "foes": []}]
        # Case 6: Expected Output
        bugs_besties = [{"name": "Tweety",
              "friends": ["Bugs","Granny"],
              "foes": ["Sylvester"]},
             {"name": "Sylvester",
              "friends": ["Bugs", "Granny"],
              "foes": ["Tweety","Bugs"]}]
        test_cases = [{"input": (case1, "Elmer"),
                       "expect": [],
                       "output": get_all_community_besties(case1, "Elmer"),
                       "message": "Elmer is not in list and has no friends"},
                      {"input": (case2, "Bugs"),
                       "expect": [],
                       "output": get_all_community_besties(case2, "Bugs"),
                       "message": "Bugs has no local besties"},
                      {"input": (case3, "Bugs"),
                       "expect": [],
                       "output": get_all_community_besties(case3, "Bugs"),
                       "message": "Bugs has no local besties"},
                      {"input": (case4, "Elmer"),
                       "expect": [],
                       "output": get_all_community_besties(case4, "Elmer"),
                       "message": "Elmer is not associated with key 'name' within the list and should have no friends"},
                      {"input": (case5, "Tweety"),
                       "expect": tweeties_besties,
                       "output": get_all_community_besties(case5, "Tweety"),
                       "message": "Tweety should have granny as a community bestie"},
                      {"input": (case5, "Taz"),
                       "expect": [],
                       "output": get_all_community_besties(case5, "Taz"),
                       "message": "Taz is in list but has no local besties"},
                      {"input": (case6, "Bugs"),
                       "expect": bugs_besties,
                       "output": get_all_community_besties(case6, "Bugs"),
                       "message": "Bugs is in both Sylvester's list of 'foes' and 'friends',"
                                  " should still be part of list returned."}
                      ]
        for test in test_cases:
            test_count += 1
            assert test["output"] == test["expect"], "Error Test Case " + str(test_count) + ": " +\
                                                       test["message"] + "\n" + \
                                                       "Input: " + str(test["input"][0]) + "\n" + \
                                                       "\t"+ str(test["input"][1])+"\n"+\
                                                       "Expected: " + str(test["expect"]) + "\n" + \
                                                       "Output: " + str(test["output"])
        return test_count

    total_tests = 0
    print("STATING TESTING...")
    print("TESTING: get_patient_people")
    total_tests += test_get_patient_people()
    print("DONE TESTING: get_patient_people")
    print("TESTING: leave_community")
    total_tests += test_leave_community()
    print("DONE TESTING: leave_community")
    print("TESTING: are_community_besties")
    total_tests += test_are_community_besties()
    print("DONE TESTING: are_community_besties")
    print("TESTING: get_all_community_besties")
    total_tests += test_get_all_community_besties()
    print("DONE TESTING: get_all_community_besties")
    print("TESTING COMPLETE", total_tests, "PASSED!")


if __name__=="__main__":
    testing()