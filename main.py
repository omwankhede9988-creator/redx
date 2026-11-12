import time

print("---------------------------------------------")
print("  REDX AI Assistant - Online & Secure")
print("  Status: All Systems Normal. Ready for Action.")
print("---------------------------------------------")

while True:
    command = input("Aapka Hukam kya hai, Om? -> ")
    
    if "exit" in command.lower() or "band karo" in command.lower():
        print("REDX: Systems shutting down. Alvida, Om!")
        break
    elif "hello" in command.lower() or "hi" in command.lower():
        print("REDX: Hello Om! Main aapka personal assistant REDX hoon. Bataiye kya madad karun?")
    else:
        print(f"REDX: '{command}' par kaam chal raha hai. Jaldi hi yeh feature bhi jud jayega!")
    
    print("-" * 40)
