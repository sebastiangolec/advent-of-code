use std::fs;

fn main() {
    let input = fs::read_to_string("src/input.txt").unwrap();
    let mut total_score = 0;

    for line in input.lines() {
        let characters: Vec<&str> = line.split(' ').collect();
        let mut score = 0;

        let my_move = *characters.get(1).unwrap();
        let enemy_move = *characters.get(0).unwrap();
        score += calculate_result(enemy_move, my_move);

        match my_move {
            "X" => score += 1,
            "Y" => score += 2,
            _ => score += 3
        }

        total_score += score;
    }

    print!("{total_score}");
}

// 'A'/'X' - rock
// 'B'/'Y' - paper
// 'C'/'Z' - scissors
fn calculate_result(enemy_move: &str, my_move: &str) -> u32 {
    let mut score = 0;

    match enemy_move {
        "A" => {
            match my_move {
                "X" => score = 3,
                "Y" => score = 6,
                _ => score = 0
            }
        },
        "B" => {
            match my_move {
                "X" => score = 0,
                "Y" => score = 3,
                _ => score = 6
            }
        },
        "C" => match my_move {
            "X" => score = 6,
            "Y" => score = 0,
            _ => score = 3
        },
        _ => score = 0
    }

    return score;
}
