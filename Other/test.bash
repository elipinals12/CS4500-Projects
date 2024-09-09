#!/bin/bash

# Set the maximum index for testing
max_index=$1  # Pass the maximum index as an argument to the script

# Loop through each test case
for i in $(seq 0 $max_index); do
    input_file="../Tests/${i}-in.json"
    expected_output_file="../Tests/${i}-out.json"
    temp_output_file="../Tests/temp-${i}-output.json"

    # Check if both input and expected output files exist
    if [[ -f $input_file && -f $expected_output_file ]]; then
        # Run the Python script with the input file and store the output
        py ../main.py < "$input_file" > "$temp_output_file"

        # Compare the output with the expected output
        if cmp -s "$temp_output_file" "$expected_output_file"; then
            echo "Test $i Passed: Output matches $expected_output_file"
        else
            echo "Test $i Failed: Output does not match $expected_output_file"
            echo "Differences:"
            diff "$temp_output_file" "$expected_output_file"
        fi

        # # Optionally, remove the temporary output file
        # rm "$temp_output_file"
    else
        echo "Test $i Skipped: $input_file or $expected_output_file not found"
    fi
done
