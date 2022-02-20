#coding:utf-8
#Copyright © 2022 df.ぽん. All Rights Reserved.
character_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
encrypted_character_list=["1q","0h","5w","8v","4c","9d","7l","4w","8a","6z","3k","7s","5p","9j","1x","3h","4f","9p","8q","0r","3t","7r","9e","0n","8q","1j","9k"]
def main():
    print("\n-----暗号・復号装置-----\n暗号の場合は1を、復号の場合は2を半角数字で入力してください。\n")
    mode_select=input("Mode>>")
    if mode_select=="1":
        print("\n暗号化したい文章を半角英字or空白のみで入力してください。\n")
        c_=input("Sentence>>")
        length=len(c_)
        after_c=""
        for i in range(length):
            if (c_[i] in character_list)==False:
                print("半角英字と空白以外が検出されました。最初からやり直してください。")
                main()
            else:
                pass
        for i in range(length):
            after_c+=encrypted_character_list[character_list.index(c_[i])]
        print("\n暗号結果:{}".format(after_c))
    elif mode_select=="2":
        print("\n復号化したい文章を入力してください。\n")
        a_=input("Sentence>>")
        length=len(a_)
        after_a=""
        for i in range(length//2):
            if (a_[i*2-2]+a_[i*2-1] in encrypted_character_list)==False:
                print("この装置で作られていない暗号文の可能性があります。最初からやり直してください。")
                main()
            else:
                pass
        for i in range(length//2):
            after_a+=character_list[encrypted_character_list.index(a_[i*2-2]+a_[i*2-1])]
        print("\n復号結果:{}".format(after_a[1:]+after_a[0]))
    else:
        main()
if __name__=="__main__":
    main()