
class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, game_settings):
        """Initialize statistics."""
        self.game_settings = game_settings
        self.reset_stats()
        # Start game in an inactive state
        self.game_active = False

    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.game_settings.ship_limit