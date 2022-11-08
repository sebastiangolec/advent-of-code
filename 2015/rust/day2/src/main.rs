use std::{fs, cmp};

fn main() {
    let input = fs::read_to_string("src/input.txt").unwrap();
    let mut needed_paper = 0;
    let mut needed_ribbon = 0;
    for line in input.split_whitespace() {
        let present = Present::create(line);
        needed_paper += present.needed_paper();
        needed_ribbon += present.needed_ribbon();
    }
    println!("Needed paper: {needed_paper}");
    println!("Needed ribbon: {needed_ribbon}");
}

struct Present {
    l: u32,
    w: u32,
    h: u32
}

impl Present {
    fn create(input: &str) -> Self {
        // Splits provided input
        // Parses given values to integer numbers
        // Sorts in order to get smallest values
        let dimensions: Vec<&str> = input.split('x').collect();
        let mut dimensions: Vec<u32> = dimensions.iter().map(|f| f.parse::<u32>().unwrap()).collect();
        dimensions.sort();
        
        Present {
            l: *dimensions.get(0).unwrap(),
            w: *dimensions.get(1).unwrap(),
            h: *dimensions.get(2).unwrap()
        }
    }

    fn needed_paper(&self) -> u32 {
        let sides: (u32, u32, u32) = (self.l * self.w, self.w * self.h, self.h * self.l);
        let mut smallest_side = sides.0;
        smallest_side = smallest_side.min(sides.1);
        smallest_side = smallest_side.min(sides.2);

        (2 * sides.0) + (2 * sides.1) + (2 * sides.2) + smallest_side
    }

    fn needed_ribbon(&self) -> u32 {
        let bow = self.l * self.w * self.h;
        let wrap = (2 * self.l) + (2 * self.w);

        wrap + bow
    }
}
