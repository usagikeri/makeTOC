import string

import yaml


def makeTemplate(templatefile):
    with open(templatefile, 'r') as f:
        template = string.Template(f.read())

    return template


def makeDict(yamlfile):
    with open(yamlfile, 'r') as f:
        y = yaml.load(f)
    return y


def makeRow(dic):
    d = dict(B3='',B4='',M1='')
    keys = dic.keys()
    print(keys)

    for i in keys:
        temp = dic[i]
        d[i] = ''.join(['{} & {} & {} \\\\\n\\hline\n'.format(*x)
                        for x in temp])

    return d


def main():
    template = makeTemplate('template.txt')
    y = makeDict('member.yaml')
    d = makeRow(y)
    result = template.substitute(d)
    print(result)


if __name__ == '__main__':
    main()
