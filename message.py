#!/usr/bin/env python3

def main(message,input_name):
    if input_name:
        print('enter your name')
        name = input()
    else
        name = 'world'
    print(f'{message} {name}!')

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--message',choices=['hello','goodbye'],default='hello')
    parser.add_argument('--input_name',action='store_true')
    args = parser.parse_args()
    main(args.message,args.input_name)
