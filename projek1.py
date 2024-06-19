import time
print("**************************************************")
#Welcome the user
print("SELAMAT DATANG KE KUIZ BAHASA MELAYU!")
time.sleep(1)
print("**************************************************")

#Chances
chances=1
print("SILA BERIKAN JAWAPAN ANDA.", chances,"JAWAPAN YANG BETUL.\n1 MARKAH AKAN DIBERIKAN SEKIRANYA JAWAPAN ANDA BETUL.\n")
time.sleep(2)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) CONTOH KATA NAMA KECUALI?\n(A) KUCING\n(B) BENCI\n(C) RINDU\n(D) SAYANG\n\n")
answer_1= "a"

for i in range(chances):
    answer = input("Jawapan: ")
    if (answer.lower() == answer_1):
        print("BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2)BERIKAN CONTOH KATA ADJEKTIF?\n(A) MASAK\n(B) LARI\n(C) RINDU\n(D) NYANYI\n\n")  
answer_2 = "c"

for i in range(chances):
    answer = input("Jawapan: ")
    if (answer.lower() == answer_2):
        print("BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("KURANG TEPAT!\n ")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3)  BERIKAN CONTOH KATA KERJA\n(A) LEBAH\n(B) PASRAH\n(C) MARAH\n(D) LOMPAT\n\n")
answer_3= "d"

for i in range(chances):
    answer = input("Jawapan: ")
    if (answer.lower() == answer_3):
        print("BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("KURANG TEPAT!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4)  BERIKAN CONTOH KATA HUBUNG?\n(A) DAN\n(B) IALAH\n(C) ADALAH\n(D) PADA\n\n")
answer_4= "a"

for i in range(chances):
    answer = input("Jawapan: ")
    if (answer.lower() == answer_4):
        print("BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("KURANG TEPAT!\n")
        time.sleep(0.5)
        print("JAWAPANNYA IALAH",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  KATA PEMERI TERDIRI DARIPADA PERKATAAN?\n(A) IALAH\n(B) IALAH DAN ADALAH\n(C) ADALAH\n(D) HANYALAH\n\n")
answer_5= "b"

for i in range(chances):
    answer = input("Jawapan: ")
    if (answer.lower() == answer_5):
        print("BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("MAAF, KURANG TEPAT!\n")
        time.sleep(0.5)
        print("JAWAPANNYA IALAH ", answer_5, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
while score >=2:
    print("BAGUS! MARKAH ANDA IALAH", score)
    break

while score <2:
    print("SEMOGA BERJAYA! MARKAH ANDA IALAH",score)
    break

#Goobye message
print("TERIMA KASIH KERANA MENYERTAI KUIZ INI!")

print("==================================================")