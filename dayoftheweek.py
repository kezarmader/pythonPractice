class Solution:
    # This solution doesn't work
    def main(self):
        day = int(input())
        month = int(input())
        year = int(input())

        print(self.dayOfTheWeek(day, month, year))
    
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        months = {
            1: 0,
            2: 31,
            3: 59,
            4: 90,
            5: 120,
            6: 151,
            7: 181,
            8: 212,
            9: 243,
            10: 273,
            11: 304,
            12: 334
        }
        
        days = {2: "Sunday", 3: "Monday", 4: "Tuesday", 5: "Wednesday", 6: "Thursday", 0: "Friday", 1: "Saturday"}
        
        FIRST_YEAR = 1971
        
        daysFromYears = (year - FIRST_YEAR) * 365
        leepYearDays = ((year - (year % 4)) - (FIRST_YEAR + 1)) // 4
        
        if year % 4 == 0 and month <= 2:
            leepYearDays -= 1
        
        monthsDays = months[month]
        
        weekDay = (daysFromYears + leepYearDays + monthsDays + day) % 7
        
        
        return days[weekDay]

if __name__ == '__main__':
    Solution().main()