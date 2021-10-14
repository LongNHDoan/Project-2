"""
Author: Ngoc Hoang Long Doan
Created on: 14/10/2021
"""
import pandas as pd
import numpy as np


def annualCountryCo2Data(df):
    """
    Extract co2 emission per capita/country from 1900-2019
    """
    years = np.linspace(1900, 2019, 120)
    # Extract rows with year = 2019. Select the columns: country and co2
    df = df[df["year"].isin(years)][['country', 'co2_per_capita', 'year', 'co2']].reset_index(drop=True)
    # Replace all NaN with 0
    df = df.fillna(0)
    # Write to a new .csv file
    df.to_csv("Countries_Annual_Co2.csv")

    return None


def annualIndustryCo2Data(df):
    """
    Extract co2 emission data per industries from 1900-2019
    """
    # Extract data
    df = df[['coal_co2', 'cement_co2', 'flaring_co2', 'gas_co2', 'oil_co2', 'other_industry_co2', 'year']].fillna(0)
    df['other_industry_co2'] += df['flaring_co2'] + df['cement_co2']
    df.drop(['cement_co2', 'flaring_co2'], axis=1, inplace=True)
    df.rename(columns={'coal_co2': 'Coal', 'gas_co2': 'Gas', 'oil_co2': 'Oil',
                       'other_industry_co2': 'Other Industries'}, inplace=True)
    # Convert to long format
    df = df.melt(id_vars=['year'], var_name='Type', value_name='Co2 Emission')
    fun = {'Co2 Emission': 'sum'}
    df = df.groupby(['year', 'Type']).agg(fun)

    # Output
    df.to_csv('Industry_Annual_Co2.csv')

    return None

def annualWorldCo2Data(df):
    """
    Extract annual world total (per capita) co2 emission data 1900-2019
    """
    # Extract data
    df = df[['year', 'co2', 'co2_per_capita']]
    df = df[df['year'] >= 1900]
    df = df.groupby('year').agg(sum)

    # Output
    df.to_csv('World_Annual_Co2.csv')

def main():
    # Import file
    df = pd.read_csv("owid-co2-data.csv")

    # Extract world annual co2 emission data
    annualCountryCo2Data(df)

    # Extract industries annual co2 emission data
    annualIndustryCo2Data(df)

    # Extract world annual co2 emission data
    annualWorldCo2Data(df)


if __name__ == "__main__":
    main()
