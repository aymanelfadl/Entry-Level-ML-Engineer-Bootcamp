import time

def ft_progress(lst):
    start_time = time.time()
    for i in range(1, len(lst) + 1):  
        elapsed = time.time() - start_time 
        speed = elapsed / i 
        eta = (len(lst) - i) * speed  
        
        bar = "=" * int(75 * i // len(lst)) + ">" + " " * (75 - int(75 * i // len(lst)))
        print(f"\rETA: {eta:.2f}s [{(i / len(lst)) * 100:.2f}%][{bar}] {i}/{len(lst)} | elapsed time {elapsed:.2f}s", end='', flush=True)

        yield i - 1

if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)

    print("\nDone!")
    print(ret)
