class TravellingSalesmanSolver:
    def __init__(self):
        self.cities = ["A", "B", "C", "D", "E", "F"]
        self.distances = {
            "A": {"A": 0, "B": 10, "C": 15, "D": 20, "E": 25, "F": 30},
            "B": {"A": 10, "B": 0, "C": 35, "D": 25, "E": 17, "F": 28},
            "C": {"A": 15, "B": 35, "C": 0, "D": 30, "E": 28, "F": 40},
            "D": {"A": 20, "B": 25, "C": 30, "D": 0, "E": 22, "F": 16},
            "E": {"A": 25, "B": 17, "C": 28, "D": 22, "E": 0, "F": 35},
            "F": {"A": 30, "B": 28, "C": 40, "D": 16, "E": 35, "F": 0},
        }

    def find_shortest_route(self):
        start_city = "A"
        remaining_cities = ["B", "C", "D", "E", "F"]

        # Helper function returns best path and distance
        def explore(current_city, remaining, path, distance_so_far):
            if not remaining:
                # return to start
                distance_so_far += self.distances[current_city][start_city]
                return path + [start_city], distance_so_far

            best_distance = 99999
            best_path = []

            for next_city in remaining:
                # remove the city we're moving to from remaining cities
                updated_remaining_cities = [remaining_city for remaining_city in remaining if remaining_city != next_city]

                new_path, new_distance = explore(
                    next_city,
                    updated_remaining_cities,
                    path + [next_city],
                    distance_so_far + self.distances[current_city][next_city]
                )

                if new_distance < best_distance:
                    best_distance = new_distance
                    best_path = new_path

            return best_path, best_distance

        # start exploring from start_city
        shortest_path, total_distance = explore(start_city, remaining_cities, [start_city], 0)
        return {"shortest_route": shortest_path, "total_distance": total_distance}
