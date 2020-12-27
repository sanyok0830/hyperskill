import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()
pipec = True
payment = args.payment
if payment!=None:
    if int(payment) < 0:
        pipec = False

principal = args.principal
if principal!=None:
    if  int(principal) < 0:
        pipec = False

periods = args.periods
if periods!=None:
    if  int(periods) < 0:
        pipec = False

interest =args.interest
if interest!=None:
    if float(interest) < 0:
        pipec = False

args = parser.parse_args()
if pipec == False:
    print("Incorrect parameters")

elif  args.type==None:
    print("Incorrect parameters")

elif  (args.principal==None and args.periods==None) or (args.principal==None and args.payment==None) or (args.periods==None and args.payment==None):
    print("Incorrect parameters")

elif args.type =="annuity":
    if interest==None:
        print("Incorrect parameters")
    else:
        def number_of_monthly_payments(payment, interest,principal):   #  correct
            nominal_rate = float(interest)/1200
            month = math.ceil(math.log(int(payment)/(int(payment) - nominal_rate*int(principal)), 1+nominal_rate))
            print(month)
            if month == 1:
                print("It will take", round(month), "month to repay the loan!")
            else:
                if month == 12:
                    print("It will take", round(month/12), "year to repay the loan!")
                elif month < 12:
                    print("It will take", round(month), "months to repay the loan!")
                elif month%12 == 0 and month!=12:
                    print("It will take", round(month / 12), "years to repay the loan!")
                elif month%12 != 0 and month > 12 and month-month//12*12!=1:
                    print("It will take", month // 12, "years and", (month-month//12*12), "months to repay the loan!")
                else:
                    print("It will take", month // 12, "years and", (month - month // 12 * 12), "month to repay the loan!")
            print("Overpayment = {}".format(month*int(payment)-int(principal)))

        def monthly_payment(principal, periods, interest ):
            nominal_rate = float(interest) / 1200
            annuity_payment = int(principal)*((nominal_rate * (1 + nominal_rate)**int(periods))/((1 + nominal_rate)**int(periods)-1))
            print("Your monthly payment = {}!".format(math.ceil(annuity_payment)))
            print("Overpayment = {}".format(math.ceil(annuity_payment)*int(periods) - int(principal)))


        def annuity_monthly_payment(payment, periods, interest ):
            loan_interest =  float(interest)/1200
            loan_principal = int(payment)/((loan_interest*((1+loan_interest)**int(periods)))/(((1+loan_interest)**int(periods))-1))
            print("Your loan principal = {}!".format(math.floor(loan_principal)))
            print("Overpayment = {}".format(math.ceil(int(payment)*int(periods) - loan_principal)))

        if args.principal==None:
            annuity_monthly_payment(payment, periods, interest )
        if args.periods==None:
            number_of_monthly_payments(payment, interest, principal)
        if args.payment==None:
            monthly_payment(principal, periods, interest )


elif args.type =="diff":
    if payment !=None or interest==None:
        print("Incorrect parameters")
    else:
        i = float(args.interest) / 1200
        count = 1
        pereplata = 0
        while count <= int(args.periods):
            payment = math.ceil(int(args.principal) / int(args.periods) + i * (int(args.principal) - (int(args.principal) * (count - 1)) / (int(args.periods))))
            print("Month {}: payment is {}".format(count, payment))
            pereplata+=payment
            count += 1
        print()
        print("Overpayment = {}".format(pereplata-int(args.principal)))



