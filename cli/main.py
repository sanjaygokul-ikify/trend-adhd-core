import argparse
from services.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', type=str, required=True)
    args = parser.parse_args()
    orchestrator = Orchestrator()
    result = orchestrator.run(args.prompt)
    print(result[0])

if __name__ == '__main__':
    main()