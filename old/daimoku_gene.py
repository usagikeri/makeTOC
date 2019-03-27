import csv


def conv_tex(filename):
    with open('{}.csv'.format(filename), 'r') as f:
        reader = csv.reader(f)
        return ['{} & {} & {} \\\\\n\hline\n'.format(*raw[:3]) for raw in reader]


if __name__ == '__main__':
    MEMBER = dict(B3='', B4='', M1='')

    with open('temple.tex', 'r') as f:
        template = f.read()

    for i in MEMBER.keys():
        with open('{}.csv'.format(i), 'r') as f:
            template = template.replace('<replace_point_{}>'.format(str(i)),
                                        ''.join(conv_tex(i)))

    with open('out.tex', 'w') as wf:
        wf.write(template)
