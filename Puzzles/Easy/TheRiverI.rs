use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

macro_rules! read_int {
    () => {{
        let mut input_line = String::new();
        std::io::stdin().read_line(&mut input_line).unwrap();
        parse_input!(input_line, i64)
    }}
}

macro_rules! follow_flow {
    ($v:expr) => {{
        let mut r = $v;
        let mut s = $v.to_string();

        for c in $v.to_string().chars() {
            r += c.to_string().parse::<i64>().unwrap()
        }

        r
    }}
}

fn main() {

    let mut r1 = read_int!();
    let mut r2 = read_int!();

    while r1 != r2 {
        if r1 < r2 {
            r1 = follow_flow!(r1);
        } else {
            r2 = follow_flow!(r2);
        }
    }

    println!("{}", r1);
}