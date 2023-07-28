import matplotlib.pyplot as plt
import pandas as pd

def get_dataset(dataset: str = 'datasets/santanilla.csv') -> pd.DataFrame:
  """
  Parameters
  ----------
  dataset_link: string
    A link to a raw .csv file of the dataset (e.g., raw.githubusercontent)
    Default is a public link to the Santanilla dataset.

  Returns
  -------
  df: DataFrame
    Dataset as a pandas DataFrame with null-yield datapoints dropped.
  
  Notes
  -----
  This function also outputs basic summarizing statistics.
  """
  # Input validation
  if not isinstance(dataset, str):
    raise Exception("get_dataset() input is not of type str.")

  # Read data from raw GitHub link
  df = pd.read_csv(dataset, index_col=0)

  # Ensure that 'Yield' column exists
  if 'Yield' not in df.columns:
    raise Exception("No column named 'Yield' in the dataset.")

  # Drop rows with NaN yields
  original_num_rows = len(df)
  df = df.dropna(subset=['Yield'])
  num_rows_dropped = original_num_rows - len(df)

  # Exploratory Data Analysis
  plt.figure(figsize=(4,4))
  plt.hist(df['Yield'])
  plt.title("Dataset Reaction Yields")
  plt.xlabel("Yield")
  plt.ylabel("Counts")
  plt.show()
  print("----- SUMMARIZING STATISTICS -----")
  print("Dropped {} datapoints due to null yields\n".format(num_rows_dropped))
  print("Number of Total Reactions =", len(df))
  print("Yield mean =", df['Yield'].mean())
  print("Yield standard deviation = {}\n".format(df['Yield'].std()))

  for col in df.columns:
    print("Number of Unique {}s =".format(col), df[col].nunique())
  
  return df

get_dataset()