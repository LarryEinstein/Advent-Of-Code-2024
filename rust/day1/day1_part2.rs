use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashSet;

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

    // Sort and deduplicate first list
    numbers_col1.sort();
    let deduped_list1: Vec<i32> = numbers_col1.iter()
        .cloned()
        .collect::<HashSet<i32>>()
        .into_iter()
        .collect::<Vec<i32>>();
    deduped_list1.sort();

    // Calculate scalar difference
    let mut difference_scalar = 0;
    for num in deduped_list1 {
        let count = numbers_col2.iter().filter(|&&x| x == num).count();
        difference_scalar += num * count as i32;
    }

    println!("Final difference for advent = {}", difference_scalar);
    Ok(())
} 