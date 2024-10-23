import os

def main():
    directory = "c:/program files"
    report_file = "dirnames.txt"

    print(f"Listing folders in {directory} to {report_file}")
    files = os.listdir(directory)
    abs_path_files = map(lambda file: f"{directory}/{file}", files)
    directories = filter(os.path.isdir, abs_path_files)
    with open(report_file, "w") as file:
        file.write('\n'.join(directories))
        
if __name__ == "__main__":
    main()