import pandas as pd
import json


def main():
    cleaner = NoxCleaner()
    df = cleaner.clean()

    stats = NoxStatistics(df)

    stats.simple()
    stats.overall_top(10)
    stats.annual_top(5)


class NoxCleaner:

    def __init__(self):
        self.df = pd.read_csv('input_data/noxrating.csv', sep=';')

    def __score_override(self):
        """
        Override known false scores with manual checked scores.
        """
        # Manual override of known bad values
        with open("input_data/score_override.json", "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
        for yid in data:
            self.df.loc[self.df['id'] == yid, 'score'] = data[yid]

    def __save(self):
        self.df.to_csv('results/dataset.csv')

    def clean(self):
        self.__score_override()

        # Drop rows with any empty cells (no score)
        self.df = self.df[self.df['score'].notna()]

        # Parse Dates to readable format for pandas
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')

        # Sort descending on score
        self.df = self.df.sort_values(by=['score', 'date'], ascending=False, ignore_index=True)

        # Save the cleaning process
        self.__save()

        return self.df


class NoxStatistics:

    def __init__(self, df):
        self.df = df
        self.markdown_mode = True

    def simple(self):
        print('Score Statistics:')
        print(self.df['score'].describe())

    def overall_top(self, top=10):
        """
        Prints the overall top 10 of all the datapoints
        :param top:
        :param df:
        """
        self.df = self.df.sort_values(by=['score', 'date'], ascending=False)
        # print(self.df.head(n=top).to_string(index=False))
        # To print in markdown notation
        print(self.df.drop(['id'], axis=1).head(n=top).to_markdown(index=False))

    def annual_top(self, top=10):
        """
        Gets the annual Top boardgames
        :param top:
        """
        # Grouping and other functions are not saved
        df = self.df.copy()
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df_group = df.groupby(df['date'].dt.year.rename('year'))

        for year in reversed(sorted(df_group.groups.keys())):
            df_year = df_group.get_group(year)
            df_year = df_year.sort_values(by=['score'], ascending=False)

            if self.markdown_mode:
                df_year['link'] = '<a href="' + df_year['link'] + '">YouTube</a>'
                print('### ' + str(year))
                print(df_year.drop(['id'], axis=1).head(n=top).to_markdown(index=False))
                print()
                print()
            else:
                print(df_year.head(n=top).to_string(index=False))


if __name__ == "__main__":
    main()
