# Bash Practice: Beginner to Advanced

## Beginner (1-10)
1. Print the path of your current directory.
2. Create a directory projects with three subdirectories a, b, c inside it, in one command.
3. Create an empty file notes.txt inside projects/a.
4. List all files (including hidden ones) in long format with human-readable sizes.
5. Copy people.csv into projects/b/ and rename it to backup.csv in the same command.
6. Create a file temp.txt containing the text temporary (using echo), then move it into projects/c/.
7. Show the first 2 lines and the last 2 lines of people.csv.
8. Count the number of lines in people.csv.
9. Store your username in a variable called name (using command substitution) and print Hello, <your username>.
10. Delete projects/a along with everything inside it.

## Intermediate (11-20)
11. Show only the lines in app.log that contain ERROR.
12. Count how many ERROR lines are in app.log.
13. Print only the names (first column) from people.csv.
14. Sort people.csv by age (2nd column), oldest first.
15. Count how many times each fruit appears in fruits.txt, most frequent first.
16. Save the ERROR lines of app.log into errors.txt, then append the WARN lines to the same file.
17. Using a pipe, show the 3 largest files in the current directory.
18. Find all .txt files in the current directory and all subdirectories.
19. Using awk, print only the names of people from India.
20. Replace every apple with mango in fruits.txt and save the result to fruits_new.txt, without changing the original.

## Advanced (21-30)
21. Create a script hello.sh that prints Hello from script. Make it executable and run it.
22. Create greet.sh that takes a name as an argument and prints Hello, <name>. If no argument is given, print a usage message to stderr and exit with code 1.
23. Using loops, create file1.txt to file5.txt, then rename each one to end in .bak.
24. Using a while read loop, read people.csv and print <name> is <age> years old for each line.
25. Write a function is_even that takes a number and prints even or odd. Test it with 4 and 7.
26. Find all .txt files recursively and count the words in each using xargs.
27. Run ls people.csv nonexistent so normal output goes to out.txt and the error goes to err.txt.
28. Using awk, print the sum and average of all ages in people.csv.
29. Create a compressed archive of the projects folder named with today's date, like backup_2026-09-19.tar.gz. The date must come from a command, not typed by hand.
30. Final challenge: write log_summary.sh that takes a log file as an argument. If the file doesn't exist, print an error to stderr and exit 1. Otherwise, print how many lines contain each level, like INFO: 2, WARN: 1, ERROR: 2. Run it on app.log.
