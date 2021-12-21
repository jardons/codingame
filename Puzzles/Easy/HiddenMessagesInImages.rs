use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<i32>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let inputs = input_line.split(" ").collect::<Vec<_>>();

    let w = parse_input!(inputs[0], i32);
    let h = parse_input!(inputs[1], i32);

    let mut v: u8 = 0;
    let mut s = String::new();
    let mut j = 0;
    for i in 0..h as usize {
        let mut inputs = String::new();
        io::stdin().read_line(&mut inputs).unwrap();

        for t in inputs.split_whitespace() {
            v = (v<<1) + (parse_input!(t, usize) & 1) as u8;

            if j == 7 {
                s += &(v as char).to_string();
                v = 0;
                j = 0;
            }
            else {
                j += 1;
            }
        }
    }

    println!("{}", s);
}