#!/usr/bin/python2
"""
Copyright 2020, Ernesto Corbellini

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from urllib import urlopen
import csv
import matplotlib.pyplot as plt


class Covid19Reader(object):
    """
    A class to read data from the covid19 public repo.
    The data represents the number of confirmed infected cases
    by country and by date
    """

    FIELD_COLUMNS = {"Province": 0,
                     "Country": 1,
                     "Latitude": 2,
                     "Longitud": 3,
                     "Start date": 4}

    def __init__(self, url=None):
        if not url:
            data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
        else:
            data_url = url
        data = urlopen(data_url)
        csv_data = csv.reader(data)
        # read the dates fields
        line = next(csv_data)
        self.dates = line[self.FIELD_COLUMNS["Start date"]:]
        # load the data for every country
        self.country_data = []
        for row in csv_data:
            self.country_data.append(row)

    def get_country_data(self, country):
        """ Return a data vector for a specified country """
        for row in self.country_data:
            if row[self.FIELD_COLUMNS["Country"]] == country:
                return {"dates": self.dates, "infected": row[self.FIELD_COLUMNS["Start date"]:]}
        return None


test = Covid19Reader()
data = test.get_country_data("Argentina")
print data

start = 35
plt.plot(data["infected"][start:])
plt.title("Casos confirmados de Covid19 en Argentina")
plt.xlabel("Fecha en dias desde el %s" % data["dates"][start])
plt.ylabel("Infectados")
plt.show()
