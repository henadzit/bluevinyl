import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('f', help='Config file')
    parser.add_argument('m', help='Master')
    args = parser.parse_args()
    
    with open(args.f) as f:
        for l in f:
            l = l.strp()

            if not l:
                continue
            
            if f[0] == '#':
                continue
            
            


if __name__ == '__main__':
    main()
