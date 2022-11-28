use std::fs;
use std::collections::HashMap;

fn main() {
    let input = fs::read_to_string("./src/input.txt").unwrap();

    let houses_with_presents = part_1(&input);
    let houses_with_presents_2 = part_2(&input);
    println!("Houses with presents: {houses_with_presents}");
    println!("Houses with presents part 2: {houses_with_presents_2}");
}

fn part_1(input: &str) -> usize {
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

    map.iter().count()
}

fn part_2(input: &str) -> usize {
    let mut santa = (0, 0);
    let mut robo_santa = (0, 0);
    let mut map: HashMap<(i32, i32), u32> = HashMap::new();

    map.entry(santa)
        .and_modify(|presents| *presents += 1)
        .or_insert(1);
    map.entry(robo_santa)
        .and_modify(|presents| *presents += 1)
        .or_insert(1);

    let mut turn = true;

    for char in input.chars() {
        let mut pointer: &mut (i32, i32);

        if turn {
            pointer = &mut santa;
        } else {
            pointer = &mut robo_santa;
        }

        match char {
            '<' => pointer.0 -= 1,
            '>' => pointer.0 += 1,
            'v' => pointer.1 -= 1,
            '^' => pointer.1 += 1,
            _ => ()
        }

        map.entry(*pointer)
            .and_modify(|presents| *presents += 1)
            .or_insert(1);
        
        turn = !turn;
    }

    map.iter().count()
}