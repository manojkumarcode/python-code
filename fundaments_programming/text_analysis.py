from fundaments_programming.test_analyzer import TextAnalyzer
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

textAnalyzer = TextAnalyzer(givenstring)
print(textAnalyzer.text)

frequency_map = textAnalyzer.freqAll()

print(frequency_map)

print(frequency_map.keys())

word = "lorem"
freq =  frequency_map.get(word)
print(f"freq of {word}=", freq)

signal_state = "Red"
if signal_state == "Green":
    print("Walk")
else:
    print("Wait")
print("Look both ways")

current_temp = 18
current_temp = current_temp > 25
print("current_temp:", current_temp)

remaining_percent = 100
while remaining_percent > 25:
    print(f"{remaining_percent}% remaining")
    remaining_percent = remaining_percent-25