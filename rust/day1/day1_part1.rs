use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    // Read the input file
    let path = Path::new("python/day1/day1_input.txt");
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    // Store numbers from each column
    let mut numbers_col1: Vec<i32> = Vec::new();
    let mut numbers_col2: Vec<i32> = Vec::new();

    // Read and parse each line
    for line in reader.lines() {
        if let Ok(line) = line {
            let numbers: Vec<i32> = line
                .split_whitespace()
                .map(|s| s.parse().unwrap())
                .collect();
            
            if numbers.len() == 2 {
                numbers_col1.push(numbers[0]);
                numbers_col2.push(numbers[1]);
            }
        }
    }

    // Sort both lists
    numbers_col1.sort();
    numbers_col2.sort();

    // Calculate total difference
    let mut total_difference = 0;
    for i in 0..numbers_col1.len() {
        total_difference += (numbers_col1[i] - numbers_col2[i]).abs();
    }

    println!("Total difference = {}", total_difference);
    Ok(())
} 