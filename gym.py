print('WELCOME TO TIGER STRENGTH FITNESS')
a=input('Enter your name:')
print('Hi',a)
print('Frist lets calculate your BMI')
height=int(input('Enter your height:'))
weight=int(input('Enter your weight:'))
bmi=(weight/(height*height))*10000
print(bmi)
if bmi<18:
    print('1.Underweight')
elif bmi>=18 and bmi<=24.9:
    print('2.Healthy')
elif bmi>25:
    print('3.Overweight')
choice=int(input('Select your result:'))

if choice==1:
    print('You can follow one of these programes:')
    print('1.Bulk')
    print('2.Mass XL')
    choice=int(input('So which programe would you like to follow?'))
    if choice==1:
        print('WELCOME TO BULK PROGRAMME')
        print('First calculate your BMR')
        W=int(input('Enter your weight:'))
        H=int(input('Enter your height:'))
        A=int(input('Enter your age:'))
        BMR=10*W+6.25*H-5*A+5
        print(BMR)
        print('Now calculate the maintenance calories:')
        Formula=float(input('Enter your BMR:'))
        Formula=BMR*1.5
        print('So your maintenance calories are:')
        print(Formula)
        print('Add extra calories for gaining')
        print('If you want to gain 0.5lbs per week then add 250 calories')
        print('If you want to gain 1lbs per week then add 500 calories')
        print('If you want to gain 2lbs per week then add 1000 calories')
        calories=float(input('Enter how much calories you want to add:'))
        calories=calories+Formula
        print('So your total calories are:')
        print(calories)
        print('So your workout programe is split like this:')
        print('1.Monday- Chest & Triceps')
        print('2.Tuesday- Legs')
        print('3.Wednesday- Shoulders & Traps')
        print('4.Thursday- Arms')
        print('5.Friday- Cardio & Abs')
        print('6.Saturday- Back & Triceps')
        print('7.Sunday- OFF')
        choice=int(input('Enter your todays workout:'))
        
        if choice==1:
            print('1.Monday- Chest & Triceps')
            print('a.Warm up-PUSH UPS-2 Sets')
            print('b.INCLINE PRESS- 3Sets- 8Reps')
            print('c.BENCH PRESS- 3Sets- 8Reps')
            print('d.DB FLY- 3Sets- 8Reps')
            print('These are your daily meals')
            meal1={'banana':2,'SCOOP WHEY ':24,'240ML MILK ':8,'150ML WATER ':0,'1.5SP PEANUT BUTTER ':5,'1/2 CUP OATS POWDER ':3}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'2 WHOLE EGGS ':12,'2 EGG WHITES ':8,'3-4 MULTIGRAIN BREAD SLICES ':8,'2SP JAM ':0}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'1 CUP RICE ':3,'1/2 CUP KIDNEY BEANS':5,'4 EGG WHITES':16}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
            
        elif choice==2:
            print('2.Tuesday- Legs')
            print('a.Warm up- BODY WEIGHT SQUAT- 2Sets- 20Reps')
            print('b.BACK SQUAT- 3Sets- 8Reps')
            print('c.BARBELL DEADLIFT- 3Sets- 8Reps')
            print('These are your daily meals')
            meal1={'1.banana':2,'2.SCOOP WHEY ':24,'3.240ML MILK ':8,'4.150ML WATER ':0,'1.5SP PEANUT BUTTER ':5,'1/2 CUP OATS POWDER ':3}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'2 WHOLE EGGS ':12,'2 EGG WHITES ':8,'3-4 MULTIGRAIN BREAD SLICES ':8,'2SP JAM ':0}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'1 CUP RICE ':3,'1/2 CUP KIDNEY BEANS':5,'4 EGG WHITES':16}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==3:
            print('Wednesday- Shoulders & Traps')
            print('Warm up-STANDING SHOULDER PRESS- 2Sets- 15Reps')
            print(' SEATED BARBELL PRESS- 3Sets- 8Reps')
            print('CABLE REAR DELT FLY- 3Sets- 8Reps')
            print('These are your daily meals')
            meal1={'banana':2,' SCOOP WHEY ':24,'240ML MILK ':8,'150ML WATER ':0,'1.5SP PEANUT BUTTER ':5,'1/2 CUP OATS POWDER ':3}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'2 WHOLE EGGS ':12,'2 EGG WHITES ':8,'3-4 MULTIGRAIN BREAD SLICES ':8,'2SP JAM ':0}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'1 CUP RICE ':3,'1/2 CUP KIDNEY BEANS':5,'4 EGG WHITES':16}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==4:
            print('Thursday- Arms')
            print(' DB CURL/DB KICKBACK- 1Set- 15reps')
            print(' CLOSE GRIP EZ BAR CURL- 3Sets- 8Reps')
            print('SPIDER INWARD CURL- 3Sets- 8Reps')
            print('These are your daily meals')
            meal1={'banana':2,' SCOOP WHEY ':24,'240ML MILK ':8,'150ML WATER ':0,'1.5SP PEANUT BUTTER ':5,'1/2 CUP OATS POWDER ':3}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'2 WHOLE EGGS ':12,'2 EGG WHITES ':8,'3-4 MULTIGRAIN BREAD SLICES ':8,'2SP JAM ':0}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'1 CUP RICE ':3,'1/2 CUP KIDNEY BEANS':5,'4 EGG WHITES':16}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==5:
            print('Friday- Cardio & Abs')
            print(' STABILITY BALL CURL- 3Sets- 8Reps')
            print('HANGING LEG RAISE- 3Sets- 8Reps')
            print(' PLANK SIDE TO SIDE- 3Sets- 8Reps')
            print('These are your daily meals')
            meal1={'banana':2,' SCOOP WHEY ':24,'240ML MILK ':8,'150ML WATER ':0,'1.5SP PEANUT BUTTER ':5,'1/2 CUP OATS POWDER ':3}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'2 WHOLE EGGS ':12,'2 EGG WHITES ':8,'3-4 MULTIGRAIN BREAD SLICES ':8,'2SP JAM ':0}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'1 CUP RICE ':3,'1/2 CUP KIDNEY BEANS':5,'4 EGG WHITES':16}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==6:
            print('Saturday- Back & Triceps')
            print(' PULL UPS- 3Sets- 8Reps')
            print('WIDE GRIP LAT PULL DOWN- 3Sets- 8Reps')
            print('BARBELL ROWS- 3Sets- 8Reps')
            print('These are your daily meals')
            meal1={'banana':2,' SCOOP WHEY ':24,'240ML MILK ':8,'150ML WATER ':0,'1.5SP PEANUT BUTTER ':5,'1/2 CUP OATS POWDER ':3}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'2 WHOLE EGGS ':12,'2 EGG WHITES ':8,'3-4 MULTIGRAIN BREAD SLICES ':8,'2SP JAM ':0}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'1 CUP RICE ':3,'1/2 CUP KIDNEY BEANS':5,'4 EGG WHITES':16}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        else:
            print('Sunday- OFF')
            print('These are your daily meals')
            meal1={'banana':2,' SCOOP WHEY ':24,'240ML MILK ':8,'150ML WATER ':0,'1.5SP PEANUT BUTTER ':5,'1/2 CUP OATS POWDER ':3}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'2 WHOLE EGGS ':12,'2 EGG WHITES ':8,'3-4 MULTIGRAIN BREAD SLICES ':8,'2SP JAM ':0}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'1 CUP RICE ':3,'1/2 CUP KIDNEY BEANS':5,'4 EGG WHITES':16}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
          
        
    elif choice==2:
        print('WELCOME TO MASS XL PROGRAME')
        print('First calculate your BMR')
        W=int(input('Enter your weight:'))
        H=int(input('Enter your height:'))
        A=int(input('Enter your age:'))
        BMR=10*W+6.25*H-5*A+5
        print(BMR)
        print('Now calculate the maintenance calories')
        Formula=int(input('Enter your BMR:'))
        Formula=BMR*1.5
        print('So your maintenance calories are:')
        print(Formula)
        print('Add extra calories for gaining')
        print('If you want to gain 0.5lbs per week then add 250 calories')
        print('If you want to gain 1lbs per week then add 500 calories')
        print('If you want to gain 2lbs per week then add 1000 calories')
        calories=int(input('Enter how much calories you want to add:'))
        calories=calories+Formula
        print('So your total calories are:')
        print(calories)
        print('So your workout programe is split like this:')
        print('1.Monday- Sloulders & Traps')
        print('2.Tuesday- Back')
        print('3.Wednesday- Biceps & Triceps')
        print('4.Thursday- Chest')
        print('5.Friday- Legs')
        print('6.Saturday- Cardio & Abs')
        print('7.Sunday- Rest')
        choice=int(input('Enter your choice:'))
        if choice==1:
            print('Monday- Sloulders & Traps')
            print('Warm up- DB SHOULDER PRESS- 3sets- 15reps')
            print('BARBELL SHOULDER PRESS- 5sets- 12reps')
            print('DB FRONT RAISE- 5sets- 12reps')
            print('SINGLE HAND DB PRESS- 5sets- 12reps')
            print('These are your daily meals')
            meal1={'QUINOA ':7,'Apple':0,'Walnuts':2}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={' WHEY ':18,'Banana':0,'milk':8}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            meal3={'Whole eggs':6,'Egg Whites':12,'Rice':3}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
                
            
        elif choice==2:
            print('Tuesday- Back')
            print('Warm up-PULL-UP- 3sets- 15reps')
            print('CLOSE GRIP LAT BAR PULLDOWN- 5sets- 12reps')
            print('WIDE GRIP LAT BAR PULLDOWN- 5sets- 12reps')
            print('T-BAR ROWS- 5sets- 12reps')
            print('These are your daily meals')
            meal1={'QUINOA ':7,'Apple':0,'Walnuts':2}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={' WHEY ':18,'Banana':0,'milk':8}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            meal3={'Whole eggs':6,'Egg Whites':12,'Rice':3}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==3:
            print('Wednesday- Biceps & Triceps')
            print('Warm up-DB CURLS- 3sets- 15reps')
            print('BARBELL CURLS- 5sets- 12reps')
            print('BARBELL CLOSE GRIP PRESS- 3sets- 12reps')
            print('DB HAMMER CURL- 3sets- 12reps ')
            print('These are your daily meals')
            meal1={'QUINOA ':7,'Apple':0,'Walnuts':2}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={' WHEY ':18,'Banana':0,'milk':8}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            meal3={'Whole eggs':6,'Egg Whites':12,'Rice':3}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==4:
            print('Thursday- Chest')
            print('Warm up-PUSH-UPS- 3sets- 15reps')
            print('BARBELL BENCH PRESS- 3sets- 12reps ')
            print('DB FLY ON FLAT BENCH- 3sets- 12reps ')
            print('These are your daily meals')
            meal1={'QUINOA ':7,'Apple':0,'Walnuts':2}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={' WHEY ':18,'Banana':0,'milk':8}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            meal3={'Whole eggs':6,'Egg Whites':12,'Rice':3}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==5:
            print('Friday- Legs')
            print('BODY SQUAT- 3sets- 15reps')
            print('BARBELL SQUAT- 3sets- 12reps ')
            print('DB DEADLIFT- 3sets- 12reps')
            print('These are your daily meals')
            meal1={'QUINOA ':7,'Apple':0,'Walnuts':2}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={' WHEY ':18,'Banana':0,'milk':8}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            meal3={'Whole eggs':6,'Egg Whites':12,'Rice':3}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==6:
            print('Saturday- Cardio & Abs')
            print('TREADMILL OR CYCLING- 30mins- 10km speed')
            print('INCLINE CRUNCHES- 3sets- 15reps')
            print('ROPE CRUNCHES- 3sets- 15reps')
            print('HANGING LEG RAISE- 3sets- 15reps')
            print('These are your daily meals')
            meal1={'QUINOA ':7,'Apple':0,'Walnuts':2}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={' WHEY ':18,'Banana':0,'milk':8}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            meal3={'Whole eggs':6,'Egg Whites':12,'Rice':3}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        else:
            print('Sunday- Rest')
            print('These are your daily meals')
            meal1={'QUINOA ':7,'Apple':0,'Walnuts':2}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={' WHEY ':18,'Banana':0,'milk':8}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            meal3={'Whole eggs':6,'Egg Whites':12,'Rice':3}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        

