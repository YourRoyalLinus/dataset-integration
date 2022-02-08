from CommandLine.command_line_parser import CommandLineParser
from DataFile.datafile import DataFile
from DataFile.file_manager import load_file
from Integration import calculate
from Utils import utils
from Output import display

def main():
    args = CommandLineParser.parse()
    data_file = DataFile(args.file)
    src_config = utils.get_graph_configs(args.source_graph)
    int_config = utils.get_graph_configs(args.integrated_graph)
    x, y = load_file(data_file, (int(args.interval), int(args.data)))
    i = calculate.integral(x, y)
    
    display.graph(x, y, i, src_config, int_config)

    #TODO
    #Reorganize/Cleanup/Optimize/Docstrings
    
if __name__ == "__main__":
    main()   