#Text_Wrap
import textwrap

def wrap(string, max_width):
    l = " ".join(textwrap.wrap(string,max_width))
    return textwrap.fill(l,max_width)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)