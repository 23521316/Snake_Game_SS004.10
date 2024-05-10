def play_step(self):
    self._handle_input()
    if not self.game_started:
        self.display.fill(BLACK)
        self.menu.draw()
    else:
        self._move_snake()
        self._check_collision()
        self._update_ui()
    pygame.display.flip()
    self.clock.tick(self.frame_rate)  # Limit the frame rate here
    