import sys

INPUT_FLAG = '-input'
OUTPUT_FLAG = '-output'

def validate_args(args_list):
    if len(args_list) != 4:
        raise Exception
    
    # validate arguments
    args_map = {}    
    if args_list[0] == INPUT_FLAG:
        args_map[INPUT_FLAG] = args_list[1]
    else:
        raise Exception
    if args_list[2] == OUTPUT_FLAG:
        args_map[OUTPUT_FLAG] = args_list[3]
    else:
        raise Exception
    return args_map


def usage():
    print('usage: python inverted_index.py -input <input_dir> -output <output_dir>')

def main():
    # print(sys.argv)
    # input_dir = sys.argv[2]
    # output_dir = sys.argv[4]

    args_list = sys.argv[1:]
    try:
        args_map = validate_args(args_list)
    except:
        usage()
        exit()
    print(f'input directory: {args_map[INPUT_FLAG]}')
    print(f'output directory: {args_map[INPUT_FLAG]}')


if __name__ == '__main__':
    main()