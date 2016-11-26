import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True, help='Config file')
    parser.add_argument('-m', required=True, help='Master')
    args = parser.parse_args()
    
    with open(args.f) as f:
        subprocess.call('pacmd unload-module module-ladspa-sink', shell=True)

        for l in f:
            l = l.strip()

            if not l:
                continue
            
            if l[0] == '#':
                continue
            
            load_mod(args.m, l.split(','))
            
            
def load_mod(master, values):
    cmd = 'pacmd load-module module-ladspa-sink sink_name=bluevinyl master={} plugin={} label={} control={}'.format(
           master, values[0], values[1], ','.join(values[2:]))
    print('executing: {}'.format(cmd))
    subprocess.call(cmd, shell=True)



if __name__ == '__main__':
    main()
