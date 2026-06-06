'''Q) To find the day of the week.'''

class week_day:
    
    def which_week_day(self, day):

            if day == 1:
                print('Monday')

            elif day == 2:
                print('Tuesday')

            elif day == 3:
                print('Wednesday')

            elif day == 4:
                print('Thursday')

            elif day == 5:
                print('Friday')

            elif day == 6:
                print('Saturday')

            elif day == 7:
                print('Sunday')

            else:
                print('Invalid')
    


# METHOD 02 :

    def whichWeekDay(self, day):
        
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        
        if 1<= day <= 7:
            print(days[day - 1])
        
        else:
            print('Invalid')
    
    
# METHOD 03 

    def whichWeekDay(self, day):
        
        days = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
            }
        
        print(days.get(day, 'Invalid'))
        
obj = week_day()
obj.which_week_day(2)
