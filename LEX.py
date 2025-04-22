import re
def analyze_text(text):
    char_count = len(text)
    word_count = len(re.findall(r'\b\w+\b', text))
    sentence_count = len(re.findall(r'[.!?]', text))
    line_count = text.count('\n') + 1
    tab_count = text.count('\t')
    number_count = len(re.findall(r'\b\d+\b', text))
    space_count = text.count(' ')
    print(f"Character Count: {char_count}")
    print(f"Word Count: {word_count}")
    print(f"Sentence Count: {sentence_count}")
    print(f"Line Count: {line_count}")
    print(f"Tab Count: {tab_count}")
    print(f"Number Count: {number_count}")
    print(f"Space Count: {space_count}")
text = input("Enter your text:\n")
analyze_text(text)
