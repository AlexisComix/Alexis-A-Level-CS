use std::io::stdin;

fn main() {
    /*
    Main program function
    */

    // Initialise variables
    let mut board = [["-"; 3]; 3];  // Make a 3x3 board array
    let mut current_player: &str = "X";

    // Function calls
    print_welcome();

    // Main loop
    loop {
        let mut is_game_won: bool = false;
        // Get the index for the input
        let mut input_index: i32 = get_input_index();
        if input_index == -1 {return;}

        // Place piece at the index
        board = place_piece(board, &input_index, &current_player);

        // Change player
        if current_player == "X" {current_player = "O";} else {current_player = "X";}

        // Print current board stat
        print_board(board);

        if is_game_won {break;}
    }
}

fn print_welcome() {
    /*
    Print a welcome message and the indexes for each box.
    */
    print!("\x1B[2J\x1B[1;1H"); // Stack overflow magic to clear the terminal
    print!("Welcome to noughts and crosses! On each turn, {}",
           "input the index for where you want to play!\n");
    
    // Print the indexes for the board
    println!("1 2 3");
    println!("4 5 6");
    println!("7 8 9");
}

fn print_board(board: [[&str; 3]; 3]) {
    /*
    This function prints the board in its current state to the screen.
    */
    for i in board {            // Iterate through rows
        for j in i {            // Iterate through cols
            print!("{} ", j);   // Print item
        }   
        println!();             // Newline
    }
}

fn get_input_index() -> i32 {
    /*
    Get input from the user and return the number if it is between 1 and 9 (inclusive)
    */
    let mut number: i32 = 0;

    let mut valid: bool = false;
    while !valid {
        match number {
            // 1 to 9 inclusive
            1..=9 => {          
                // Return the number if it is valid
                valid = true;
                return number;
            }
            _ => {
                // Take input from the user as a String
                let mut input_string = String::new();
                stdin().read_line(&mut input_string)
                    .ok()
                    .expect("Failed to read line");
                
                // Convert the input to an i32 
                    number = input_string
                    .trim()
                    .parse()
                    .expect("This string cannot be converted to a number");
            }
        }
    }
    
    return -1;  // Fail state
}

fn place_piece<'a>(mut board: [[&'a str; 3]; 3], index: &i32, player: &'a str) -> [[&'a str; 3]; 3] {
    /*
    Place a piece on the board with the index given from the player
    */
    // Integer division
    let y: i32 = (index - 1) / 3;   // Gets the row for the piece as i32
    
    // Gets the col as i32
    let x1: i32 = (index % 3) - 1;     // Funky and cringe maths
    let mut x2: i32;
    if x1 < 0 {x2 = 2;} else {x2 = x1;}     // If it is -1, the index should be 2
    
    // Convert x and y to usize
    let row: usize = usize::try_from(y).unwrap();
    let col: usize = usize::try_from(x2).unwrap();
    
    if board[row][col] == "-" {
        board[row][col] = player;   // Set piece in place if free
    } else {
        panic!("Place on board taken, cheater!")    // cba to loop and wait for valid
    }

    return board;
}