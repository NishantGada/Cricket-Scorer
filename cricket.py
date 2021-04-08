batsmen = ["Rohit Sharma", "Ishaan Kishan", "Virat Kohli", "SKY",
           "Rishabh Pant", "Hardik Pandya", "R. Jadega", "J. Bumrah",
           "Y. Chahal", "Md. Shami", "B. Kumar"]

balls = 0
overs = 0
wickets = 0
extras = 0


class NewBatsman:
    runs = 0
    balls = 0
    out = False
    if balls != 0:
        strike_rate = runs / balls

    def __init__(self, name):
        self.name = name


strike = NewBatsman(batsmen[wickets])
non_strike = NewBatsman(batsmen[wickets + 1])

# print(strike.name, "*")
# print(strike.runs, "/", strike.balls)
#
# print()
#
# print(non_strike.name)
# print(non_strike.runs, "/", non_strike.balls)
# print()


while 1:
    if balls > 0 and balls % 6 == 0:
        strike, non_strike = non_strike, strike
        overs += 1
        # print("overs = ", overs)
    print()
    print(strike.name, "*")
    print(strike.runs, "/", strike.balls)
    print()
    print(non_strike.name)
    print(non_strike.runs, "/", non_strike.balls)
    print()
    print("Total balls = ", balls)
    if balls > 0 and balls % 6 == 0:
        print("overs = ", overs)
    print()
    print("==========================================")
    print()
    print("Press 1 for runs")
    print("Press 2 for wicket")
    print("Press 3 for dot ball")
    print("Press 4 for extras")
    print()

    choice = int(input("Next Ball = "))
    balls += 1
    print()

    if choice == 1:
        runs = int(input("Enter runs = "))

        if runs == 0:
            print("Invalid entry, there is a separate section for dot balls")
            balls -= 1

        else:
            print()
            strike.runs += runs
            strike.balls += 1

            if runs % 2 == 0:
                pass
                # print(strike.name, "*")
                # print(strike.runs, "/", strike.balls)
                # print()
                # print(non_strike.name)
                # print(non_strike.runs, "/", non_strike.balls)
            else:

                strike, non_strike = non_strike, strike

                # print(strike.name, "*")
                # print(strike.runs, "/", strike.balls)
                # print()
                # print(non_strike.name)
                # print(non_strike.runs, "/", non_strike.balls)

    elif choice == 2:
        wickets += 1
        print("Press 1 for strike")
        print("Press 2 for non-strike")
        print()
        wicket = int(input("Enter player = "))
        if wicket == 1:
            print()
            print(strike.name, "OUT")
            print("-------------------------------------")
            strike = NewBatsman(batsmen[wickets + 1])
            print(strike.name, "IN")
        elif wicket == 2:
            print()
            print(non_strike.name, "OUT")
            print("-------------------------------------")
            non_strike = NewBatsman(batsmen[wickets + 1])
            print(non_strike.name, "IN")

    elif choice == 3:
        strike.balls += 1




