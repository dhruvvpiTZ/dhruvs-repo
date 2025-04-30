
def main():
    timeinputted = input("What time is it? ")

#if user inputs time in 12 hour format then appropriately tell user what to eat.
    if timeinputted.endswith("a.m.") :

#time in 12 hr format which ends with a.m. goes from 12:00 a.m. to 11:59 a.m.

        if timeinputted.startswith("12") :
            return
        else :
            timein24hrf = timeinputted.strip("a.m.")

# here timein24hrf will be in this range - [1:00, 11:59]
#in this range only breakfast is possible

            no_of_hrs = convert(timein24hrf)
            if 7.0 <= no_of_hrs <= 8.0 :
                print("breakfast time")
            else :
                return

    elif timeinputted.endswith("p.m.") :

#time in 12 hr format which ends with p.m. goes from 12:00 p.m. to 11:59 p.m.
#12:00 p.m. to 1:00 p.m.(12:00-13:00) is lunch time, and 6:00 p.m. to 7:00 p.m. (18:00-19:00) is dinner time.

        if timeinputted.startswith("12") :
            print("lunch time")
#program has been asked to print lunch time between 12:00 p.m. and 12:59 p.m.

        else :
#convert time in 12 hr format which ends with p.m. to time in 24 hr format

            hours, minutes = timeinputted.strip("p.m.").split(":")
            hours = int(hours) + 12
            minutes = int(minutes)

            timein24hrf = str(hours) + ":" + str(minutes)

#here timein24hrf lies in this range - [13:00, 23:59]
#in this time range lunch is possible at exactly 13:00 and dinner between 18:00 and 19:00

            no_of_hrs = convert(timein24hrf)
            if no_of_hrs == 13.0 :
                print("lunch time")
            elif 18.0 <= no_of_hrs <= 19.0 :
                print("dinner time")
            else :
                return

#if user inputs time in 24 hr format then tell the user what to eat

    else :
        timein24hrf = timeinputted
        no_of_hrs = convert(timein24hrf)
        if 7.0 <= no_of_hrs <= 8.0 :
            print("breakfast time")
        elif 12.0 <= no_of_hrs <= 13.0 :
            print("lunch time")
        elif 18.0 <= no_of_hrs <= 19.0 :
            print("dinner time")



# create a function called convert(time) , that converts time a str in 24 hr format , to the corresponding number of hours as a float.
def convert(time) :
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return float(((hours * 60) + minutes)/60)


if __name__ == "__main__":
    main()
