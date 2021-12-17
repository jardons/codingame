use std::io;

macro_rules! read_string {
    () => {{
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        input_line.trim_matches('\n').to_string()
    }}
}

macro_rules! char_part {
    ($s:expr, $i:expr) => {{ $s[($i*3)..($i*3)+3].to_string() }}
}

// This macro could be replaced with literal declaration once latest Rust version is available on codingame.
macro_rules! map({
    $($key:expr => $value:expr),+ } => {{
        let mut m = ::std::collections::HashMap::new();
        $(
            m.insert($key, $value);
        )+
        m
    }};
);

fn main() {

    let chars = map!{
        String::from(" _ | ||_|") => 0,
        String::from("     |  |") => 1,
        String::from(" _  _||_ ") => 2,
        String::from(" _  _| _|") => 3,
        String::from("   |_|  |") => 4,
        String::from(" _ |_  _|") => 5,
        String::from(" _ |_ |_|") => 6,
        String::from(" _   |  |") => 7,
        String::from(" _ |_||_|") => 8,
        String::from(" _ |_| _|") => 9
    };

    let line_1: String = read_string!();
    let line_2: String = read_string!();
    let line_3: String = read_string!();
    let l = line_1.len() / 3;
    let mut r = String::from("");

    for i in 0..l {
        let s1:String = char_part!(line_1, i);
        let s2:String = char_part!(line_2, i);
        let s3:String = char_part!(line_3, i);

        let s = s1 + &s2 + &s3;

        r += &chars.get(&s).unwrap().to_string();
    }

    println!("{}", r);
}