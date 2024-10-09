import revolt

class EmbedField:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Embed(revolt.SendableEmbed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = []
        self.raw_description = str(kwargs.get('description', None))

    @property
    def description(self):
        if self.fields:
            return self.raw_description + '\n\n' + '\n\n'.join([f'**{field.name}**\n{field.value}' for field in self.fields])
        else:
            return self.raw_description

    @description.setter
    def description(self, value):
        self.raw_description = value

    def add_field(self, name, value):
        self.fields.append(EmbedField(name, value))

    def clear_fields(self):
        self.fields = []

    def insert_field_at(self, index, name, value):
        self.fields.insert(index, EmbedField(name, value))

    def remove_field(self, index):
        self.fields.pop(index)

    def set_field_at(self, index, name, value):
        self.fields[index] = EmbedField(name, value)
