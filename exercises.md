Bash Practice: Beginner to Advanced

Run this setup once so every question has files to work with:
bash
mkdir -p ~/bash-practice && cd ~/bash-practice
printf "alice,25,India\nbob,30,Germany\ncarol,22,India\ndave,35,USA\neve,28,Germany\n" > people.csv
printf "apple\nbanana\napple\ncherry\nbanana\napple\n" > fruits.txt
printf "2026-09-01 INFO Server started\n2026-09-01 ERROR Disk full\n2026-09-02 WARN High m
Beginner (1-10)
Print the path of your current directory.
Create a directory projects with three subdirectories a, b, c inside it, in one command.
Create an empty file notes.txt inside projects/a.
List all files (including hidden ones) in long format with human-readable sizes.
Copy people.csv into projects/b/ and rename it to backup.csv in the same command.
Create a file temp.txt containing the text temporary (using echo), then move it into projects/c/.
Show the first 2 lines and the last 2 lines of people.csv.
Count the number of lines in people.csv.
Store your username in a variable called name (using command substitution) and print Hello, <your username>.
Delete projects/a along with everything inside it.
