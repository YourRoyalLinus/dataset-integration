import stat
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
                            help="column of measured values (optional)",
                            required=False, default=1)
        parser.add_argument("-i", "--integrate",
                            help="column to represent the variable of "
                            "integration (optional)",
                            required=False, default=0)            
        parser.add_argument("-x", "--x_label", 
                            help="label for x-axis (optional)", 
                            required=False, default=None)
        parser.add_argument("-y", "--y_label", 
                            help="label for y-axis (optional)", 
                            required=False, default=None)
        parser.add_argument("-t", "--title", 
                            help="title for graph (optional)", 
                            required=False, default=None)

        return parser.parse_args()
