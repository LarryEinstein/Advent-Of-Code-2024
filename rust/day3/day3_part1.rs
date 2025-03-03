use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use regex::Regex;

fn main() -> io::Result<()> {
    // Read the input file
    let path = Path::new("python/day3/day3_input.txt");
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    // Read the entire content as a string
    let content: String = reader.lines()
        .filter_map(|line| line.ok())
        .collect::<Vec<String>>()
        .join("\n");

    // Create regex pattern for mul(x,y)
    let pattern = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    // Find all matches and calculate total
    let mut total = 0;
    for cap in pattern.captures_iter(&content) {
        if let (Some(x), Some(y)) = (cap.get(1), cap.get(2)) {
            if let (Ok(x_num), Ok(y_num)) = (x.as_str().parse::<i32>(), y.as_str().parse::<i32>()) {
                total += x_num * y_num;
            }
        }
    }

    println!("{}", total);
    Ok(())
} 