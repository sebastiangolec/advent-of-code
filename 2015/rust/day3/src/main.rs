use std::fs;
use std::collections::HashMap;

fn main() {
    let input = fs::read_to_string("./src/input.txt").unwrap();
    let mut pointer = (0, 0);
    let mut map: HashMap<(i32, i32), u32> = HashMap::new();
    map.entry(pointer)
        .and_modify(|presents| *presents += 1)
        .or_insert(1);

    for char in input.chars() {
        match char {
            '<' => pointer.0 -= 1,
            '>' => pointer.0 += 1,
            'v' => pointer.1 -= 1,
            '^' => pointer.1 += 1,
            _ => ()
        }

        map.entry(pointer)
            .and_modify(|presents| *presents += 1)
            .or_insert(1);
    }

    let houses_with_presents = map.iter().count();
    println!("Houses with presents: {houses_with_presents}");
}