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

    // Create regex pattern for mul(x,y), do(), and don't()
    let pattern = Regex::new(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))").unwrap();

    // Process all matches
    let mut total = 0;
    let mut mul_enabled = true;

    for cap in pattern.captures_iter(&content) {
        if let Some(full_match) = cap.get(0) {
            let match_str = full_match.as_str();
            
            if match_str.starts_with("do()") {
                mul_enabled = true;
            } else if match_str.starts_with("don't()") {
                mul_enabled = false;
            } else if match_str.starts_with("mul") {
                if mul_enabled {
                    if let (Some(x), Some(y)) = (cap.get(2), cap.get(3)) {
                        if let (Ok(x_num), Ok(y_num)) = (x.as_str().parse::<i32>(), y.as_str().parse::<i32>()) {
                            total += x_num * y_num;
                        }
                    }
                }
            }
        }
    }

    println!("{}", total);
    Ok(())
} 