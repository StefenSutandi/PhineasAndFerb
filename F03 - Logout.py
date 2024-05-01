# F03 - Logout

def logout():
    global isLoggedOut
    if isLoggedOut == True :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else : # User login
        print("Anda telah logout dari akun")    
    isLoggedOut = True 

isLoggedOut = False