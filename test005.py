from sys import version_info

if version_info.major == 2:
    if version_info.minor >= 6:
        import multiprocessing
        print(multiprocessing.cpu_count())
    else:
        print("func not supprot!")
else:
    import multiprocessing
    print(multiprocessing.cpu_count())
