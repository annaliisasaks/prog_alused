vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ")
tüüp = input("Sisestage treeningu tüüp: ")

m_1_min = round((220 - vanus) * 0.5)
m_1_max = round((220 - vanus) * 0.7)

m_2_min = m_1_max
m_2_max = round((220 - vanus) * 0.8)

m_3_min = m_2_max
m_3_max = round((220 - vanus) * 0.87)

n_1_min = round((206 - vanus * 0.88) * 0.5)
n_1_max = round((206 - vanus * 0.88) * 0.7)

n_2_min = n_1_max
n_2_max = round((206 - vanus * 0.88) * 0.8)

n_3_min = n_2_max
n_3_max = round((206 - vanus * 0.88) * 0.87)

if (sugu == "M" or sugu == "m") and tüüp == "1":
    print("Pulsisagedus peaks olema vahemikus " + str(m_1_min) + " kuni " + str(m_1_max) + ".")

elif (sugu == "M" or sugu == "m") and tüüp == "2":
    print("Pulsisagedus peaks olema vahemikus " + str(m_2_min) + " kuni " + str(m_2_max) + ".")

elif (sugu == "M" or sugu == "m") and tüüp == "3":
    print("Pulsisagedus peaks olema vahemikus " + str(m_3_min) + " kuni " + str(m_3_max) + ".")

elif (sugu == "N" or sugu == "n") and tüüp == "1":
    print("Pulsisagedus peaks olema vahemikus " + str(n_1_min) + " kuni " + str(n_1_max) + ".")

elif (sugu == "N" or sugu == "n") and tüüp == "2":
    print("Pulsisagedus peaks olema vahemikus " + str(n_2_min) + " kuni " + str(n_2_max) + ".")

elif (sugu == "N" or sugu == "n") and tüüp == "3":
    print("Pulsisagedus peaks olema vahemikus " + str(n_3_min) + " kuni " + str(n_3_max) + ".")
