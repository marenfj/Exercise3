packets_data = [
    {'id': 1, 'arr': 0}, {'id': 2, 'arr': 0},
    {'id': 3, 'arr': 1}, {'id': 4, 'arr': 1},
    {'id': 6, 'arr': 2}, {'id': 5, 'arr': 3}, 
    {'id': 7, 'arr': 3}, {'id': 8, 'arr': 5}, 
    {'id': 9, 'arr': 5}, {'id': 10, 'arr': 7},
    {'id': 11, 'arr': 8}, {'id': 12, 'arr': 8}
]

def task_a_fifo():
    queue, results = [], []
    time = 0
    remaining = list(packets_data)
    
    while remaining or queue:
        while remaining and remaining[0]['arr'] <= time:
            queue.append(remaining.pop(0))
            
        if not queue:
            time = remaining[0]['arr']
            continue
            
        queue.sort(key=lambda p: (p['arr'], p['id']))
        pkt = queue.pop(0)
        
        results.append((pkt['id'], time - pkt['arr']))
        time += 1
        
    avg = sum(d for _, d in results) / len(results)
    
    print("Task A (FIFO) - [Packet ID: Delay]:")
    for pid, delay in results:
        print(f"P{pid}: {delay}", end=" | ")
    print(f"\nAverage Delay: {avg:.3f}\n")

def task_b_priority():
    queue, results = [], []
    time = 0
    remaining = list(packets_data)
    
    while remaining or queue:
        while remaining and remaining[0]['arr'] <= time:
            queue.append(remaining.pop(0))
            
        if not queue:
            time = remaining[0]['arr']
            continue
            
        queue.sort(key=lambda p: (p['id'] % 2 == 0, p['arr'], p['id']))
        pkt = queue.pop(0)
        
        results.append((pkt['id'], time - pkt['arr']))
        time += 1
        
    f1_delays = [d for p, d in results if p % 2 != 0]
    f2_delays = [d for p, d in results if p % 2 == 0]
    avg = sum(d for _, d in results) / len(results)
    
    print("Task B (Priority) - [Packet ID: Delay]:")
    for pid, delay in results:
        print(f"P{pid}: {delay}", end=" | ")
    print(f"\nAvg F1 (Odd): {sum(f1_delays)/len(f1_delays):.3f}")
    print(f"Avg F2 (Even): {sum(f2_delays)/len(f2_delays):.3f}")
    print(f"Overall Avg: {avg:.3f}")

task_a_fifo()
task_b_priority()

