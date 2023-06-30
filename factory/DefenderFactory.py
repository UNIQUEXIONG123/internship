class DefenderFactory:
    def __init__(self, mrad_animation, srad_animation, scng_animation):
        # 分配队列
        self.allocate_list = []
        # 发射队列
        self.launch_list = []
        # 记录弹药量
        self.animation_map = {
            "mrad_animation": mrad_animation,
            "srad_animation": srad_animation,
            "scng_animation": scng_animation
        }

    def generate(self):
        pass
