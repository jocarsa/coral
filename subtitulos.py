def clean_srt_to_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as srt_file:
        lines = srt_file.readlines()
    
    cleaned_lines = []
    for line in lines:
        # Remove lines that are numbers or contain time markers
        if line.strip().isdigit() or '-->' in line:
            continue
        # Add non-empty, non-timestamp lines to cleaned_lines
        cleaned_line = line.strip()
        if cleaned_line:
            cleaned_lines.append(cleaned_line)

    # Combine all text into a single string
    plain_text = ' '.join(cleaned_lines)

    # Write to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(plain_text)

# Example usage
input_srt = 'example.srt'  # Replace with your input SRT file
output_txt = 'output.txt'  # Replace with your desired output file
clean_srt_to_text(input_srt, output_txt)

print(f"Plain text has been written to {output_txt}")
