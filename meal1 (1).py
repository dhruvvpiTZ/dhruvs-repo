
def main():
    timeinputted = input("What time is it? ")

    if timeinputted.endswith("a.m.") :
        if timeinputted.startswith("12") :
            return
        else :
            time1 = timeinputted.strip("a.m.")
            no_of_hrs = convert(time1)
            if 7.0 <= no_of_hrs <= 8.0 :
                print("breakfast time")
            else :
                return

    elif timeinputted.endswith("p.m.") :
        if timeinputted.startswith("12") :
            print("lunch time")
        else :
            time2 = timeinputted.strip("p.m.")
            no_of_hrs = convert(time2) + 12
            if no_of_hrs == 13.0 :
                print("lunch time")
            elif 18.0 <= no_of_hrs <= 19.0 :
                print("dinner time")
            else :
                return





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
