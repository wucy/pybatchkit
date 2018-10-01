import concurrent.futures

def run_process_jobs(func, job_array, num_worker=4, timeout=120):
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=num_worker)
    fut_lst = list()
    for args in job_array:
        if isinstance(args, (list, tuple)):
            future = executor.submit(func, *args)
        else:
            future = executor.submit(func, args)
        fut_lst.append(future)
    result = list()
    for fut in fut_lst:
        result_item = None
        try:
            result_item = fut.result(timeout=timeout)
        except Exception as e:
            print(e)
            result_item = None
        if result_item == None:
            continue
        result.append(result_item)
    return result

if __name__ == '__main__':
    def test_proc_func(arg):
        return arg
    test_proc_lst = [2, 4, 6, 7, 8]
    test_proc_res = run_process_jobs(test_proc_func, test_proc_lst)
    print test_proc_res == [2, 4, 6, 7, 8]
