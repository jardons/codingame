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

        for c in $v.to_string().chars() {
            r += c.to_string().parse::<i64>().unwrap()
        }

        r
    }}
}

fn main() {

    let tgt = read_int!();
    let mut m = ::std::collections::HashSet::new();

    for i in 1..tgt
    {
        let mut n = i;
        while n <= tgt && !m.contains(&n)
        {
            m.insert(n);
            n = follow_flow!(n);
        }
    }

    println!("{}", if m.contains(&tgt) { "YES" } else { "NO" });
}