keep_running = True
while keep_running == True:
    uppercase = str(input("escreva algo em maiúsculo: "))
    if uppercase.isdigit():
        print(f"{uppercase} e você digitou um número, não uma letra maiúscula.")
        keep_running = True
    
    elif uppercase.isupper():
        print(f"digite dessa forma: '{uppercase.lower()}', pois não existem motivos para você estar gritando.")
        keep_running = False
        