def split_text_file(file_path):
    try:
        # Read the contents of the file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Calculate the split point
        total_lines = len(lines)
        split_index = int(total_lines / 2)

        # Split the lines into two parts
        first_half = lines[:split_index]
        second_half = lines[split_index:]

        # Write the first part to a new file
        with open("first_half.txt", "w") as file:
            file.writelines(first_half)

        # Write the second part to a new file
        with open("second_half.txt", "w") as file:
            file.writelines(second_half)

        print("Splitting of the file is complete. Check 'first_half.txt' and 'second_half.txt'.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    file_path = input("Enter the path of the text file to split: ")
    split_text_file(file_path)


if __name__ == "__main__":
    main()
