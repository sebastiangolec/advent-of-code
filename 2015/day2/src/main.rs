use std::fs;

fn main() {
    let input = fs::read_to_string("src/input.txt").unwrap();
    let mut needed_paper = 0;
    for line in input.split_whitespace() {
        let present = Present::create(line);
        needed_paper += present.needed_paper();
    }
    println!("Needed paper: {needed_paper}");
}

struct Present {
    l: u32,
    w: u32,
    h: u32
}

impl Present {
    fn create(input: &str) -> Self {
        let dimensions: Vec<&str> = input.split('x').collect();
        
        Present {
            l: dimensions.get(0).unwrap().parse().unwrap(),
            w: dimensions.get(1).unwrap().parse().unwrap(),
            h: dimensions.get(2).unwrap().parse().unwrap()
        }
    }

    fn needed_paper(&self) -> u32 {
        let sides: (u32, u32, u32) = (self.l * self.w, self.w * self.h, self.h * self.l);
        let mut smallest_side = sides.0;

        if sides.1 < smallest_side {
            smallest_side = sides.1;
        }

        if sides.2 < smallest_side {
            smallest_side = sides.2;
        }

        (2 * sides.0) + (2 * sides.1) + (2 * sides.2) + smallest_side
    }
}
