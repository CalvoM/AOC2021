use std::fs;

fn get_file_contents(filename: String) -> String {
    fs::read_to_string(filename).expect("Something went wrong with reading the file")
}

fn get_inst(content: String) -> Vec<String> {
    content.split("\n").map(|s| s.to_string()).collect()
}
fn soln(){
    let contents = get_file_contents(String::from("../input2.txt"));
    let insts = get_inst(contents);
    let mut hor: usize = 0;
    let mut ver: usize = 0;
    for i in insts.iter(){
        if i.len()> 0{
        let config: Vec<String> = i.split(" ").map(|s| s.to_string()).collect();
        let key = &config[0];
        let value: usize = config[1].parse().unwrap();
        if key == "forward"{
            hor = hor + value;
        }else if key == "up"{
            ver = ver - value;
        }else if key == "down"{
            ver = ver + value;
        }

        }
    }
    println!("{}", ver * hor);
}
fn main() {
    soln()
}