elif choice==2:
    print('You are healthy dont come from tomorrow ')
elif choice==3:
    print('You can follow one of these programes')
    print('1.Muscular 8')
    print('2.6 Week Shredded')
    choice=int(input('SO which programe would you like to follow?'))
    if choice==1:
        print('WELCOME TO MUSCULAR 8, LETS DO IT ')
        print('Your workout is split in this manner:')
        print('1.Monday- Chest & Cardio')
        print('2.Tuesday- Arms, Abs & Cardio')
        print('3.Back & Cardio')
        print('4.Thursday- Abs & Cardio')
        print('5.Friday- Shoulders & Cardio')
        print('6.Saturday- Legs, Abs & Cardio')
        print('7.Sunday- Rest')
        choice=int(input('Select your todays workout:'))
        if choice==1:
            print('Monday- Chest & Cardio')
            print('Brbell press-3sets-15reps')
            print('Dumbell decline press-3sets-15reps')
            print('Cable crossove-3sets-15reps')
            print('These are your daily meals')
            meal1={'6 eggs whites':36,'1/2 kidney beans':4,'3sp peanuts':8}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'100g grilled chicken':20,'30g sweet potato':5,'1/2 cup green beans':4}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'120g grilled chicken':30,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==2:
            print('Tuesday- Arms, Abs & Cardio')
            print('Cable overhead ext-3sets-15reps')
            print('DB Curl-3sets-15reps')
            print('DB decline press-3sets-15reps')
            print('These are your daily meals')
            meal1={'6 eggs whites':36,'1/2 kidney beans':4,'3sp peanuts':8}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'100g grilled chicken':20,'30g sweet potato':5,'1/2 cup green beans':4}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'120g grilled chicken':30,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
           
        elif choice==3:
            print('Back & Cardio')
            print('Pull ups-2sets-15reps')
            print('Close grip lat pull down-3sets-15reps')
            print('Cable lat pull down-3sets-15reps')
            print('Stationary bike-20mins-10level')
            print('These are your daily meals')
            meal1={'6 eggs whites':36,'1/2 kideny beans':4,'3sp peanuts':8}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'100 grilled chicken':20,'30g sweet potato':5,'1/2 cup green beans':4}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'120g grilled chicken':30,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[keys])
            print(sum(protein))
        elif choice==4:
            print('Thursday- Abs & Cardio')
            print('Decline sit ups-3sets-15reps')
            print('Reverse crunches')
            print('Hanging knee raises')
            print('Running')
            print('Thses are your daily meals')
            meal1={'6 eggs whites':36,'1/2 kideny beans':4,'3sp peanuts':8}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'100 grilled chicken':20,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'120g grilled chicken':30,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal3)
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==5:
            print('Friday- Shoulders & Cardio')
            print('Barbell front press-3sets-15reps')
            print('Barbell behind the neck press-3sets-15reps')
            print('Wide grip upright rows-3sets-15reps')
            print('Elliptical-20mins-12kmph')
            print('These are your daily meals')
            meal1={'6 eggs whites':36,'1/2 kideny beans':4,'3sp peanuts':8}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'100 grilled chicken':20,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'120g grilled chicken':30,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal3)
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==6:
            print('aturday- Legs, Abs & Cardio')
            print('Leg press-3sets-15reps')
            print('Reverse lunges-3sets-15reps')
            print('Sumo deadlift-3sets-15reps')
            print('Stationary bike-20mins-12level')
            print('These are your daily meals')
            meal1={'6 eggs whites':36,'1/2 kideny beans':4,'3sp peanuts':8}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'100 grilled chicken':20,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'120g grilled chicken':30,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal3)
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        else:
            print('Sunday- Rest')
            print('These are your daily meals')
            meal1={'6 eggs whites':36,'1/2 kideny beans':4,'3sp peanuts':8}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'100 grilled chicken':20,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'120g grilled chicken':30,'2 Whole eggs':12,'2 Eggs whites':12}
            print(meal3)
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
    if choice==2:
        print('WELCOME TO 6 WEEK SHREDDED PROGRAME')
        print('Your workout is split in this manner:')
        print('1.Monday- Shoulders+Triceps, Upper abs')
        print('2.Tuesday-Chest, Upper back+Lower abs')
        print('3.Wenesday-Upper abs')
        print('4.Thursday-Lat, Mid back+Biceps, Lower abs')
        print('5.Friday-Quads, Ham & Calves, Upper abs')
        print('6.Saturday-Cardio, Lower abs')
        print('7.Sunday-Recovery')
        choice=int(input('Select your schedule:'))
        if choice==1:
            print('Monday- Shoulders+Triceps, Upper abs')
            print('DB shoulder press-3sets-15,12,10reps')
            print('DB Side raise-3sets-12,10,10reps')
            print('Cable front raise-3sets-12,10,10reps')
            print('DB front raise-10,10,10reps')
            print('These are your daily meals:')
            meal1={'2Slice wheat bread-':4,'200ml milk':10,'1 multi vitamines':10}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'Fresh juice':4,'1 Cup roasted channa':6}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'Paneer sandwich':10}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==2:
            print('Tuesday-Chest, Upper back+Lower abs')
            print('DB inclined press-3sets-12,12,8reps')
            print('Cable fly-3sets-12,10,8reps')
            print('Incline cable fly-3sets-12,10,8reps')
            print('These are your daily meals:')
            meal1={'2Slice wheat bread-':4,'200ml milk':10,'1 multi vitamines':10}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'Fresh juice':4,'1 Cup roasted channa':6}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'Paneer sandwich':10}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==3:
            print('Wenesday-Upper abs')
            print('HIIC tredmill-20mins')
            print('These are your daily meals:')
            meal1={'2Slice wheat bread-':4,'200ml milk':10,'1 multi vitamines':10}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'Fresh juice':4,'1 Cup roasted channa':6}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'Paneer sandwich':10}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==4:
            print('Thursday-Lat, Mid back+Biceps, Lower abs')
            print('Close grip lat pull down-3sets-125,10,8reps')
            print('DB rows-3sets-15,10,8reps')
            print('Cable curl-3sets-12,10,8reps')
            print('These are your daily meals:')
            meal1={'2Slice wheat bread-':4,'200ml milk':10,'1 multi vitamines':10}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'Fresh juice':4,'1 Cup roasted channa':6}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'Paneer sandwich':10}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==5:
            print('Friday-Quads, Ham & Calves, Upper abs')
            print('DB squat-3sets-15,10,8reps')
            print('DB lunges-3sets-15,108reps')
            print('Calf raise-3sets-12,10,8reps')
            print('These are your daily meals:')
            meal1={'2Slice wheat bread-':4,'200ml milk':10,'1 multi vitamines':10}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'Fresh juice':4,'1 Cup roasted channa':6}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'Paneer sandwich':10}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        elif choice==6:
            print('Saturday-Cardio, Lower abs')
            print('Incline crunches-3sets-20reps')
            print('Incline twist-3sets-20reps')
            print('Standing rope crunches-3sets-20reps')
            print('These are your daily meals:')
            meal1={'2Slice wheat bread-':4,'200ml milk':10,'1 multi vitamines':10}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'Fresh juice':4,'1 Cup roasted channa':6}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'Paneer sandwich':10}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
        else:
            print('Sunday-Recovery')
            print('These are your daily meals:')
            meal1={'2Slice wheat bread-':4,'200ml milk':10,'1 multi vitamines':10}
            print(meal1)
            protein=[]
            for key in meal1.keys():
                protein.append(meal1[key])
            print(sum(protein))
            meal2={'Fresh juice':4,'1 Cup roasted channa':6}
            print(meal2)
            protein=[]
            for key in meal2.keys():
                protein.append(meal2[key])
            print(sum(protein))
            meal3={'Paneer sandwich':10}
            print(meal3)
            protein=[]
            for key in meal3.keys():
                protein.append(meal3[key])
            print(sum(protein))
            
            
        
            
            
            
            
        
        
            
            
            
    
        
