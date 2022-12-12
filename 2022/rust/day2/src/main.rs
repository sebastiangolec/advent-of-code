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

        if my_move == "X" {
            score += 1;
        } else if my_move == "Y" {
            score += 2;
        } else {
            score += 3;
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

    if enemy_move == "A" { 
        if my_move == "X" {
            score = 3;
        } else if my_move == "Y" {
            score = 6;
        } else {
            score = 0; 
        }
    } else if enemy_move == "B" {
        if my_move == "X" {
            score = 0
        } else if my_move == "Y" {
            score = 3;
        } else {
            score = 6;
        }
    } else if enemy_move == "C" {
        if my_move == "X" {
            score = 6;
        } else if my_move == "Y" {
            score = 0;
        } else {
            score = 3
        }
    }

    return score;
}
