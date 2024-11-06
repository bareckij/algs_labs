def count_intervals(data):
    segment_count, point_count = data[0][0], data[0][1]
    intervals = [x for x in data[1:1 + segment_count]]
    points = data[-1]

    events = []
    point_results = {}

    for start, end in intervals:
        events.append([start, "L"])  
        events.append([end, "R"])    
    
    for point in points:
        events.append([point, "P"])  
        point_results[point] = 0

    events.sort()

    active_segments = 0
    for position, event_type in events:
        if event_type == "L":
            active_segments += 1
        elif event_type == "R":
            active_segments -= 1
        elif event_type == "P":
            point_results[position] = active_segments

    return [point_results[point] for point in points]

if __name__ == "__main__":
    count_intervals()
