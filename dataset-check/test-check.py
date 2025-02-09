import pandas as pd

# List of file paths for datasets from different dates
file_paths = [
    "/Users/rooj/Documents/RP3-Main/RP3-Data/CSE-CIC-IDS2018/DoS-Related/02-15-2018.csv",
    "/Users/rooj/Documents/RP3-Main/RP3-Data/CSE-CIC-IDS2018/DoS-Related/02-16-2018.csv",
    "/Users/rooj/Documents/RP3-Main/RP3-Data/CSE-CIC-IDS2018/DoS-Related/02-20-2018.csv",
    "/Users/rooj/Documents/RP3-Main/RP3-Data/CSE-CIC-IDS2018/DoS-Related/02-21-2018.csv"
    # Add all relevant file paths here
]

# Function to load and inspect datasets
def check_datasets(file_paths):
    reference_columns = None
    attack_types = set()
    
    for file_path in file_paths:
        print(f"Processing file: {file_path}")
        try:
            data = pd.read_csv(file_path)
            
            # Check column compatibility
            if reference_columns is None:
                reference_columns = set(data.columns)
            else:
                current_columns = set(data.columns)
                if current_columns != reference_columns:
                    print(f"Warning: Columns do not match for {file_path}")
                    print(f"Missing or extra columns: {reference_columns.symmetric_difference(current_columns)}")
                else:
                    print("Columns match.")

            # Check attack types
            if 'Label' in data.columns:
                attack_types.update(data['Label'].unique())
            else:
                print(f"Warning: 'Label' column not found in {file_path}")

        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
    
    print("\nSummary:")
    print(f"Columns in the reference dataset: {sorted(reference_columns)}")
    print(f"Attack types across datasets: {sorted(attack_types)}")

# Run the check
check_datasets(file_paths)