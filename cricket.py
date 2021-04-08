batsmen = ["Rohit Sharma", "Ishaan Kishan", "Virat Kohli", "SKY",
           "Rishabh Pant", "Hardik Pandya", "R. Jadega", "J. Bumrah",
           "Y. Chahal", "Md. Shami", "B. Kumar"]

balls = 0
overs = 0
wickets = 0
extras = 0
score = 0


class Extras:
    leg_byes = 0
    wide = 0
    no_ball = 0


class NewBatsman:
    runs = 0
    balls = 0
    out = False
    # strike_rate = 0
    # if balls != 0:
    #     strike_rate = runs / balls

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
        # overs += 1
    print()
    print(strike.name, "*")
    print(strike.runs, "/", strike.balls)
    print()
    print(non_strike.name)
    print(non_strike.runs, "/", non_strike.balls)
    print()
    print("Score = ", score)
    # print()
    print("Total balls = ", balls)
    if balls > 0 and balls % 6 == 0:
        overs = balls / 6
        print("Overs = ", overs)
    print()
    print("==========================================")
    print()
    print("Press 1 for runs")
    print("Press 2 for wicket")
    print("Press 3 for dot ball")
    print("Press 4 for extras")
    print("Press 5 for batsman statistics")
    # print("Press 4 for extras")
    print()

    choice = int(input("Enter choice = "))
    balls += 1
    print()

    if choice == 1:
        runs = int(input("Enter runs = "))

        if runs == 0:
            print("Invalid entry, there is a separate section for dot balls")
            balls -= 1

        else:
            print()
            score += runs
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

    elif choice == 4:
        print("Press 1 for Wide")
        print("Press 2 for Leg Byes")
        print("Press 3 for No Ball")

        print()
        extra = int(input("Enter choice = "))

        if extra == 1:
            Extras.wide += 1
            print("Wide = ", Extras.wide)

        elif extra == 2:
            Extras.leg_byes += 1
            print("Leg Byes = ", Extras.leg_byes)

        elif extra == 3:
            Extras.no_ball += 1
            print("No Ball = ", Extras.no_ball)

        extras += 1
        balls -= 1
        score += 1
        print("Extras = ", extras)

    elif choice == 5:
        print(strike.name, " ---> ", (strike.runs / strike.balls) * 100)
        print(non_strike.name, " ---> ", (non_strike.runs / non_strike.balls) * 100)

