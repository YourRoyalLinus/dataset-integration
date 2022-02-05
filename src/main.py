from CommandLine.command_line_parser import CommandLineParser
from DataFile.datafile import DataFile
from DataFile.file_manager import load_file
from Integration import integrate
import plotext as plt

def main():
    args = CommandLineParser.parse()
    data_file = DataFile(args.file)
    x, y = load_file(data_file, (args.integrate, args.data))
    i = integrate.integral(x, y)

    plt.plot(i)
    plt.xlabel("Day")
    plt.ylabel("Cumulative Cases")
    plt.show()


if __name__ == "__main__":
    main()   