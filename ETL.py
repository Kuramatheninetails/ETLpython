import pandas as pd

# Step 1: Extract

# Load raw data from CSV file
input_path = r"F:\archive (2)\creditcard.csv"  # Change path if needed
try:
    df = pd.read_csv(input_path)
    print("✅ Data loaded successfully.")
except FileNotFoundError:
    print(f"❌ File not found at: {input_path}")
    exit()


# Step 2: Transform


# Rename column 'Class' to 'is_fraud' for clarity
if 'Class' in df.columns:
    df.rename(columns={'Class': 'is_fraud'}, inplace=True)

# Add a new column: transaction_hour (if 'Time' column exists)
if 'Time' in df.columns:
    df['transaction_hour'] = (df['Time'] / 3600).astype(int)

# Flag high-value transactions
df['high_value'] = df['Amount'].apply(lambda x: 1 if x > 2000 else 0)

# Risk scoring function
def risk_score(row):
    if row['high_value'] == 1 and row['is_fraud'] == 1:
        return 5
    elif row['high_value'] == 1:
        return 3
    elif row['is_fraud'] == 1:
        return 4
    else:
        return 1

df['risk_score'] = df.apply(risk_score, axis=1)

# Drop unnecessary columns (optional)
df.drop(columns=['Time'], errors='ignore', inplace=True)


# Step 3: Load

output_path = r"F:\archive (2)\cleaned_transactions.csv"
df.to_csv(output_path, index=False)
print(f"✅ ETL pipeline completed. Cleaned data saved to: {output_path}")