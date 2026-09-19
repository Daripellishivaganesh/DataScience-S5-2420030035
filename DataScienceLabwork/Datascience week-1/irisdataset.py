import pandas as pd

def main():
    df = pd.read_csv('Iris.csv')

    print('First 10 rows:')
    print(df.head(10), end='\n\n')

    print('Last 10 rows:')
    print(df.tail(10), end='\n\n')

    print('Info:')
    df.info()
    print('\nShape:', df.shape)

    print('\nDescription:')
    print(df.describe())


if __name__ == '__main__':
    main()