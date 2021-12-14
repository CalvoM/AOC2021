use std::fs;

//get_file_contents: read the content of the file provided as string
fn get_file_contents(filename: String) -> String{
    let contents = fs::read_to_string(filename).expect("Something went wrong with reading the file");
    contents
}

//get_heights: split the string content along \n to get heights
fn get_heights(content: String) -> Vec<u32>{
    let v_str: Vec<&str> = content.split("\n").collect();
    let mut v_int: Vec<u32> = Vec::new();
    for s in v_str.iter(){
        if s.len()> 0{
        let i: u32 = s.parse::<u32>().unwrap();
        v_int.push(i);
        }
    }
    v_int
}


fn main() {
    let input = get_file_contents(String::from("../input.txt"));
    let heights: Vec<u32> = get_heights(input);
    let mut inc: i32 = 0;
    let mut prev: i32 = -1;
    for h in heights.iter(){
        if prev == -1{
            prev = *h as i32;
    }else{
        if *h as i32 > prev{
            inc = inc + 1;
        }
        prev = *h as i32;
    }

    }
    println!("{}", inc);
}
