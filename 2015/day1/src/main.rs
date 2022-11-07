use std::fs;
fn main() {
    let input = fs::read_to_string("src/input.txt").unwrap();
    let mut counter = 0;
    for char in input.chars() {
        match char {
            '(' => counter += 1,
            ')' => counter -= 1,
            _ => counter += 0
        }
    }
    println!("{counter}");
}
