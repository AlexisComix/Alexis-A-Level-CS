struct Student {
    _name: String,
    _house: String,   
}
impl Student {
    fn new(name: String, house: String) -> Self {
        Student {
            _name: name,
            _house: house,
        }
    }

    fn as_string(&self) -> String {
        return "Name: ".to_owned()
                 + &self._name
                 + " House: "
                 + &self._house.to_owned();
    }
}

pub fn main() {
    let student: Student = Student::new(String::from("Bob"), String::from("House"));
    println!("{}", student.as_string());
} 