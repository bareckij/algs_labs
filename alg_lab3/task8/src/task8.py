def find_k_nearest_points(points, k):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]

if __name__ == "__main__":
    find_k_nearest_points()
