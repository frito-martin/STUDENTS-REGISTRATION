class student:
    def __init__(self,name,registration_no,access_no,program,email,year,GPA):
        self.name=name
        self.registration_no=registration_no
        self.access_no=access_no
        self.program=program
        self.email=email
        self.year=year
        self.GPA=GPA

    def __str__(self):

        return(f"Name:{self.name}\n Registration_no:{self.registration_no}\n Access_no:{self.access_no}\n Program:{self.program}\n Email:{self.email}\n Year:{self.year}\n GPA:{self.GPA}\n")

Muzei=student("Muzei","m23b13/049","b21267","information_technology","muzei@gmail.com","2","4.5")
Kasozi=student("Kasozi","m20b13/005","A4567","computer_science","kasozi@gmail.com","3","3.9")
Kyakuwaire=student("Kyakuwaire","m29b14/011","j2234","development_study","kyas@gmail.com","1","3.7")
Okurut=student("Okurut","m11b12/055","A2316","engineering","okurut@gmail.com","2","3.5")
Eboru=student("Eboru","A23b34/120","S2367","social_work","eboru@gmail.com","1","2.9")
Nabukera=student("Nabukere","m23b11/900","j1122","nursing","nabukere@gmail.com","1","3.4")

print(Muzei)
print(Kasozi)
print(Kyakuwaire)
print(Okurut)
print(Eboru)
print(Nabukera)