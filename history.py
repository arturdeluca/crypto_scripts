from tabulate import tabulate
import re
import pandas as pd


def btc_price_daily():
    # FILE LAST UPDATED ON APRIL 26, 2023 - YAHOO FINANCE
    # FIRST DAY AVAILABLE: SEPTEMBER 17, 2014
    # LAST DAY AVAILABLE: APRIL 26, 2023 - 2:45PM GMT-3
    while True:
        try:
            date = input(
                "\nCORRECT FORMAT IS: YYYY-MM-DD\n   first date available is 2014-09-17\n   last date available is 2023-04-26 2:45PM GMT-3\n\nDATE FOR PRICE LOOKUP\n"
            )
            date_regex = re.compile(
                r"^(?!0000)[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
            )
            ls = []
            if date_regex.match(date):
                df = pd.read_csv("data/BTC_max_daily.csv")
                for d in df["Date"]:
                    ls.append(d)

                if date not in ls:
                    raise ValueError

                else:
                    index_pos = ls.index(date)
                    dfdate = df["Date"][index_pos]
                    dfopen = float(df["Open"][index_pos])
                    dfhigh = float(df["High"][index_pos])
                    dflow = float(df["Low"][index_pos])
                    dfclose = float(df["Close"][index_pos])
                    dfvolume = int(df["Volume"][index_pos])

                    table = [
                        ["Date", dfdate],
                        ["Open", f"$ {dfopen:,}"],
                        ["High", f"$ {dfhigh:,}"],
                        ["Low", f"$ {dflow:,}"],
                        ["Close", f"$ {dfclose:,}"],
                        ["Volume", f"{dfvolume:,}"],
                    ]

                    return tabulate(table, tablefmt="heavy_grid")

            else:
                raise ValueError

        except ValueError:
            print(
                "\nTHIS DATE IS NOT ACCEPTABLE\n   please check the format or spaces before or after date\n"
            )
            print(
                "--------------------------------------------------------------------"
            )


def eth_price_daily():
    # FILE LAST UPDATED ON APRIL 26, 2023 - YAHOO FINANCE
    # FIRST DAY AVAILABLE: NOVEMBER 09, 2017
    # LAST DAY AVAILABLE: APRIL 26, 2023 - 2:45PM GMT-3
    while True:
        try:
            date = input(
                "\nCORRECT FORMAT IS: YYYY-MM-DD\n   first date available is 2017-11-09\n   last date available is 2023-04-26 2:45PM GMT-3\n\nDATE FOR PRICE LOOKUP\n"
            )
            date_regex = re.compile(
                r"^(?!0000)[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
            )
            ls = []
            if date_regex.match(date):
                df = pd.read_csv("data/ETH_max_daily.csv")
                for d in df["Date"]:
                    ls.append(d)

                if date not in ls:
                    raise ValueError

                else:
                    index_pos = ls.index(date)
                    dfdate = df["Date"][index_pos]
                    dfopen = float(df["Open"][index_pos])
                    dfhigh = float(df["High"][index_pos])
                    dflow = float(df["Low"][index_pos])
                    dfclose = float(df["Close"][index_pos])
                    dfvolume = int(df["Volume"][index_pos])

                    table = [
                        ["Date", dfdate],
                        ["Open", f"$ {dfopen:,}"],
                        ["High", f"$ {dfhigh:,}"],
                        ["Low", f"$ {dflow:,}"],
                        ["Close", f"$ {dfclose:,}"],
                        ["Volume", f"{dfvolume:,}"],
                    ]

                    return tabulate(table, tablefmt="heavy_grid")

            else:
                raise ValueError

        except ValueError:
            print(
                "\nTHIS DATE IS NOT ACCEPTABLE\n   please check the format or spaces before or after date\n"
            )
            print(
                "--------------------------------------------------------------------"
            )


