awk -F ',' -v OFS=',' '$3 == ""{a=$2; $2 = "none"; $3=a};1' example.txt

