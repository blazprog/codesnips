# Write to file
path = os.path.join('/opt/exports', filename)
try:
    with open(path, 'w') as fobj:
        for record in self:
            fobj.write(record.data)
            fobj.write('\n')
except (IOError, OSError) as exc:
    message = 'Unable to save file: %s' % exc
    raise UserError(message)


# Read from file
try:
    with open(filename) as fh:
        for line in fh:
            process(line)
except EnvironmentError as err:
    print(err)

# Read from file and write to file
try:
    with open(source) as fin:
        with open(target, "w") as fout:
            for line in fin:
                fout.write(process(line))
except EnvironmentError as err:
    print(err)

# Without nesting with statements python 3.1 and more
try:
    with open(source) as fin, open(target, "w") as fout:
        for line in fin:
            fout.write(process(line))
except EnvironmentError as err:
    D
    D
    print(err)
