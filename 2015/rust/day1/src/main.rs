use std::fs;
fn main() {
    let input = fs::read_to_string("src/input.txt").unwrap();
    let mut counter = 0;
    let mut index = 1;
    
    for char in input.chars() {
        counter += match char {
            '(' => 1,
            ')' => -1,
            _ => 0
        };

        if counter == -1 {
            println!("Reaching basement at {index} character.");
        }

        index += 1;
    }
    println!("Destination floor is {counter}.");
}
