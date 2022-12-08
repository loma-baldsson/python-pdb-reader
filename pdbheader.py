from pdbread import get_byte, get_word, get_dword, get_string
from pdbwrite import put_byte, put_word, put_dword, put_string


class PDBHeader:
    def __init__(self):
        self.name = ""
        self.attributes = 0
        self.version = 0
        self.creation_time = 0
        self.modification_time = 0
        self.backup_time = 0
        self.modification_number = 0
        self.app_info_offset = 0
        self.sort_info_offset = 0
        self.type = 0
        self.creator = 0
        self.unique_id = 0
        self.next_record_id = 0
        self.num_records = 0

    @classmethod
    def load_from_file(cls, file):
        self = cls()

        self.name = get_string(file, 32, True)
        self.attributes = get_word(file)
        self.version = get_word(file)
        self.creation_time = get_dword(file)
        self.modification_time = get_dword(file)
        self.backup_time = get_dword(file)
        self.modification_number = get_dword(file)
        self.app_info_offset = get_dword(file)
        self.sort_info_offset = get_dword(file)
        self.type = get_string(file, 4)
        self.creator = get_string(file, 4)
        self.unique_id = get_dword(file)
        self.next_record_id = get_dword(file)
        self.num_records = get_word(file)

        return self

    def write_to_file(self, file):
        put_string(file, self.name, 32, True)
        put_word(file, self.attributes)
        put_word(file, self.version)
        put_dword(file, self.creation_time)
        put_dword(file, self.modification_time)
        put_dword(file, self.backup_time)
        put_dword(file, self.modification_number)
        put_dword(file, self.app_info_offset)
        put_dword(file, self.sort_info_offset)
        put_string(file, self.type, 4)
        put_string(file, self.creator, 4)
        put_dword(file, self.unique_id)
        put_dword(file, self.next_record_id)
        put_word(file, self.num_records)

    def __str__(self):
        out = f"name: {self.name!r}\n"
        out += f"attributes: {self.attributes!r}\n"
        out += f"version: {self.version!r}\n"
        out += f"creation_time: {self.creation_time!r}\n"
        out += f"modification_time: {self.modification_time!r}\n"
        out += f"backup_time: {self.backup_time!r}\n"
        out += f"modification_number: {self.modification_number!r}\n"
        out += f"app_info_offset: {self.app_info_offset!r}\n"
        out += f"sort_info_offset: {self.sort_info_offset!r}\n"
        out += f"type: {self.type!r}\n"
        out += f"creator: {self.creator!r}\n"
        out += f"unique_id: {self.unique_id!r}\n"
        out += f"next_record_id: {self.next_record_id!r}\n"
        out += f"num_records: {self.num_records!r}\n"

        return out


# TODO: Make getter/setter methods for each attribute
