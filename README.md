# Calculator-with-text
Basically this calculator is text into calculator . we give  a operation in text formet and calculate the operation



### Calculator with History – Description

This is a **Python-based menu-driven calculator program** that performs basic operations such as addition, subtraction, multiplication, and division. It uses different functions to perform calculations, display history, clear history, and save calculations. The program stores calculation history in a `history.txt` file using Python file handling.

The program uses `if-elif` conditions to identify the mathematical operator and also checks division by zero. A `while` loop is used to continuously display the menu and take user choices. The main advantages of this program are its simple structure, use of functions, file handling, and history feature. However, it can be improved by adding proper exception handling, an exit option, automatic history saving, and avoiding the use of global variables.


Good Things

Simple to use: Program ka interface simple hai aur ise easily samjha ja sakta hai.
Functions ka use: Different tasks ke liye alag functions banaye gaye hain, jisse code organized rehta hai.
File Handling: Calculations ko history.txt file me save kiya ja sakta hai.
History Feature: User apni previous calculations dekh sakta hai aur history clear bhi kar sakta hai.
Error Checking: Division by zero ko check kiya gaya hai, isliye program invalid division se bach jata hai.
Menu System: Options diye gaye hain, jisse user apne according calculation ya history ka option choose kar sakta hai.

Bad Things

Exit option missing: Program me exit karne ke liye koi separate option nahi diya gaya hai.
Invalid input: Agar user wrong input deta hai, jaise abc + 5, to program error de sakta hai.
Global variable: global result ka use kiya gaya hai, jise return statement se better way me handle kiya ja sakta hai.
Manual saving: Calculation karne ke baad history ko save karne ke liye alag se save option select karna padta hai.
None problem: Agar result ke bina history save karne ki koshish ki jaye, to None file me save ho sakta hai.
