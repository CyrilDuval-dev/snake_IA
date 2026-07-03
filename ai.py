from collections import deque
from position import Position

DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}

OPPOSITE = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT",
}


class SnakeAI:
    """IA algorithmique (pathfinding) pour jouer au Snake automatiquement.

    Stratégie, dans l'ordre :
    1. Chercher le plus court chemin (BFS) vers la pomme, en évitant le corps
       du serpent (la case de la queue est considérée comme libre car elle
       aura bougé au prochain tour, sauf si le serpent va grandir).
    2. Si aucun chemin vers la pomme n'existe, choisir la direction voisine
       valide qui laisse le plus d'espace libre accessible (flood fill),
       pour survivre le plus longtemps possible plutôt que de foncer dans
       un cul-de-sac.
    3. En dernier recours, garder la direction actuelle.
    """

    def __init__(self, grid):
        self.grid = grid

    def get_next_direction(self, snake, food):
        head = snake.body[0]

        path = self._bfs(head, food.position, snake)
        if path:
            next_cell = path[0]
        else:
            next_cell = self._best_survival_move(head, snake)

        if next_cell is None:
            return snake.direction

        return self._direction_from_cells(head, next_cell)

    def _direction_from_cells(self, head, next_cell):
        d_row = next_cell.row - head.row
        d_col = next_cell.column - head.column
        for direction, (dr, dc) in DIRECTIONS.items():
            if (dr, dc) == (d_row, d_col):
                return direction
        return None

    def _valid_neighbors(self, pos, obstacles):
        neighbors = []
        for _, (dr, dc) in DIRECTIONS.items():
            new_row = pos.row + dr
            new_col = pos.column + dc
            if self.grid.is_inside(new_row, new_col):
                candidate = Position(new_row, new_col)
                if candidate not in obstacles:
                    neighbors.append(candidate)
        return neighbors

    def _bfs(self, start, goal, snake):
        obstacles = set(snake.body)
        tail = snake.body[-1]
        # La queue va se libérer au prochain déplacement (sauf en cas de
        # croissance juste après), on peut donc la traverser sans risque.
        obstacles.discard(tail)

        queue = deque([start])
        came_from = {start: None}

        while queue:
            current = queue.popleft()
            if current == goal:
                return self._reconstruct_path(came_from, start, goal)
            for neighbor in self._valid_neighbors(current, obstacles):
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    queue.append(neighbor)

        return None

    def _reconstruct_path(self, came_from, start, goal):
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    def _best_survival_move(self, head, snake):
        obstacles = set(snake.body)
        best_move = None
        best_score = -1

        for direction, (dr, dc) in DIRECTIONS.items():
            if direction == OPPOSITE.get(snake.direction):
                continue  # ne jamais faire demi-tour sur soi-même
            new_row = head.row + dr
            new_col = head.column + dc
            if not self.grid.is_inside(new_row, new_col):
                continue
            candidate = Position(new_row, new_col)
            if candidate in obstacles:
                continue
            score = self._flood_fill(candidate, obstacles)
            if score > best_score:
                best_score = score
                best_move = candidate

        return best_move

    def _flood_fill(self, start, obstacles):
        visited = {start}
        queue = deque([start])
        count = 0
        while queue:
            current = queue.popleft()
            count += 1
            for neighbor in self._valid_neighbors(current, obstacles | visited):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return count