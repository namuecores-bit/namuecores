import random
import tkinter as tk

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BRICK_ROWS = 5
BRICK_COLUMNS = 10
BRICK_WIDTH = 56
BRICK_HEIGHT = 20
BRICK_PADDING = 4
PADDLE_WIDTH = 300
PADDLE_HEIGHT = 12
BALL_RADIUS = 8
BALL_SPEED = 4

class BrickBreaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Brick Breaker")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="#20232a")
        self.canvas.pack()

        self.score = 0
        self.lives = 3
        self.game_over = False

        self.create_bricks()
        self.create_paddle()
        self.create_ball()
        self.create_labels()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.restart_game)

        self.update_game()

    def create_bricks(self):
        self.bricks = []
        colors = ["#e63946", "#f77f00", "#fcbf49", "#a8dadc", "#457b9d"]
        start_y = 40
        for row in range(BRICK_ROWS):
            brick_row = []
            for col in range(BRICK_COLUMNS):
                x1 = BRICK_PADDING + col * (BRICK_WIDTH + BRICK_PADDING)
                y1 = start_y + row * (BRICK_HEIGHT + BRICK_PADDING)
                x2 = x1 + BRICK_WIDTH
                y2 = y1 + BRICK_HEIGHT
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colors[row % len(colors)], outline="#111")
                brick_row.append(brick)
            self.bricks.append(brick_row)

    def create_paddle(self):
        paddle_x = (WINDOW_WIDTH - PADDLE_WIDTH) / 2
        paddle_y = WINDOW_HEIGHT - 40
        self.paddle = self.canvas.create_rectangle(
            paddle_x, paddle_y,
            paddle_x + PADDLE_WIDTH, paddle_y + PADDLE_HEIGHT,
            fill="#8ecae6", outline="#023047"
        )
        self.paddle_speed = 0

    def create_ball(self):
        start_x = WINDOW_WIDTH / 2
        start_y = WINDOW_HEIGHT / 2
        self.ball = self.canvas.create_oval(
            start_x - BALL_RADIUS, start_y - BALL_RADIUS,
            start_x + BALL_RADIUS, start_y + BALL_RADIUS,
            fill="#ffb703", outline="#fb8500"
        )
        self.ball_dx = BALL_SPEED * random.choice([-1, 1])
        self.ball_dy = -BALL_SPEED

    def create_labels(self):
        self.score_label = self.canvas.create_text(90, 15, text=f"Score: {self.score}", fill="#ffffff", font=("Arial", 14, "bold"))
        self.lives_label = self.canvas.create_text(540, 15, text=f"Lives: {self.lives}", fill="#ffffff", font=("Arial", 14, "bold"))
        self.message_label = self.canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, text="", fill="#ffffff", font=("Arial", 24, "bold"))

    def move_left(self, event=None):
        self.paddle_speed = -8

    def move_right(self, event=None):
        self.paddle_speed = 8

    def restart_game(self, event=None):
        if self.game_over:
            self.canvas.delete("all")
            self.score = 0
            self.lives = 3
            self.game_over = False
            self.create_bricks()
            self.create_paddle()
            self.create_ball()
            self.create_labels()

    def update_game(self):
        if not self.game_over:
            self.move_paddle()
            self.move_ball()
            self.check_collisions()
            self.update_labels()
            if self.lives <= 0:
                self.end_game("Game Over")
            elif self.remaining_bricks() == 0:
                self.end_game("You Win!")

        self.root.after(16, self.update_game)

    def move_paddle(self):
        if self.paddle_speed == 0:
            return
        x1, y1, x2, y2 = self.canvas.coords(self.paddle)
        new_x1 = max(0, x1 + self.paddle_speed)
        new_x2 = min(WINDOW_WIDTH, x2 + self.paddle_speed)
        if new_x1 == 0:
            new_x2 = PADDLE_WIDTH
        if new_x2 == WINDOW_WIDTH:
            new_x1 = WINDOW_WIDTH - PADDLE_WIDTH
        self.canvas.coords(self.paddle, new_x1, y1, new_x2, y2)

    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        x1, y1, x2, y2 = self.canvas.coords(self.ball)

        if x1 <= 0 or x2 >= WINDOW_WIDTH:
            self.ball_dx = -self.ball_dx
        if y1 <= 0:
            self.ball_dy = -self.ball_dy
        if y2 >= WINDOW_HEIGHT:
            self.lives -= 1
            self.reset_ball_and_paddle()

    def reset_ball_and_paddle(self):
        paddle_x = (WINDOW_WIDTH - PADDLE_WIDTH) / 2
        paddle_y = WINDOW_HEIGHT - 40
        self.canvas.coords(self.paddle, paddle_x, paddle_y, paddle_x + PADDLE_WIDTH, paddle_y + PADDLE_HEIGHT)
        ball_x = WINDOW_WIDTH / 2
        ball_y = WINDOW_HEIGHT / 2
        self.canvas.coords(
            self.ball,
            ball_x - BALL_RADIUS, ball_y - BALL_RADIUS,
            ball_x + BALL_RADIUS, ball_y + BALL_RADIUS
        )
        self.ball_dx = BALL_SPEED * random.choice([-1, 1])
        self.ball_dy = -BALL_SPEED

    def check_collisions(self):
        ball_coords = self.canvas.coords(self.ball)
        overlapping = self.canvas.find_overlapping(*ball_coords)
        if self.paddle in overlapping:
            self.ball_dy = -abs(self.ball_dy)
            paddle_coords = self.canvas.coords(self.paddle)
            ball_center = (ball_coords[0] + ball_coords[2]) / 2
            paddle_center = (paddle_coords[0] + paddle_coords[2]) / 2
            offset = (ball_center - paddle_center) / (PADDLE_WIDTH / 2)
            self.ball_dx = BALL_SPEED * offset

        for row in self.bricks:
            for brick in row:
                if brick in overlapping:
                    self.canvas.delete(brick)
                    row.remove(brick)
                    self.ball_dy = -self.ball_dy
                    self.score += 10
                    return

    def remaining_bricks(self):
        return sum(len(row) for row in self.bricks)

    def update_labels(self):
        self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}")
        self.canvas.itemconfig(self.lives_label, text=f"Lives: {self.lives}")

    def end_game(self, message):
        self.game_over = True
        self.canvas.itemconfig(self.message_label, text=message + "\nPress Space to Restart")
        self.ball_dx = 0
        self.ball_dy = 0
        self.paddle_speed = 0


if __name__ == "__main__":
    root = tk.Tk()
    game = BrickBreaker(root)
    root.mainloop()
