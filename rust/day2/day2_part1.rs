use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn is_safe(report: &[i32]) -> bool {
    // Determine the direction: increasing or decreasing
    let first = report[0];
    let last = report[report.len() - 1];

    // If first == last, it can't be strictly increasing or decreasing
    if first == last {
        return false;
    }

    // Increasing if the last is greater than the first
    let increasing = last > first;

    // Check all adjacent differences
    for i in 0..report.len() - 1 {
        let diff = report[i + 1] - report[i];

        // If we expect increasing, diff should be positive; if decreasing, diff should be negative
        if increasing && diff <= 0 {
            return false;
        }
        if !increasing && diff >= 0 {
            return false;
        }

        // Check if the absolute difference is between 1 and 3
        if !(1..=3).contains(&diff.abs()) {
            return false;
        }
    }

    true
}

fn main() -> io::Result<()> {
    // Read the input file
    let path = Path::new("python/day2/day2_input.txt");
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    // Parse each line into a vector of integers
    let data_as_rows: Vec<Vec<i32>> = reader
        .lines()
        .filter_map(|line| {
            line.ok().map(|l| {
                l.split_whitespace()
                    .filter_map(|s| s.parse().ok())
                    .collect()
            })
        })
        .collect();

    // Count how many reports are safe
    let safe_count = data_as_rows.iter().filter(|row| is_safe(row)).count();
    println!("{}", safe_count);

    Ok(())
} 