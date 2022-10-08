use std::io;

fn main() {
    println!("Input an operator from + - * /");
    let operatornum: u8 = get_operator();
    if operatornum == 0 {return}    // Funky guard clause

    let first_operand: f32 = get_operand();
    let second_operand: f32 = get_operand();

    let result: f32 = do_operation(operatornum, first_operand, second_operand);
    println!("Result: {}", result);
}

fn get_operator() -> u8 {
    // We get an input from the user
    let 
    mut input_string = String::new();
    io::stdin().read_line(&mut input_string).ok().expect("Err");

    // Parse input for operator and return 0-4 based on the operator
    // As the numbers will only be small, we return as a u8 for memory
    for character in input_string.chars() {
        if character == '+' {return 1}
        else if character == '-' {return 2}
        else if character == '*' {return 3}
        else if character == '/' {return 4}
    }
    println!("No operator found.");
    return 0;   // Fail
}

fn get_operand() -> f32 {
    let mut num: f32 = 0.0;
    let mut input = String::new();
    
    println!("Enter number: ");
    io::stdin().read_line(&mut input).expect("Not a valid string");
    num = input.trim().parse().expect("Not a valid number");
    
    return num;
} 

fn do_operation(operation: u8, operand1: f32, operand2: f32) -> f32 {
    if operation == 1 {return operand1 + operand2}
    else if operation == 2 {return operand1 - operand2}
    else if operation == 3 {return operand1 * operand2}
    else if operation == 4 {return operand1 / operand2}
    else {return 0.0}
}