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

fn is_safe_with_one_removal(report: &[i32]) -> bool {
    // Check if already safe without removal
    if is_safe(report) {
        return true;
    }

    // Try removing each level once and check if the resulting report is safe
    for i in 0..report.len() {
        let modified_report: Vec<i32> = report.iter()
            .enumerate()
            .filter(|&(j, _)| j != i)
            .map(|(_, &x)| x)
            .collect();
        if is_safe(&modified_report) {
            return true;
        }
    }

    false
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

    // Count how many reports are safe with one possible removal
    let safe_count_with_removal = data_as_rows.iter()
        .filter(|row| is_safe_with_one_removal(row))
        .count();
    println!("{}", safe_count_with_removal);

    Ok(())
} 