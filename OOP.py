print("\n\n\n")
print("WELCOME TO XYZ BLOOD DONATION Service Centre")
print("\n    This Is A Login Portal\n\n")
print("Please follow the given instructions in order to log in")
print("\nFOR ADMIN LOGIN: PRESS A")
print("FOR USER LOGIN : PRESS a")
q=int(input())

class donor:
  x=0 #for counting no. of donors
  def init(self,name,age,sex,blood_group,platelets_count,wbc_count,rbc_count):
    self.name=name
    self.age=age
    self.sex=sex
    self.blood_group=blood_group
    self.platelets_count=platelets_count
    self.wbc_count=wbc_count
    self.rbc_count=rbc_count
    donor.x+=1

    
donor_1=donor('ROCKEY',30,'MALE','A+',200234,34768,54678)
donor_2=donor('LOGAN',50,'MALE','AB-',203456,36758,56780)
donor_3=donor('MARTIN',32,'MALE','O+',345670,45678,36987)
donor_4=donor('RONNEY',37,'MALE','B-',354678,67547,45691)
donor_5=donor('ALITA',41,'FEMALE','A+',321432,56543,56764)
donor_6=donor('RIO',48,'MALE','A-',265439,45654,65478) 
donor_7=donor('JENNIFER',69,'FEMALE','A+',234188,45678,65785)
donor_8=donor('DEXTER',26,'MALE','A+',267554,45694,56543)
donor_9=donor('PETER',30,'MALE','AB+',265354,46614,52743)
donor_10=donor('CHAUBEY',60,'MALE','A+',267462,45204,56783) 


def blood_banks():
  print("\n\nFollowing blood banks are avalable near you: ")
  print("\n\n1. Mysore Blood Bank")
  print("\n2. Diagnostic labrotary ")
  print("\n3.  Ex- servicemen Blood Bank")
  print("\n4. NIKE Blood Bank")
  print("\n5. HKES Blood Bank")
  print("\n6. Mysore Baptist Hospital and  Blood Bank")


def rare_blood_groups():
  print("\nDonors with rare blood groups and their details are listed below: ")
  print("\nNAME       AGE         SEX           BLOOD_GROUP\n")
  print("Rockey       30         MALE           AB-\n")
  print("Martin       32         MALE         O+\n")
  print("Ronney       37         MALE         B-\n")
  print("Chaubey      60         MALE           AB+\n")

if q==1:
  print("\n\n-------------------- Welcome Admin ---------------------\n")
  w=input("Please enter your username: ")
  w.lower()
  if w=='Harshita':
    b=input("\nUsername found!\n\n Please enter your password: ")  
    b.lower()
    if b=='password':
      print("\nSigned In successfully!")
      print("\n\n-------------Hello Admin we kindly Welcome you-----------------")
      print("\n\nTell me what you want to know")
      print("\n1. Details of the Donors")       #Only admins can know the details of the donors
      print("\n2. Details of the Blood Banks")
      print("\n3. Details of the donors with rare blood groups")
      a=int(input("\n\nEnter a choice from the above: "))
      if a==1:
        l1=[donor_1,donor_2,donor_3,donor_4,donor_5,donor_6,donor_7,donor_8,donor_9,donor_10]
        for f in l1:
          print("\n")
          print(f.dict)
      elif a==2:
        blood_banks()
      elif a==3:
        rare_blood_groups()
      else:
        print("\nInvalid Choice!")
    else:
      print("\nPassword doesn't match!")
  
  else:
    print("\nAdmin not found. Please enter the correct Username")

elif q==2:
  print("\n\n-------------------- Welcome User ---------------------\n")
  w=input("Please enter your username: ")
  w.lower()
  if w=='ramesh' or 'ronit' or 'appu' or 'milan' or 'amin':
    b=input("\nUsername found!\n\n Please enter your password: ")  
    b.lower()
    if b=='password':
      print("\nSigned In successfully!")
      print("\n\n-------------Hello User Welcome -----------------")
      print("\n\nTell me what you want to know")
      print("\n1. Number of the Donors available")  #Users can only know the number of donors available and not their details
      print("\n2. Details of the Blood Banks")
      print("\n3. Details of the donors with rare blood groups")
      a=int(input("\n\nEnter a choice from the above: "))
      if a==1:
        print("\nTotal number of Donors avalable is: ",donor.x) #donor.x for counting the number of donors
      elif a==2:
        blood_banks()
      elif a==3:
        rare_blood_groups()
      else:
        print("\nInvalid Choice!")
    else:
        print("\nPassword doesn't match!")
  
  else:
    print("\nUser not found. Please enter the correct Username")

else:
  print("\nWrong Choice! Please enter from the above choice only")