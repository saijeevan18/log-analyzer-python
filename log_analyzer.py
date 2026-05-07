error_count = 0
warning_count = 0
info_count = 0
total_logs = 0

error_dict = {}

try:
    file = open("log.txt", "r")

    for line in file:
        line = line.strip()
        total_logs += 1

        if "ERROR" in line:
            error_count += 1

            if line in error_dict:
                error_dict[line] += 1
            else:
                error_dict[line] = 1

        elif "WARNING" in line:
            warning_count += 1

        elif "INFO" in line:
            info_count += 1

    file.close()

    # Most frequent error
    most_error = ""
    max_count = 0

    for key in error_dict:
        if error_dict[key] > max_count:
            max_count = error_dict[key]
            most_error = key

    # OUTPUT
    print("\n===== LOG ANALYSIS REPORT =====\n")

    print("Total Logs Processed =", total_logs)
    print("Errors =", error_count)
    print("Warnings =", warning_count)
    print("Info =", info_count)

    # Most frequent error
    if most_error != "":
        print("\nMost Frequent Error =", most_error)
        print("Occurred =", max_count, "times")

    # Critical alert
    if error_count > 3:
        print("\nCRITICAL ALERT: Too many errors detected!")

    # Search keyword
    keyword = input("\nEnter keyword to search in logs: ")

    file = open("log.txt", "r")

    print("\nSearch Results:\n")

    found = False

    for line in file:
        if keyword.lower() in line.lower():
            print(line.strip())
            found = True

    if not found:
        print("No matching logs found.")

    file.close()

    # Save report
    report = open("report.txt", "w")

    report.write("===== LOG ANALYSIS REPORT =====\n\n")
    report.write(f"Total Logs Processed = {total_logs}\n")
    report.write(f"Errors = {error_count}\n")
    report.write(f"Warnings = {warning_count}\n")
    report.write(f"Info = {info_count}\n")

    if most_error != "":
        report.write(f"\nMost Frequent Error = {most_error}\n")
        report.write(f"Occurred = {max_count} times\n")

    if error_count > 3:
        report.write("\nCRITICAL ALERT: Too many errors detected!\n")

    report.close()

    print("\nReport saved successfully in report.txt")

except FileNotFoundError:
    print("Error: log.txt file not found!")