acronyms = {
    "NASA": "National Aeronautics and Space Administration",
    "FBI": "Federal Bureau of Investigation",
    "CIA": "Central Intelligence Agency",
    "UN": "United Nations",
    "WHO": "World Health Organization",
    "IDN": "I don't know",
    "TBH": "to be honest"
}

acronyms["CIA2"] = 'Central Intelligence Agency Station'
del acronyms["CIA"]

defination = acronyms["CIA2"]
translation = acronyms["IDN"] + ' what happened ' + acronyms["WH"]

if translation:
    print(translation)
else:
    print("Definition does not exist.")