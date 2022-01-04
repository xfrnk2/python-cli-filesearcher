from collections import deque
import click
import os



@click.group()
def main():
    """
    Simple CLI for querying books on Google Books by Oyetoke Toby
    """
    pass

@main.command()
@click.argument('name')
def find(name):
    if not validate(name):
        return

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results = search(root_dir, name)
    print_results(results)

def search(start_dir, name):
    queue = deque()
    queue.append((start_dir, os.listdir(start_dir)))
    results = []
    while queue:
        path, files = queue.popleft()
        for file in files:
            temp = path + "\\" + file
            if os.path.isdir(temp):
                queue.append((temp, os.listdir(temp)))
            elif name in temp:
                results.append(temp)
    return results

def print_results(results):
    count = len(results)
    print(f"[탐색 결과] {count}건")
    if count <= 0:
        return
    print("[발견된 위치]")
    for result in results:
        click.echo(result)
    return


def validate(value):
    unusable_name_values = ["/", "|", ":", "*", "?", "<", ">"]
    for char in unusable_name_values:
        if char in value:
            print(f"사용이 불가능한 문자가 포함되어 있습니다. '{char}'")
            return False
    return True

if __name__ == "__main__":
    main()
