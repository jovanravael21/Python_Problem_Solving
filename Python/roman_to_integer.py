# Roman Sysmbols List
romanSymbolsValue = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

# Roman Sysmbols Converter Function
def roman_Symblos_Converter(roman_Symbols_Value, input_User):
    # Listing the input symbols and symbols list
    listInput = list(input_User)
    listSysmbols = list(roman_Symbols_Value.keys())

    # Final Result
    finalOutcome = 0

    numsInput = len(input_User)
    # Checking input is in List
    for a in range (numsInput) :
        if listInput[a] not in listSysmbols :
            return "Error: input sysmbol is in correct"

    # Converting Symbols to Value & Sum Value
    for i in range (numsInput) :
        if i < numsInput-1:
            if listInput[i] == "I" and listInput[i+1] == "V":
                finalOutcome += (roman_Symbols_Value["V"] - roman_Symbols_Value["I"])          
            elif listInput[i] == "I" and listInput[i+1] == "X":
                finalOutcome += (roman_Symbols_Value["X"] - roman_Symbols_Value["I"])     
            elif listInput[i] == "X" and listInput[i+1] == "L":
                finalOutcome += (roman_Symbols_Value["L"] - roman_Symbols_Value["X"])             
            elif listInput[i] == "X" and listInput[i+1] == "C":
                finalOutcome += (roman_Symbols_Value["C"] - roman_Symbols_Value["X"])              
            elif listInput[i] == "C" and listInput[i+1] == "D":
                finalOutcome += (roman_Symbols_Value["D"] - roman_Symbols_Value["C"])               
            elif listInput[i] == "C" and listInput[i+1] == "M":
                finalOutcome += (roman_Symbols_Value["M"] - roman_Symbols_Value["C"])     
            else:
                finalOutcome += (2*roman_Symbols_Value[listInput[i]])

    return finalOutcome

# Getting input 
inputUser = input("Enter Your Roman Symbols: ")
print(roman_Symblos_Converter(romanSymbolsValue,inputUser))