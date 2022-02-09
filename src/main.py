import utils
import calculations
from file.datafile import DataFile
from file.manage.load import  load_file
from graph import graph

def main():
    args = utils.parse_command_line()
    data_file = DataFile(args.file)
    x_vals, y_vals = load_file(data_file, (int(args.interval), int(args.data)))
    i = calculations.integrate(x_vals, y_vals)
    
    graph.graph(x_vals, y_vals, i, args.source_graph, args.integrated_graph)

    #TODO
    #Reorganize/Cleanup/Optimize/Docstrings
    
if __name__ == "__main__":
    main()   