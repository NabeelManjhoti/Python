def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks to create a fun story.\n")

    name = input("Enter a name: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")

    story = f"""
    Once upon a time, {name} went on an adventure to {place}. It was a {adjective} day, 
    and the sun was shining brightly. Along the way, {name} found a mysterious {noun}.
    Curious, {name} decided to {verb} it. Suddenly, a {animal} appeared out of nowhere!
    What an unforgettable journey!
    """

    print("\nHere is your Mad Libs story:")
    print(story)


if __name__ == "__main__":
    mad_libs()