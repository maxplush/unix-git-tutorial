#!/usr/bin/python3

def main(message):
    print(f'{message} world!')

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--message',choices=['hello','goodbye'])
    args = parser.parse_args()
    main(args.message)
