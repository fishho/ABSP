import os, re, shutil

def fill_gaps(folder, prefix):
    filename_re = re.compile(r'{}(\d+)\.(.*)'.format(re.escape(prefix)))
    name = lambda match: match.group(0)
    number = lambda match: int(match.group(1))
    ext = lambda match: match.group(2)

    # A list of regular expression matches for all filenames that fit the
    # pattern, sorted numerically. filter(None,...) eliminates false values,
    # namely the failed re.match(...) calls that returned None.
    matches = sorted(filter(None, (
        filename_re.match(entry.name)
        for entry in os.scandir(folder)
        if entry.is_file()
    )), key = number)

    if not matches: return

    first_num = number(matches[0])

    width = max(len(match.group(1)) for match in matches)

    for n, match in enumerate(matches, first_num):
         old_name = os.path.join(folder, name(match))
         new_name = os.path.join(
             folder,
             '{}{:0{width}}.{}'.format(prefix, n, ext(match), width = width)
         )
         if new_name != old_name:
             if os.path.exists(new_name):
                 raise FileExistsError(new_name)

             shutil.move(old_name, new_name)