def comp_btc():
    while True:
        try:
            date = input(
                "\nCORRECT FORMAT IS: YYYY-MM\n   first month available is 2014-09\n   last month available is 2023-04 2:45PM GMT-3\n\nDATE FOR PRICE LOOKUP\n"
            )

            date_regex = re.compile(r"^(?!0000)[0-9]{4}-(0[1-9]|1[0-2])$")
            ls = []
            if date_regex.match(date):
                df = pd.read_csv("data/BTC_max_monthly.csv")
                date = date + "-01"
                for d in df["Date"]:
                    ls.append(d)

                if date not in ls:
                    raise ValueError

                else:
                    index_pos = ls.index(date)
                    months = {
                        "01": "January",
                        "02": "February",
                        "03": "March",
                        "04": "April",
                        "05": "May",
                        "06": "June",
                        "07": "July",
                        "08": "August",
                        "09": "September",
                        "10": "October",
                        "11": "November",
                        "12": "December",
                    }
                    dfopen = float(df["Open"][index_pos])
                    dfhigh = float(df["High"][index_pos])
                    dflow = float(df["Low"][index_pos])
                    dfclose = float(df["Close"][index_pos])
                    dfvolume = int(df["Volume"][index_pos])

                    dif = float(dfclose - dfopen)
                    dfcomp = dif

                    date_sep = date.split("-")
                    dfdate = months[date_sep[1]]

                    table = [
                        ["Date", f"{dfdate} {date_sep[0]}"],
                        ["Open", f"$ {dfopen:,}"],
                        ["High", f"$ {dfhigh:,}"],
                        ["Low", f"$ {dflow:,}"],
                        ["Close", f"$ {dfclose:,}"],
                        ["Volume", f"{dfvolume:,}"],
                        ["Diference in the Month", f"$ {dfcomp}"],
                    ]

                    return tabulate(table, tablefmt="heavy_grid")

            else:
                raise ValueError

        except ValueError:
            print(
                "\nTHIS DATE IS NOT ACCEPTABLE\n   please check the format or spaces before or after date\n"
            )
            print(
                "--------------------------------------------------------------------"
            )


def comp_eth():
    while True:
        try:
            date = input(
                "\nCORRECT FORMAT IS: YYYY-MM\n   first month available is 2017-12\n   last month available is 2023-04 2:45PM GMT-3\n\nDATE FOR PRICE LOOKUP\n"
            )

            date_regex = re.compile(r"^(?!0000)[0-9]{4}-(0[1-9]|1[0-2])$")
            ls = []
            if date_regex.match(date):
                df = pd.read_csv("data/ETH_max_monthly.csv")
                date = date + "-01"
                for d in df["Date"]:
                    ls.append(d)

                if date not in ls:
                    raise ValueError

                else:
                    index_pos = ls.index(date)
                    months = {
                        "01": "January",
                        "02": "February",
                        "03": "March",
                        "04": "April",
                        "05": "May",
                        "06": "June",
                        "07": "July",
                        "08": "August",
                        "09": "September",
                        "10": "October",
                        "11": "November",
                        "12": "December",
                    }
                    dfopen = float(df["Open"][index_pos])
                    dfhigh = float(df["High"][index_pos])
                    dflow = float(df["Low"][index_pos])
                    dfclose = float(df["Close"][index_pos])
                    dfvolume = int(df["Volume"][index_pos])

                    dif = float(dfclose - dfopen)
                    dfcomp = dif

                    date_sep = date.split("-")
                    dfdate = months[date_sep[1]]

                    table = [
                        ["Date", f"{dfdate} {date_sep[0]}"],
                        ["Open", f"$ {dfopen:,}"],
                        ["High", f"$ {dfhigh:,}"],
                        ["Low", f"$ {dflow:,}"],
                        ["Close", f"$ {dfclose:,}"],
                        ["Volume", f"{dfvolume:,}"],
                        ["Diference in the Month", f"$ {dfcomp}"],
                    ]

                    return tabulate(table, tablefmt="heavy_grid")

            else:
                raise ValueError

        except ValueError:
            print(
                "\nTHIS DATE IS NOT ACCEPTABLE\n   please check the format or spaces before or after date\n"
            )
            print(
                "--------------------------------------------------------------------"
            )


def main():
    while True:
        try:
            op = input(
                "DO YOU WANT TO LOOKUP?\n\n  1. BTC prices in a certain data\n  2. ETH prices in a certain data\n  3. BTC prices and data of a certain month\n  4. ETH prices and data of a certain month\n\n PLEASE USE 1, 2, 3, OR 4 to select your option\n"
            ).lower()

            if op == "1":
                print("\nBITCOIN\n")
                print(btc_price_daily())
                print("\n\n")

            elif op == "2":
                print("\nETHER\n")
                print(eth_price_daily())
                print("\n\n")

            elif op == "3":
                print("\nBITCOIN\n")
                print(comp_btc())
                print("\n\n")

            elif op == "4":
                print("\nETHER\n")
                print(comp_eth())
                print("\n\n")

            else:
                raise ValueError

        except ValueError:
            print("\nOPTION NOT AVAILABLE\n")


if __name__ == "__main__":
    main()
