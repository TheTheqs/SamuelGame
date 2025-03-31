# Used to load the background when necessary
def with_background(render_method):
    def wrapper(self, screen, *args, **kwargs):
        screen.blit(self.background, (0, 0))
        return render_method(self, screen, *args, **kwargs)

    return wrapper
