from CommandLine.command_line_parser import CommandLineParser
from file.datafile import DataFile
from file.manage.load import  load_file

from Integration import calculate
from Utils import utils
from Output import display

def main():
    args = CommandLineParser.parse()
    data_file = DataFile(args.file)
    src_config = utils.get_graph_configs(args.source_graph)
    int_config = utils.get_graph_configs(args.integrated_graph)
    x_vals, y_vals = load_file(data_file, (int(args.interval), int(args.data)))
    i = calculate.integral(x_vals, y_vals)
    
    display.graph(x_vals, y_vals, i, src_config, int_config)

    #TODO
    #Reorganize/Cleanup/Optimize/Docstrings
    
if __name__ == "__main__":
    main()   