import argparse
import os

def to_character_sequence(tokenized_text: str) -> str:
    if not tokenized_text.strip():
        return ""

    # 1. Prepare the sequence: replace spaces between tokens with the ' SPACE ' marker.
    # We use strip() to handle leading/trailing whitespace gracefully.
    temp_sequence = tokenized_text.strip().replace(' ', ' SPACE ')

    # 2. Iterate through the string, separating every character/symbol.
    char_sequence = []
    for char in temp_sequence:
        if char != ' ':
            char_sequence.append(char)
            char_sequence.append(' ')
        else:
            char_sequence.append(char)
            
    # 3. Join the list and remove any trailing space.
    return "".join(char_sequence).strip()


def convert_file(input_path: str, output_path: str):
    """Reads a file, converts each line (sentence) to a character sequence, and writes to an output file."""
    
    print(f"Processing input file: {input_path}")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            sentences = infile.readlines()
        
        output_sentences = []
        for line in sentences:
            # The line is expected to be in the tokenized format, e.g., "I am go home ."
            char_seq = to_character_sequence(line)
            if char_seq:
                output_sentences.append(char_seq)

        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write('\n'.join(output_sentences) + '\n')
            
        print(f"Successfully wrote {len(output_sentences)} lines to: {output_path}")

    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert tokenized text file to character sequence format."
    )
    parser.add_argument(
        '--input', dest='inp', required=True, help="Path to the input file (tokenized format)."
    )
    parser.add_argument(
        '--output', dest='out', required=True, help="Path to the output file (character sequence format)."
    )
    args = parser.parse_args()
    
    # Ensure the output directory exists before writing
    output_dir = os.path.dirname(args.out)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    convert_file(args.inp, args.out)


if __name__ == '__main__':
    main()