
use std::{fs, ops::Add};

fn main() {
    let input = fs::read_to_string("src/input.txt").unwrap();
    let mut elves: Vec<i32> = Vec::new();

    let mut sum = 0;
    for line in input.lines() {
        if line.is_empty() {
            elves.push(sum);
            sum = 0;
        } else {
            let value: i32 = line.parse().unwrap();
            sum = sum + value;
        }
    }

    elves.sort();
    let mut most_calories_elf = elves.pop();
    let most_calories_elf = *most_calories_elf.get_or_insert(0);
    println!("{most_calories_elf}");

    let mut second_most_calories_elf = elves.pop();
    let second_most_calories_elf = *second_most_calories_elf.get_or_insert(0);

    let mut third_most_calories_elf = elves.pop();
    let third_most_calories_elf = *third_most_calories_elf.get_or_insert(0);
    let top3_answer = most_calories_elf.add(second_most_calories_elf).add(third_most_calories_elf);
    println!("{top3_answer}");
}
