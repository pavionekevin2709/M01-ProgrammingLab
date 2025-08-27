# Knock Knock Cow Joke Extravaganza!
# Tells one super silly cow knock knock joke and checks user responses.

def tell_cow_joke():
    # The cow joke details
    who = "Cow"
    punchline = "Cow says moo, not who, silly!"
    
    # Start the joke
    print("Knock knock!")
    reply1 = input("Say something: ").strip().lower()
    
    # Check for "who's there?"
    if reply1 == "who's there?":
        print(who)
        reply2 = input("Now say: ").strip().lower()
        
        # Check for "cow who?"
        if reply2 == "cow who?":
            print(punchline)
        else:
            print("Moo-ve over! You gotta say 'Cow who?' or the cows will hide your hay!")
    else:
        print("Oh no! Say 'Who's there?' or the cow will moo at you all night!")

def main():
    # Welcome to the cow party
    print("Welcome to the Great Cow Knock Knock Joke!")
    tell_cow_joke()
    print("Thanks for moo-ving through the joke!")

# Start the fun
if __name__ == "__main__":
    main()