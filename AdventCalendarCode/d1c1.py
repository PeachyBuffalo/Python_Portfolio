import day1challenge1.txt as d1c1

# Function to extract first and last digit from each line
def extract_first_last_digit(text):
    lines = text.strip().split("\n")
    result = []
    for line in lines:
        first_digit = re.search(r'\d', line)
        last_digit = re.search(r'\d(?![^\d]*\d)', line)
        if first_digit and last_digit:
            result.append((line, first_digit.group(), last_digit.group()))
        else:
            result.append((line, None, None))
    return result

# Applying the function to each chunk
result = extract_first_last_digit(d1c1)

# Combining results
combined_results = result_1 + result_2 + result_3
combined_results[:10]  # Display first 10 results for brevity