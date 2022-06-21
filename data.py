class AddonData:
    data: dict = {}
    is_loaded: bool = False

    @classmethod
    def load(cls):
        if 'icon_id' not in cls.data:
            cls.data['obj'] = None
            cls.data['icon_id'] = None
        cls.is_loaded = True

    @classmethod
    def set_preview_obj(cls, obj):
        cls.data['obj'] = obj

    @classmethod
    def set_icon_id(cls, icon_id):
        cls.data['icon_id'] = icon_id
