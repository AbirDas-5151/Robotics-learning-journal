## Beginner
#1.
pwd

#2.
mkdir -p projects/{a,b,c}

#3.
touch projects/a/notes.txt

#4.
ls -lah

#5.
cp people.csv projects/b/backup.csv

#6.
echo "temporary" > temp.txt
mv temp.txt projects/c/

#7.
head -n 2 people.csv
tail -n 2 people.csv

#8.
wc -l people.csv          # or: wc -l < people.csv (number only)

#9.
name=$(whoami)
echo "Hello, $name"

#10.
rm -r projects/a

# 11
grep ERROR app.log

# 12
grep -c ERROR app.log     # or: grep ERROR app.log | wc -l

# 13
cut -d, -f1 people.csv

# 14
sort -t, -k2 -nr people.csv

# 15
sort fruits.txt | uniq -c | sort -nr
# expected: 3 apple / 2 banana / 1 cherry

# 16
grep ERROR app.log > errors.txt
grep WARN app.log >> errors.txt

# 17
ls -S | head -3

# 18
find . -name "*.txt"

# 19
awk -F, '$3=="India" {print $1}' people.csv
# expected: alice, carol

# 20
sed 's/apple/mango/g' fruits.txt > fruits_new.txt

# 21
cat > hello.sh << 'EOF'
#!/bin/bash
echo "Hello from script"
EOF
chmod +x hello.sh
./hello.sh

# 22  (greet.sh)
#!/bin/bash
if [ $# -eq 0 ]; then
  echo "Usage: $0 <name>" >&2
  exit 1
fi
echo "Hello, $1"
# test: ./greet.sh Sam   and   ./greet.sh; echo $?   (should print 1)

# 23
for i in {1..5}; do touch file$i.txt; done
for f in file*.txt; do mv "$f" "${f%.txt}.bak"; done

# 24
while IFS=, read -r name age country; do
  echo "$name is $age years old"
done < people.csv

# 25
is_even() {
  if (( $1 % 2 == 0 )); then
    echo "even"
  else
    echo "odd"
  fi
}
is_even 4
is_even 7

# 26
find . -name "*.txt" -print0 | xargs -0 wc -w

# 27
ls people.csv nonexistent > out.txt 2> err.txt

# 28
awk -F, '{sum+=$2} END {print "Sum:", sum, "Average:", sum/NR}' people.csv
# expected: Sum: 140  Average: 28

# 29
tar -czf backup_$(date +%F).tar.gz projects/

# 30  (log_summary.sh)
#!/bin/bash
if [ ! -f "$1" ]; then
  echo "Error: file not found" >&2
  exit 1
fi
for level in INFO WARN ERROR; do
  count=$(grep -c "$level" "$1")
  echo "$level: $count"
done
# run: chmod +x log_summary.sh && ./log_summary.sh app.log
# expected: INFO: 2 / WARN: 1 / ERROR: 2
