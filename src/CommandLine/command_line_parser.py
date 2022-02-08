import argparse

class CommandLineParser:
    def __init__(self):
        pass

    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(prog='dataset-integration')

        parser.add_argument("-f", "--file", 
                            help="data file path (required)", required=True)
        parser.add_argument("-d", "--data",
                            help="column of measured values (optional). "
                            "Defaults to column 1 (0-indexed)",
                            required=False, default=1)
        parser.add_argument("-i", "--interval",
                            help="column to represent the period of the data "
                            " (optional). "
                            "Defaults to column 0 (0-indexed)",
                            required=False, default=0)            
        parser.add_argument("--source_graph", 
                            help="\"XLABEL | YLABEL | TITLE | COLOR\" for the " 
                            "source data graph separated by the '|' character "
                            "(optional)", 
                            required=False, default=None)
        parser.add_argument("--integrated_graph", 
                            help="\"XLABEL | YLABEL | TITLE | COLOR\" for the "
                            "integrated graph separated by the '|' character "
                            "(optional)", 
                            required=False, default=None)

        return parser.parse_args()
